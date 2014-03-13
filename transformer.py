import parsing
import scraper
import lists
import re

meatTypes = {"chicken": '0500', "beef": "1300", "pork": "1000"}
substitutions = {
				"ground poultry": "canned, drained cannellini beans",
				"ground beef": "canned, drained red kidney beans",
				"ground pork": "canned, drained red kidney beans",
				"ground other": "canned, drained black beans",
				"poultry": "firm tofu",
				"beef": "portobello mushrooms"
				}

def getRecipe(recipeURL):
	#temporary
	lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
	lists.updateNameDB()
	###
	recipeInfo = scraper.retrieveRecipe(recipeURL)
	recipe = parsing.buildRecipeObject(recipeInfo)

	return recipe


def getMeats(ingredients):
	# TODO: Include seafood as meat
	meatCategories = ['0500', '0700', '1000', '1300', '1700','1500']
	meats = []
	groundMeats = []
	categories = []
	for ingredient in ingredients:
		if ingredient.category.strip() in meatCategories:
			if re.search("(?i).*ground.*", ingredient.name):
				groundMeats.append(ingredient)
			meats.append(ingredient)
			categories.append(ingredient.category.strip())

	return {
			"meats": meats,
			"groundMeats": groundMeats,
			"categories": categories
			}



def vegTransformer(recipe): #TODO: include seafood and liquids (sauces, broths)
	ingredients = recipe.ingredients

	meatInfo = getMeats(ingredients)
	meats = meatInfo["meats"]
	categories = meatInfo["categories"]
	groundMeats = meatInfo["groundMeats"]

	newSteps = recipe.directions

	# Transform ingredient list
	# TODO: veal? fish? Sausage?
	if len(meats):
		print 'NAME: ', recipe.name
		if len(groundMeats):
			# Replace ground meats with beans
			meatType = groundMeats[0].category.strip()
			groundMeat = re.search("(?i)ground .*", groundMeats[0].origName).group()
			if meatType == meatTypes["chicken"]:
				newSteps = subsituteMeat(groundMeat, substitutions["ground poultry"], newSteps)
			elif meatType == meatTypes["beef"] or meatType == meatTypes["pork"]:
				newSteps = subsituteMeat(groundMeat, substitutions["ground beef"], newSteps)
			else:
				newSteps = subsituteMeat(groundMeat, substitutions["ground other"], newSteps)
		
		elif meatTypes["chicken"] in categories or \
			isStirFry(recipe) or isDeepFried(recipe):
			meat = meats[0].name.split(',')[0].lower()
			newSteps = subsituteMeat(meat, substitutions["poultry"], newSteps)
			# TODO: Add extra prep steps for tofu (drain, dry, cut into cubes,  pan-fry first?)
		
		elif meatTypes["beef"] or meatTypes["pork"]:
			meat = meats[0].name.split(',')[0].lower()
			newSteps = subsituteMeat(meat, substitutions["beef"], newSteps)
		else:
			print 'Remove all meats'
			meat = meats[0].name.split(',')[0].lower()
			newSteps = subsituteMeat(meat, "", newSteps)
			
	else:
		# There are no meats in this recipe => already vegetarian
		print "No transformation performed, recipe contains no meat"

	print "New Directions\n====================\n", newSteps


def isStirFry(recipe):
	pat = "stir-fry"
	isStirFry = False
	if re.search("(?i).*%s.*" % pat, recipe.name):
		isStirFry = True

	return isStirFry


def isDeepFried(recipe):
	isFried = False
	if "fry" in recipe.methods:
		isFried = True

	return isFried


def subsituteMeat(ingredient, substitution, directions):
	newSteps = directions
	print "!! Substituting ", ingredient, " with ", substitution
	# Substitute meats for substitute ingredient
	for i, step in enumerate(directions):
		if re.search("(?i).*%s.*" % ingredient, step):
			newStep = re.sub("(?i)%s" % ingredient, substitution, step)
			newSteps[i] = newStep

	# TODO: Handle mentions of meat, grease, fat, beef, chicken, turkey, pork, etc. Also pink on inside, [cooking method] until ___
		# Tofu, completely remove meat sentences? Add in new tofu cooking steps?

	return newSteps


def main():
	# recipe = getRecipe('http://allrecipes.com/recipe/spaghetti-sauce-with-ground-beef/')
	recipe = getRecipe('http://allrecipes.com/recipe/shepherds-pie-vi/')
	# recipe = getRecipe('http://allrecipes.com/recipe/chicken-stir-fry-3/')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Flavorful-Beef-Stir-Fry-3/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stir%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i2')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Crispy-Deep-Fried-Bacon/Detail.aspx?event8=1&prop24=SR_Thumb&e11=deep%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i17')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Beef-Stew-V/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stew&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i5')
	print recipe.unicode()
	vegTransformer(recipe)


main()


'''
Notes for Vegetarian substitutions:
- Tofu 
	* good for pork, chicken, beef (use extra-firm tofu)
	* typically used to replace meat-heavy dishes (stir-fry, salad, fajitas)
	* still need to season tofu, but maybe not as much as the meat
	* probably need to reduce cooking time
- Beans
	* Can use to substitute for ground meat in things like chili, etc
	* Use sturdier beans (black, pinto, red kidney - canned beans)
	*  cannellini beans, garbanzo beans for ground chicken/turkey. Red kidney beans for ground beef 
- Remove all meat
	* For recipes that already contain proprotionally very little meat, and/or lots of other proteins
	* Remove all if meat is not the main ingredient
- Mushroom
	* Portobello to replace large pieces/slabs of meat (burger patty, steak, sandwich meat, etc)
- Eggplant
	* Similar to mushroom, but perhaps for chicken and turkey? (chicken parmigiana)
#~0500~^~Poultry Products~
#~0700~^~Sausages and Luncheon Meats~
#~1000~^~Pork Products~
#~1300~^~Beef Products~
#~1700~^~Lamb, Veal, and Game Products~
#~1500~^~Finfish and Shellfish Products~
'''
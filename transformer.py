import parsing
import scraper
import lists
import re
import pprint

meatTypes = {"chicken": '0500', "beef": "1300", "pork": "1000"}
substitutions = {
				"ground poultry": "cannellini beans",
				"ground beef": "red kidney beans",
				"ground pork": "red kidney beans",
				"ground other": "black beans",
				"poultry": "firm tofu",
				"beef": "portobello mushrooms"
				}


##### TRANSFORMERS ######
def vegTransformer(recipe): #TODO: include seafood and liquids (sauces, broths)
	ingredients = recipe.ingredients

	meatInfo = getMeats(ingredients)
	meats = meatInfo["meats"]
	categories = meatInfo["categories"]
	groundMeats = meatInfo["groundMeats"]
	ingredients = meatInfo["ingredients"]
	newSteps = recipe.directions

	if len(meats):
		substitution = ""
		meat = meats[0].name.split(',')[0].lower()
		if len(groundMeats):	# Replace ground meats with beans
			meatType = groundMeats[0].category.strip()
			if meatType == meatTypes["chicken"]:
				substitution = substitutions["ground poultry"]
			elif meatType == meatTypes["beef"] or meatType == meatTypes["pork"]:
				substitution = substitutions["ground beef"]
			else:
				substitution = substitutions["ground other"]

		elif meatTypes["chicken"] in categories or isStirFry(recipe) or isDeepFried(recipe):	# Replace poultry, stir-fry, fried things with tofu
			substitution = substitutions["poultry"]		
		elif meatTypes["beef"] or meatTypes["pork"]:	# Replace with mushrooms
			substitution =  substitutions["beef"]
		else:	# Remove all meats
			print 'Remove all meats'
			substitution = ""

		performVegSub(meat, substitution, ingredients, newSteps)
		
	else:
		print "No transformation performed, recipe contains no meat"

	printRecipe(recipe.name, ingredients, newSteps)


##### SUBSTITUTIONS ######
def performVegSub(meat, substitution, ingredients, steps):
	newSteps = vegSubDirections(meat, substitution, steps)
	newIngredients = vegSubIngredients(ingredients, substitution)

	return {
			"steps": newSteps, 
			"ingredients": newIngredients
			}


def vegSubDirections(ingredient, substitution, directions):
	# TODO: look/replace broths first before meats
	newSteps = directions
	print "!! Substituting ", ingredient, " with ", substitution
	# Substitute meats for substitute ingredient
	for i, step in enumerate(directions):
		newStep = step
		if re.search("(?i).*ground %s.*" % ingredient, step):
			newStep = re.sub("(?i)ground %s" % ingredient, substitution, step)
		elif re.search("(?i).*%s.*" % ingredient, step):
			newStep = re.sub("(?i)%s" % ingredient, substitution, step)
			
		newStep = sanitizeMeatDirections(newStep, substitution)

		newSteps[i] = newStep


	return newSteps


def sanitizeMeatDirections(step, substitution):
	# TODO: remove any mentions of meat (beef, chicken, turkey, sausage, pork, etc)
	# Get rid of meat related directions
	meatyWords = ["grease", "until", "fat", "meat"]
	sentences = step.split(".")
	meatlessStep = ""
	for sentence in sentences:
		for word in meatyWords:
			if word == "until":
				if re.search("(?i).*(%s|%s).*" % (substitution, 'meat'), sentence):
					if re.search("(?i).*%s" % word, sentence):
						print "REMOVING Directions: ", sentence, " - ", word
						sentence = re.sub("(?i) until.*[;]", ";", sentence)
						sentence = re.sub("(?i) until.*$", "", sentence)

			elif word == "meat":
				if re.search("(?i).*%s" % word, sentence):
					print "REMOVING Directions: ", sentence, " - ", word		
					sentence = ""
			else:
				if re.search("(?i).*%s" % word, sentence):
					print "REMOVING Directions: ", sentence, " - ", word
					sentence = re.sub("(?i).*%s" % word, "", sentence)
					sentence = re.sub('^[,:;] ', "", sentence).capitalize()

		if sentence:
			meatlessStep += ". " + sentence

	return meatlessStep


def vegSubIngredients(ingredients, substitution):
	newIngredient = parsing.findIngredient(substitution)
	newIngredient.amount = ""
	newIngredient.unit = ""
	newIngredient.updateString()
	newIngredients =  ingredients.append(newIngredient)

	return ingredients	


##### INGREDIENT/METHODS INFO ######
def getMeats(ingredients):
	# TODO: Include seafood as meat
	meatCategories = ['0500', '0700', '1000', '1300', '1700','1500']
	meats = []
	groundMeats = []
	categories = []
	meatlessIngredients = []
	for ingredient in ingredients:
		if ingredient.category.strip() in meatCategories:
			if re.search("(?i).*ground.*", ingredient.name):
				print "found ground"
				groundMeats.append(ingredient)
			meats.append(ingredient)
			categories.append(ingredient.category.strip())
		else:
			meatlessIngredients.append(ingredient)

	return {
			"meats": meats,
			"groundMeats": groundMeats,
			"categories": categories,
			"ingredients": meatlessIngredients
			}


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


##### PRINTING ######
def printRecipe(name, ingredients, steps):
	print "RECIPE: Vegetarian ", name, "\n"
	print "Ingredients\n====================\n", printIngredients(ingredients)
	print "Directions\n====================\n"
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(steps)


def printIngredients(ingredients):
	for i in ingredients:
		print i.name, " - ", i.category


##### RECIPE INFO ######
def getRecipe(recipeURL):
	#temporary
	lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
	lists.updateNameDB()
	###
	recipeInfo = scraper.retrieveRecipe(recipeURL)
	recipe = parsing.buildRecipeObject(recipeInfo)

	return recipe


def main():
	# recipe = getRecipe('http://allrecipes.com/recipe/spaghetti-sauce-with-ground-beef/')
	# recipe = getRecipe('http://allrecipes.com/recipe/shepherds-pie-vi/')
	# recipe = getRecipe('http://allrecipes.com/recipe/chicken-stir-fry-3/')
	recipe = getRecipe('http://allrecipes.com/Recipe/Flavorful-Beef-Stir-Fry-3/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stir%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i2')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Crispy-Deep-Fried-Bacon/Detail.aspx?event8=1&prop24=SR_Thumb&e11=deep%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i17')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Beef-Stew-V/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stew&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i5')
	# print recipe.unicode()

	vegTransformer(recipe)


main()
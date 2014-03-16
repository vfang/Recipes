from lists import cuisines as cuisines
import lists, scraper, parsing
# Lists
from lists import poultryAndGame as poultryAndGame,\
livestock as livestock, \
stocks as stocks, \
seafood as seafood


meatsCategories = ['0500', '0700', '1000','1300','1700']

def cuisineChange(recipe, cuisineType):
	if cuisineType == "indian":
		changeToIndian(recipe)
	elif cuisineType == "chinese":
		changeToChinese(recipe)
	elif cuisineType == "mexican":
		changeToMexican(recipe)

def changeToIndian(recipe):
	ingredients = recipe.ingredients
	cuisineMeats = cuisines["indian"]["meats"]
	for ing in ingredients:
		# category
		category = ing.category
		if category in meatsCategories:
			print ing.unicode()
			# name
			meat = ing.name
			meatInDescriptor = findMeatDescriptor(ing.descriptor, cuisineMeats)
			print 'MEATS: ', meat, ", ", meatInDescriptor
			if meat not in cuisineMeats and meatInDescriptor not in cuisineMeats:
				# Replace with meat in cuisineMeats
				if meat in (poultryAndGame + seafood) or meatInDescriptor in (poultryAndGame + seafood):
					# chicken
					ing.name = "chicken"
					ing.descriptor = "boneless"
				else:
					# lamb/mutton
					ing.name = "mutton"
					ing.descriptor = ""	
				print ing.unicode()


	

def findMeatDescriptor(descriptor, cuisineMeats):
	words = descriptor.split(' ')
	meat = ''
	# print words
	for word in words:
		if word in cuisineMeats:
			meat = word
			break
	return meat

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
	# recipe = getRecipe('http://allrecipes.com/recipe/chicken-stir-fry-3/')
	recipe = getRecipe('http://allrecipes.com/Recipe/Flavorful-Beef-Stir-Fry-3/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stir%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i2')
	
	cuisineChange(recipe, "indian")

main()

# Go through ings
	# Check category, name, descriptor
	# If meat not in cuisine meats
		# Replace meat
			# Poultry + fish -> chicken
			# Else -> non chicken
	# Cheese
		# Indian, all cheese -> cottage cheese
		# Asian, remove all cheese
		# Mexican, oaxaca cheese
	# Breads
		# Indian, naan
		# Chinese, ignore
		# Mexican, tortilla
	# Veggies
		# If not veggie list
			# Replace


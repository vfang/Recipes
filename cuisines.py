from lists import cuisines as cuisines
import lists, scraper, parsing,re
# Lists
from lists import poultryAndGame as poultryAndGame,\
livestock as livestock, \
stocks as stocks, \
seafood as seafood


meatsCategories = ['0500', '0700', '1000','1300','1700']
cheeseCategory = ['0100']
sauceCategory = ['0600']

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
	cuisineCheese = cuisines['indian']['cheese']
	for ing in ingredients:
		# category
		category = ing.category
		#check the meats used in recipe
		if category in meatsCategories:
			print ing.unicode()
			# name
			meat = ing.name
			meatInDescriptor = findInDescriptor(ing.descriptor, cuisineMeats)
			#print 'MEATS: ', meat, ", ", meatInDescriptor
			if meat not in cuisineMeats and meatInDescriptor not in cuisineMeats:
				# Replace with meat in cuisineMeats
				if meat in (poultryAndGame + seafood) or meatInDescriptor in (poultryAndGame + seafood):
					# chicken
					ing.name = "chicken"
					ing.descriptor = "boneless"
				else:
					# lamb/mutton
					ing.name = "mutton"	
				print ing.unicode()
		#replace cheese with indian cheese
		if category in cheeseCategory:
			pat = re.search("cheese*",ing.name.lower())
			pat2 = re.search("cheese*",ing.descriptor.lower())
			if pat or pat2:
				print ing.unicode()
				cheese = ing.name
				cheeseInDescriptor = findInDescriptor(ing.descriptor,cuisineCheese) 
				#print 'CHEESE: ', cheese, ", ", cheeseInDescriptor
				if cheese not in cuisineCheese and cheeseInDescriptor not in cuisineCheese:
					#replace cheese with indian cheese
					ing.name = "cottage cheese"
					ing.descriptor = ""
					print ing.unicode()
		#replace bread with naan if not pastry (i.e. cake, pie)... this is tough....
		#replace sauces....

'''
def changeToMexican(recipe):
	ingredients = recipe.ingredients
	cuisineMeats = cuisines["mexican"]["meats"]
	cuisineCheese = cuisines['mexican']['cheese']
	for ing in ingredients:
		# category
		category = ing.category
		#check the meats used in recipe
		if category in meatsCategories:
			print ing.unicode()
			# name
			meat = ing.name
			meatInDescriptor = findInDescriptor(ing.descriptor, cuisineMeats)
			#print 'MEATS: ', meat, ", ", meatInDescriptor
			if meat not in cuisineMeats and meatInDescriptor not in cuisineMeats:
				# Replace with meat in cuisineMeats
				if meat in (poultryAndGame + seafood) or meatInDescriptor in (poultryAndGame + seafood):
					# chicken
					ing.name = "chicken"
					ing.descriptor = "boneless"
				else:
					# lamb/mutton
					ing.name = "pork"	
				print ing.unicode()
		#replace cheese with indian cheese
		if category in cheeseCategory:
			pat = re.search("cheese*",ing.name.lower())
			pat2 = re.search("cheese*",ing.descriptor.lower())
			if pat or pat2:
				print ing.unicode()
				cheese = ing.name
				cheeseInDescriptor = findInDescriptor(ing.descriptor,cuisineCheese) 
				#print 'CHEESE: ', cheese, ", ", cheeseInDescriptor
				if cheese not in cuisineCheese and cheeseInDescriptor not in cuisineCheese:
					#replace cheese with indian cheese
					ing.name = "oaxaca cheese"
					ing.descriptor = ""
					print ing.unicode()
'''


def findInDescriptor(descriptor, cuisineList):
	words = descriptor.split(' ')
	x = ''
	# print words
	for word in words:
		if word in cuisineList:
			x = word
			break
	return x
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
	#recipe = getRecipe('http://allrecipes.com/Recipe/Flavorful-Beef-Stir-Fry-3/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stir%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i2')
	recipe = getRecipe('http://allrecipes.com/recipe/shepherds-pie-vi/')
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


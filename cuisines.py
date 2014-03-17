from lists import cuisines as cuisines
import lists, scraper, parsing,re,objects
# Lists
from lists import poultryAndGame as poultryAndGame,\
livestock as livestock, \
stocks as stocks, \
seafood as seafood


meatsCategories = ['0500', '0700', '1000','1300','1700']
cheeseCategory = ['0100']
spiceHerbsCategory = ['0200']
sauce= ['0600']
veggiesGarnish = ['1100']

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
	cuisineSpiceHerb = cuisines['indian']['spicesAndHerbs']
	cuisineSauces = cuisines['indian']['sauces']
	cuisineVegGarn = cuisines['indian']['veggiesAndGarnish']
	removeIngredients=[]
	addSpices = False
	vegIndex = 0
	for ing in ingredients:
		# category
		category = ing.category
		#check the meats used in recipe
		if category in meatsCategories:
			#print ing.unicode()
			# name
			meat = ing.name
			meatInDescriptor = findInDescriptor(ing.descriptor, cuisineMeats)
			#print 'MEATS: ', meat, ", ", meatInDescriptor
			if meat not in cuisineMeats and meatInDescriptor not in cuisineMeats:
				# Replace with meat in cuisineMeats
				if meat in (poultryAndGame + seafood) or meatInDescriptor in (poultryAndGame + seafood):
					# chicken
					removeIngredients.append({ing.name+"$"+ing.descriptor:"chicken"})
					ing.name = "chicken"
					ing.descriptor = "boneless"
				else:
					# lamb/mutton
					removeIngredients.append({ing.name+"$"+ing.descriptor:"mutton"})
					ing.name = "mutton"	
				#print ing.unicode()
		#replace cheese with indian cheese
		if category in cheeseCategory:
			pat = re.search("cheese*",ing.name.lower())
			pat2 = re.search("cheese*",ing.descriptor.lower())
			if pat or pat2:
				#print ing.unicode()
				cheese = ing.name
				cheeseInDescriptor = findInDescriptor(ing.descriptor,cuisineCheese) 
				#print 'CHEESE: ', cheese, ", ", cheeseInDescriptor
				if cheese not in cuisineCheese and cheeseInDescriptor not in cuisineCheese:
					#replace cheese with indian cheese
					removeIngredients.append({ing.name+"$"+ing.descriptor:"cottage cheese (paneer)"})
					ing.name = "cottage cheese (paneer)"
					ing.descriptor = ""
					#print ing.unicode()
		if category in spiceHerbsCategory:
			#print ing.unicode()
			spiceHerb = ing.name
			spiceInDescriptor = findInDescriptor(ing.descriptor,cuisineSpiceHerb)
			if spiceHerb not in cuisineSpiceHerb and spiceInDescriptor not in cuisineSpiceHerb:
				if not addSpices:
					addSpices = True
					removeIngredients.append({ing.name+"$"+ing.descriptor: "turmeric, cumin, garam masala"})
					turmeric = parsing.findIngredient('turmeric')
					cumin = parsing.findIngredient('cumin')
					garam_masala = objects.Ingredient(name='garam masala')
					ing.name = ""
					#print ing.name
					#ingredients.remove(ing)
					ingredients+=[turmeric,cumin,garam_masala]
				else:
					ing.name = ""
					removeIngredients.append({ing.name+"$"+ing.descriptor: ""})
		#replace bread with naan if not pastry (i.e. cake, pie)... this is tough....
		#replace sauces....
		if category in sauce or ing.name in stocks:
			soupSauces = ing.name
			sauceInDescriptor = findInDescriptor(ing.descriptor,cuisineSauces)
			#print 'Sauces:',soupSauces, "Descriptor:", sauceInDescriptor
			if soupSauces not in cuisineSauces and sauceInDescriptor not in cuisineSauces:
				removeIngredients.append({ing.name+"$"+ing.descriptor:"curry sauce"})
				ing.name= "curry sauce"
				ing.descriptor = "tomato puree based"

		if category in veggiesGarnish:
			veggieGarName = ing.name
			veggieDescriptor = ing.descriptor
			#veggieDescriptor = findInDescriptor(ing.descriptor,cuisineVegGarn)
			isVeggie = findVeggies(veggieGarName,veggieDescriptor,"indian")
			#print "BEFORE:",ing.unicode()
			if not isVeggie:
				if vegIndex < len(cuisineVegGarn):
					removeIngredients.append({ing.name+"$"+ing.descriptor:cuisineVegGarn[vegIndex]})
					ing.name = cuisineVegGarn[vegIndex]
					vegIndex+=1
					#print "AFTER:",ing.unicode()
				else:
					ing.name = ""
					removeIngredients.append({ing.name+"$"+ing.descriptor:""})

			#if soupSauces not in cuisineSauces and sauceInDescriptor not in cuisineSauces:
	#recipe.ingredients = removeIngredient(ingredients)
	recipe.ingredients = sanitizeIngredients(ingredients)
	recipe.steps = replaceDirections(removeIngredients,recipe.steps)
	recipe.name = "Indian Version of -"+recipe.name
	print recipe.unicode()

def removeIngredient(ingredients):
	finalIng = []
	for ing in ingredients:
		if ing.name:
			finalIng.append(ing)
	return finalIng

def replaceDirections(ingredients,steps):
	for ing in ingredients:
		for key,value in ing.iteritems():
			for step in steps:
				splitKey = key.split('$')
				name = splitKey[0]
				descriptor = splitKey[1]
				if re.search("(?i)(%s|%s)" % (name, descriptor+name), step.direction):
					step.direction = re.sub("(?i)(%s|%s)" % (name, descriptor+name), value, step.direction)
	return steps

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

def findVeggies(name,descriptor,cuisine):
	for veggie in cuisines[cuisine]['veggiesAndGarnish']:
		pat = re.search("%s.*" % veggie,name)
		pat2 = re.search("%s.*" % veggie,descriptor)
		if pat:
			return True
		elif pat2:
			return True

def findInDescriptor(descriptor, cuisineList):
	words = descriptor.split(' ')
	x = ''
	# print words
	for word in words:
		if word in cuisineList:
			x = word
			break
	return x

def sanitizeIngredients(ingredientsList):
	uniqueIng = []
	finalIng = []
	for ing in ingredientsList:
		if not ing.name in uniqueIng and ing.name:
			uniqueIng.append(ing.name)
			finalIng.append(ing)
	return finalIng

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
	recipe = getRecipe('http://allrecipes.com/Recipe/Italian-Sausage-Soup-with-Tortellini/Detail.aspx?event8=1&prop24=SR_Title&e11=soups&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i3')
	#print recipe.unicode()
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


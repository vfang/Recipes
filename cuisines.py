from lists import cuisines as cuisines
import lists, scraper, parsing,re,objects
# Lists
from lists import poultryAndGame as poultryAndGame,\
livestock as livestock, \
stocks as stocks, \
seafood as seafood,\
meats as meats

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
	cuisine = "indian"
	ingredients = recipe.ingredients
	cuisineMeats = cuisines[cuisine]["meats"]
	cuisineCheese = cuisines[cuisine]['cheese']
	cuisineSpiceHerb = cuisines[cuisine]['spicesAndHerbs']
	cuisineSauces = cuisines[cuisine]['sauces']
	cuisineVegGarn = cuisines[cuisine]['veggiesAndGarnish']

	modifiedIngredients=[]
	addSpices = False
	vegIndex = 0
	for ing in ingredients:
		category = ing.category
		#check the meats used in recipe
		if category in meatsCategories or ing.name in meats:

			if fitsCuisineForCategory(ing,cuisineMeats):
				(meat,meatInDescriptor) = findIngNames(ing,cuisineMeats)
				if meat in (poultryAndGame + seafood) or meatInDescriptor in (poultryAndGame + seafood):
					# chicken
					modifiedIngredients.append(updateIngredient(ing,cuisineMeats[0],"boneless",""))
				else:
					# lamb/mutton
					modifiedIngredients.append(updateIngredient(ing, cuisineMeats[1], "", ""))

		#replace cheese with indian cheese
		elif category in cheeseCategory:
			pat = re.search("cheese*",ing.name.lower())
			pat2 = re.search("cheese*",ing.descriptor.lower())
			if pat or pat2:
				if fitsCuisineForCategory(ing,cuisineCheese):
					(cheese,cheeseInDescriptor) = findIngNames(ing,cuisineCheese)
					modifiedIngredients.append(updateIngredient(ing,cuisineCheese[0],"",""))

		#replace spices and herbs
		elif category in spiceHerbsCategory:
			if fitsCuisineForCategory(ing,cuisineSpiceHerb):
				if not addSpices:
					addSpices= True
					modifiedIngredients.append({ing.name+"$"+ing.descriptor:', '.join(cuisineSpiceHerb[0:3])})
					modifiedIngredients.append(updateIngredient(ing,"","",""))
				else:
					modifiedIngredients.append(updateIngredient(ing, "", "", ""))
		
		#replace sauces....
		elif category in sauce or ing.name in stocks:
			if fitsCuisineForCategory(ing,cuisineSauces):
				modifiedIngredients.append(updateIngredient(ing,cuisineSauces[0],"tomato puree based",""))

		elif category in veggiesGarnish:
			veggieGarName = ing.name
			veggieDescriptor = ing.descriptor
			isVeggie = findVeggies(veggieGarName,veggieDescriptor,cuisine)
			if not isVeggie:
				if vegIndex < len(cuisineVegGarn):
					modifiedIngredients.append(updateIngredient(ing,cuisineVegGarn[vegIndex],"",""))
					vegIndex+=1
				else:
					modifiedIngredients.append(updateIngredient(ing,"","",""))
	if addSpices:
		for spiceHerb in cuisineSpiceHerb[0:3]:
			newIng=parsing.findIngredient(spiceHerb)
			if not newIng.name:
				newIng = objects.Ingredient(name=spiceHerb)
			ingredients.append(newIng)

	recipe.ingredients = sanitizeIngredients(ingredients)
	recipe.steps = replaceDirections(modifiedIngredients,recipe.steps)
	recipe.name = "Indian Version of -"+recipe.name
	print recipe.unicode()

def changeToMexican(recipe):
	cuisine = "mexican"
	ingredients = recipe.ingredients
	cuisineMeats = cuisines[cuisine]["meats"]
	cuisineCheese = cuisines[cuisine]['cheese']
	cuisineSpiceHerb = cuisines[cuisine]['spicesAndHerbs']
	cuisineSauces = cuisines[cuisine]['sauces']
	cuisineVegGarn = cuisines[cuisine]['veggiesAndGarnish']

	modifiedIngredients=[]
	addSpices = False
	vegIndex = 0
	for ing in ingredients:
		category = ing.category
		#check the meats used in recipe
		if category in meatsCategories or ing.name in meats:

			if fitsCuisineForCategory(ing,cuisineMeats):
				(meat,meatInDescriptor) = findIngNames(ing,cuisineMeats)
				if meat in (poultryAndGame + seafood) or meatInDescriptor in (poultryAndGame + seafood):
					modifiedIngredients.append(updateIngredient(ing,cuisineMeats[0],"boneless",""))
				else:
					modifiedIngredients.append(updateIngredient(ing, cuisineMeats[1], "barbacoa", ""))

		elif category in cheeseCategory:
			pat = re.search("cheese*",ing.name.lower())
			pat2 = re.search("cheese*",ing.descriptor.lower())
			if pat or pat2:
				if fitsCuisineForCategory(ing,cuisineCheese):
					(cheese,cheeseInDescriptor) = findIngNames(ing,cuisineCheese)
					modifiedIngredients.append(updateIngredient(ing,cuisineCheese[0],"",""))

		elif category in spiceHerbsCategory:
			if fitsCuisineForCategory(ing,cuisineSpiceHerb):
				if not addSpices:
					addSpices= True
					modifiedIngredients.append({ing.name+"$"+ing.descriptor:', '.join(cuisineSpiceHerb)})
					modifiedIngredients.append(updateIngredient(ing,"","",""))
				else:
					modifiedIngredients.append(updateIngredient(ing, "", "", ""))
		
		#replace sauces....
		elif category in sauce:
			if fitsCuisineForCategory(ing,cuisineSauces):
				modifiedIngredients.append(updateIngredient(ing,cuisineSauces[0],"",""))

		elif category in veggiesGarnish:
			veggieGarName = ing.name
			veggieDescriptor = ing.descriptor
			isVeggie = findVeggies(veggieGarName,veggieDescriptor,cuisine)
			if not isVeggie:
				if vegIndex < len(cuisineVegGarn):
					modifiedIngredients.append(updateIngredient(ing,cuisineVegGarn[vegIndex],"",""))
					vegIndex+=1
				else:
					modifiedIngredients.append(updateIngredient(ing,"","",""))
	if addSpices:
		for spiceHerb in cuisineSpiceHerb[0:3]:
			newIng=parsing.findIngredient(spiceHerb)
			if not newIng.name:
				newIng = objects.Ingredient(name=spiceHerb)
			ingredients.append(newIng)

	recipe.ingredients = sanitizeIngredients(ingredients)
	recipe.steps = replaceDirections(modifiedIngredients,recipe.steps)
	recipe.name = "Mexican Version of - "+recipe.name
	print recipe.unicode()

##### CHINESE ######
def changeToChinese(recipe):
	cuisine = "chinese"
	ingredients = recipe.ingredients
	cuisineMeats = cuisines[cuisine]["meats"]
	cuisineSpiceHerb = cuisines[cuisine]['spicesAndHerbs']
	cuisineSauces = cuisines[cuisine]['sauces']
	cuisineVegGarn = cuisines[cuisine]['veggiesAndGarnish']
	cuisineAlcohol = cuisines[cuisine]['alcohol']

	modifiedIngredients=[]
	addSpices = False
	vegIndex = 0
	for ing in ingredients:
		category = ing.category
		if category in meatsCategories or ing.name in meats:
			if fitsCuisineForCategory(ing, cuisineMeats):
				(meat, meatInDescriptor) = findIngNames(ing, cuisineMeats)
				if meat in (poultryAndGame + seafood) or meatInDescriptor in (poultryAndGame + seafood):
					modifiedIngredients.append(updateIngredient(ing, cuisineMeats[0], "boneless", ""))
				else:
					modifiedIngredients.append(updateIngredient(ing, cuisineMeats[1], "tenderloin", "cubed"))

		elif category in spiceHerbsCategory:
			if fitsCuisineForCategory(ing, cuisineSpiceHerb):
				if not addSpices:
					addSpices = True
					modifiedIngredients.append({ing.name+"$"+ing.descriptor: ', '.join(cuisineSpiceHerb)})
					modifiedIngredients.append(updateIngredient(ing, "", "", ""))
					
					# Add in garlic, chili pepper, basil combo at end
				else:
					modifiedIngredients.append(updateIngredient(ing, "", "", ""))

		elif category in sauce:
			if fitsCuisineForCategory(ing, cuisineSauces):
				modifiedIngredients.append(updateIngredient(ing, cuisineSauces[0], "", ""))

		elif category in veggiesGarnish:
			veggieGarName = ing.name
			veggieDescriptor = ing.descriptor
			isVeggie = findVeggies(veggieGarName,veggieDescriptor,cuisine)
			if not isVeggie:
				if vegIndex < len(cuisineVegGarn):
					modifiedIngredients.append(updateIngredient(ing, cuisineVegGarn[vegIndex], "", ""))
					vegIndex+=1
				else:
					modifiedIngredients.append(updateIngredient(ing, "", "", ""))

		elif ing.name == "wine":
			newIng = parsing.findIngredient(cuisineAlcohol[0])
			modifiedIngredients.append(updateIngredient(ing, newIng.name, newIng.descriptor, ""))

	if addSpices:
		for spiceHerb in cuisineSpiceHerb:
			newIng = parsing.findIngredient(spiceHerb)
			if not newIng.name:
				newIng = objects.Ingredient(name = spiceHerb)
			ingredients.append(newIng)

	recipe.ingredients = sanitizeIngredients(ingredients)
	recipe.steps = replaceDirections(modifiedIngredients,recipe.steps)
	recipe.name = "Chinese Version of -"+recipe.name
	print recipe.unicode()
	return recipe

##HELPER FUNCTIONS##
#goes through the directions and replaces old ingredients with new ingredients
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
#searches for veggies plural in name and descriptor
def findVeggies(name,descriptor,cuisine):
	for veggie in cuisines[cuisine]['veggiesAndGarnish']:
		pat = re.search("%s.*" % veggie,name)
		pat2 = re.search("%s.*" % veggie,descriptor)
		if pat:
			return True
		elif pat2:
			return True

#searches for name of ingredient in descriptor
def findInDescriptor(descriptor, cuisineList):
	words = descriptor.split(' ')
	x = ''
	# print words
	for word in words:
		if word in cuisineList:
			x = word
			break
	return x

#removes duplicate ingredients and any ingredients that need to be tossed out
def sanitizeIngredients(ingredientsList):
	uniqueIng = []
	finalIng = []
	for ing in ingredientsList:
		if not ing.name in uniqueIng and ing.name:
			uniqueIng.append(ing.name)
			finalIng.append(ing)
	return finalIng

#stores a modification of an old ingredient with the new ingredient
def updateIngredient(ingredient, name, descriptor, preparation):
	origName = ingredient.name
	origDesc = ingredient.descriptor
	ingredient.name = name
	ingredient.descriptor = descriptor
	ingredient.preparation = preparation

	return {origName + "$" + origDesc:name}

#gives name and name of ingredient from findInDescriptor
def findIngNames(ing, category):
	return (ing.name, findInDescriptor(ing.descriptor, category))

#decides if the ingredient found fits the cuisine or not
def fitsCuisineForCategory(ing, category):
	(name, nameInDescriptor) = findIngNames(ing, category)
	fits = False
	if name not in category and nameInDescriptor not in category:
		fits = True
	return fits

##### RECIPE INFO ######
def getRecipe(recipeURL):
	lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
	lists.updateNameDB()
	###
	recipeInfo = scraper.retrieveRecipe(recipeURL)
	recipe = parsing.buildRecipeObject(recipeInfo)

	return recipe

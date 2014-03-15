import parsing
import scraper
import lists
import re
import pprint
import copy

# Lists
from lists import poultryAndGame as poultryAndGame,\
livestock as livestock, \
stocks as stocks, \
meats as meats, \
seafood as seafood, \
prepared as prepared, \
vegSubstitutions as vegSubstitutions, \
healthySubstitutions as healthySubstitutions


# TODO: add seafoods for veggie transformer
# TODO: healthy transformer, qty, method, and meat substitutions

##############################
##### HEALTHY TRANSFORMER ####
##############################
def healthyTransformer(recipe):
	healthyRecipe = recipe

	for ingredient in healthyRecipe.ingredients:
		substitution = ""
		if ingredient.name in healthySubstitutions:
			baseIng = healthySubstitutions[ingredient.name]
			if ingredient.descriptor in baseIng:
				print baseIng[ingredient.descriptor]
				substitution = baseIng[ingredient.descriptor]
			else:
				if baseIng[""]:
					print baseIng[""]
					substitution = baseIng[""]
				else:
					print "Nothing to substitute"

		# PERFORM SUBSTITUTION
		if substitution:
			ingredient = performHealthySub(ingredient, substitution)

	return healthyRecipe


'''
Substitutions not in list:
QTY SUBSTITUTIONS
Reduce sugar (75%)	
two egg whties - one whole egg

METHODS
oven/pan-fry - deep fry (cut fat)
steam - boil (steaming removes fewer nutrients)

OTHER
white meat poultry - dark meat poultry 
beef - bison
ground beef - ground turkey
'''

def performHealthySub(ingredient, recipe, substitution):
	ingredients = healthySubIngredients(ingredient, recipe.ingredients, substitution)
	# steps = healthySubSteps(ingredient, ingredients["origIng"], recipe.directions)

	recipe.ingredients = ingredients["ingredients"]
	# recipe.directions = steps

	return recipe

def healthySubIngredients(ingredient, substitution):
	newIng = parsing.parseIngredient({"name":substitution, "amount": ""})
	newIng.amount = ingredient.amount
	newIng.unit = ingredient.unit
	return newIng


# ## What does this do?
# 	substitution = {"name": newIng.name, "descriptor": newIng.descriptor}
# 	origIng = copy.deepcopy(ingredient)
# 	ingIndex = ingList.index(ingredient)
# 	if substitution:
# 		for field in substitution:
# 			if substitution[field]:
# 				if field == "name":
# 					ingList[ingIndex].name = substitution[field]
# 					print "NAME"
# 				elif field == "descriptor":
# 					ingList[ingIndex].descriptor = substitution[field]
# 	else:
# 		# REMOVE INGREDIENT
# 		ingList.pop(ingIndex)


# 	return {"ingredients": ingList, "origIng": origIng}

##############################
##### VEGGIE TRANSFORMER #####
##############################
def veggieTransformer(recipe):
	ingredients = recipe.ingredients
	vegRecipe = recipe
	for ingredient in ingredients:
		substitution = ""
		name = ingredient.name
		# STOCKS
		if name in stocks:
			print 'STOCK'
			substitution = vegSubstitutions["stock"]
		# MEATS
		elif name in meats:
			# GROUND MEATS
			if re.search("(?i)ground", ingredient.descriptor):
				if ingredient.name in poultryAndGame:
					substitution = vegSubstitutions["ground poultry"]
				else:
					substitution = vegSubstitutions["ground livestock"]
			elif name in poultryAndGame or isStirFry(recipe) or isDeepFried(recipe):
				substitution = vegSubstitutions["poultry"]
			elif name in livestock:
				substitution = vegSubstitutions["livestock"]
			elif name in seafood or ingredient.descriptor in seafood:
				substitution = vegSubstitutions["seafood"]
			else:
				substitution = None

		# PERFORM SUBSTITUTION
		if substitution:	
			vegRecipe = performVegSub(ingredient, vegRecipe, substitution)


	return vegRecipe

##### SUBSTITUION METHODS ######
def performVegSub(ingredient, recipe, substitution):
	ingredients = vegSubIngredients(ingredient, recipe.ingredients, substitution)
	steps = vegSubSteps(ingredient, ingredients["origIng"], recipe.directions)

	recipe.ingredients = ingredients["ingredients"]
	recipe.directions = steps

	return recipe

def vegSubIngredients(ingredient, ingList, substitution):
	origIng = copy.deepcopy(ingredient)
	ingIndex = ingList.index(ingredient)
	if substitution:
		for field in substitution:
			if substitution[field]:
				if field == "name":
					ingList[ingIndex].name = substitution[field]
					print "NAME"
				elif field == "descriptor":
					ingList[ingIndex].descriptor = substitution[field]
				elif field == "preparation":
					ingList[ingIndex].preparation = substitution[field]
	else:
		# REMOVE INGREDIENT
		ingList.pop(ingIndex)


	return {"ingredients": ingList, "origIng": origIng}

def vegSubSteps(newIng, origIng, steps):
	newSteps = steps
	print "!!! Substituting ", origIng.name," ", origIng.descriptor, " with ", newIng.name, " ", newIng.descriptor 
	for i,step in enumerate(steps):
		newStep = step
		# STOCKS
		if origIng.name in stocks:
			if re.search("(?i)(bouillon|stock|broth)", step):
				splitWord = re.search("(?i)(bouillon|stock|broth)", step).group()
				descriptor = step.split(splitWord)[0].split(' ')[-2]
				sub = " ".join([newIng.descriptor, newIng.name])
				if descriptor in origIng.descriptor:
					newStep = re.sub("(?i)%s%s" % (origIng.descriptor, origIng.name), sub, step)
				else:
					newStep = re.sub("(?i)%s" % origIng.name, sub, newStep) 
		# MEATS
		if origIng.name in meats:
			if re.search("(?i)ground", origIng.descriptor):
				newStep = re.sub("(?i)ground %s" % origIng.name, newIng.name, step)
			elif re.search("(?i).*%s.*" % origIng.name, step):
				newStep = re.sub("(?i)%s" % origIng.name, newIng.name, newStep)
			else:
				meat = findMeatDescriptor(origIng.descriptor)
				newStep = re.sub("(?i)%s" % meat, newIng.name, newStep)


		newStep = sanitizeMeatDirections(newStep, newIng)

		# Replace udpated step
		newSteps[i] = newStep

	return newSteps

def findMeatDescriptor(descriptor):
	words = descriptor.split(' ')
	meat = ''
	print words
	for word in words:
		if word in meats:
			meat = word
			break
	return meat

def sanitizeMeatDirections(step, newIng):		# Get rid of meat related directions
	meatyWords = ["grease", "until", "fat", "meat"]
	sentences = step.split(".")
	meatlessStep = ""
	for sentence in sentences:
		for word in meatyWords:
			if word == "until":
				if re.search("(?i).*(%s|%s).*" % (newIng.name, 'meat'), sentence):
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
					if re.search("(?i).*%s.*[,;]" % word, sentence):
						sentence = re.sub("(?i).*%s.*[,;]" % word, "", sentence)
					else:
						sentence = re.sub("(?i).*%s.*" % word, "", sentence)
					sentence = re.sub('^[,:;] ', "", sentence)
					sentence = re.sub("^\s+", "", sentence).capitalize()
		if sentence:
			if meatlessStep:
				meatlessStep += "." + sentence
			else:
				meatlessStep += sentence

	return meatlessStep

##### HELPERS ######
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
		print i.name," ", i.descriptor, " - ", i.category


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
	recipe = getRecipe('http://allrecipes.com/recipe/shepherds-pie-vi/')
	# recipe = getRecipe('http://allrecipes.com/recipe/chicken-stir-fry-3/')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Flavorful-Beef-Stir-Fry-3/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stir%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i2')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Crispy-Deep-Fried-Bacon/Detail.aspx?event8=1&prop24=SR_Thumb&e11=deep%20fry&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i17')
	# recipe = getRecipe('http://allrecipes.com/Recipe/Beef-Stew-V/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stew&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i5')
	# seafood
	# recipe = getRecipe('http://allrecipes.com/recipe/seafood-gumbo/')
	# print recipe.unicode()

	# recipe = getRecipe('http://allrecipes.com/Recipe/Mayonnaise-Cookies/Detail.aspx?event8=1&prop24=SR_Thumb&e11=mayonnaise&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i6')
	# a = parsing.parseIngredient({"name": "melted butter", "amount": "1 cup"})
	# print a.unicode()
	a = veggieTransformer(recipe)
	# a = healthyTransformer(recipe)
	printRecipe(a.name, a.ingredients, a.directions)


main()
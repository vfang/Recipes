import scraper
import objects
import lists
import string
import pprint
import sys
import re

def buildRecipeObject(recipeInfo):	#recipeInfo is a dictionary
	recipe = objects.Recipe(name=recipeInfo['title'],
		author= recipeInfo['author'], 
		cookTime=recipeInfo['time'], 
		servings=recipeInfo['servings'], 
		rating=recipeInfo['rating'])
	# recipe.ingredients = parseIngredients(recipeInfo['ingredients'])
	recipe.directions = recipeInfo['directions']
	toolsAndMethods = parseDirections(recipeInfo['directions'],recipe.ingredients)	
	recipe.tools= toolsAndMethods['tools']
	recipe.methods = toolsAndMethods['methods']
	return recipe

def parseIngredients(ingredients):
	newIngredients = []
	for ingredient in ingredients:
		ing = objects.Ingredient()
		# First find qty
		amnt = ingredient["amount"].split(" ")
		if amnt:
			unit = amnt[-1]
			if unit in lists.units:
				ing.unit = unit
				amnt.pop()
				ing.amount = " ".join(amnt)
			else:
				ing.amount = amnt[0]
		newIngredients.append(ing)
		print ing.unicode()
	# print newIngredients



def parseDirections(directions,ingredients):
	exclude = set(string.punctuation)
	ingredientsList = []
	for ing in ingredients:
		ingredientsList.append(ing.origName)
	words = []
	parsed = {"tools":[],"methods":[]}
	for sentence in directions:
		sentence = ''.join(ch for ch in sentence if ch not in exclude)
		w = sentence.split()
		for word in w:
			word = word.lower()
			if word not in words: #and word not in ignoreWords:
				words.append(word)

	for word in words:
		nextWordIndex = words.index(word)+1
		double_word =''

		try:
			double_word = word+' '+words[nextWordIndex]
		except:
			double_word = word
		try:
			lastTool = parsed['tools'][-1]
		except:
			lastTool = ''

		if word not in lastTool:
			if double_word in lists.tools:
				parsed['tools'].append(double_word)
			elif word in lists.tools:
				if double_word not in ingredientsList:
					parsed['tools'].append(word)

		if double_word in lists.methods:
			parsed['methods'].append(double_word)

		elif word in lists.methods:
			if double_word not in ingredientsList:
				parsed['methods'].append(word)

	return parsed


def main(recipeURL):
	#temporary
	# lists.ingredientDB = readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
	# lists.updateNameDB()
	###
	recipeInfo = scraper.retrieveRecipe(recipeURL)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(recipeInfo)
	ings = parseIngredients(recipeInfo["ingredients"])

	# recipe = buildRecipeObject(recipeInfo)
	# print recipe.unicode()

main(sys.argv[1])
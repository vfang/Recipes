import scraper
import objects
import lists
import string

#list of predefined things


#define ingredient categories
#~0100~^~Dairy and Egg Products~
#~0200~^~Spices and Herbs~
#~0300~^~Baby Foods~
#~0400~^~Fats and Oils~
#~0500~^~Poultry Products~
#~0600~^~Soups, Sauces, and Gravies~
#~0700~^~Sausages and Luncheon Meats~
#~0800~^~Breakfast Cereals~
#~0900~^~Fruits and Fruit Juices~
#~1000~^~Pork Products~
#~1100~^~Vegetables and Vegetable Products~
#~1200~^~Nut and Seed Products~
#~1300~^~Beef Products~
#~1400~^~Beverages~
#~1500~^~Finfish and Shellfish Products~
#~1600~^~Legumes and Legume Products~
#~1700~^~Lamb, Veal, and Game Products~
#~1800~^~Baked Products~
#~1900~^~Sweets~
#~2000~^~Cereal Grains and Pasta~
#~2100~^~Fast Foods~
#~2200~^~Meals, Entrees, and Side Dishes~
#~2500~^~Snacks~
#~3500~^~American Indian/Alaska Native Foods~
#~3600~^~Restaurant Foods~

def buildRecipeObject(recipeInfo):#recipeInfo is a dictionary
	recipe = objects.Recipe(name=recipeInfo['title'],
		author= recipeInfo['author'], 
		cooktime=recipeInfo['time'], 
		servings=recipeInfo['servings'], 
		rating=recipeInfo['rating'])

	directions = parseDirections(recipeInfo['directions'])
	recipe.ingredients = parseIngredients(recipeInfo['ingredients'])
	recipe.directions = recipeInfo['directions']
	recipe.tools= directions['tools']
	recipe.methods = directions['methods']
	recipe.ingredients= ingredients
	return recipe

def parseIngredient(ingr):#Maps a string to the corresponding ingredient in the ingredient database
	ing = objects.ingredient()
	items = ingr.split()
	matches = []
	matchScore = 0.0

	for DBing in lists.ingredientDB:
		match = True

		for word in items:
			if word not in DBing.descriptor:
				match = False
				break
			else:
				des = DBing.descriptor.split(',')
				for d in des:
					if word in d:
						matchScore += 1.0 / (des.index(d) + .001)

		if match:
			ing.name = DBing.name
			ing.descriptor = DBing.descriptor
			break

	return ing

def parseIngredients(ingredients):
	ings = []
	for ing in ingredients:
		ing.append(parseIngredient(ing))

	return ings

def parseDirections(directions):#return a dictionary with directions, tools, and methods
	ingredientsList = ['brown sugar','barbecue sauce']
	exclude = set(string.punctuation)
	words = []
	parsed = {"tools":[],"methods":[]}
	ignoreWords = ['a','the','in','at','and','or','on','to']
	for sentence in directions:
		sentence = ''.join(ch for ch in sentence if ch not in exclude)
		w = sentence.split()
		for word in w:
			word = word.lower()
			if word not in words and word not in ignoreWords:
				words.append(word)
	for word in words:
		nextWordIndex = words.index(word)+1
		try:
			potentialIng = word+' '+words[nextWordIndex]
		except:
			potentialIng = word
		if word in lists.tools:
			if potentialIng not in ingredientsList:
				parsed['tools'].append(word)
			
		if word in lists.methods:
			if potentialIng not in ingredientsList:
				parsed['methods'].append(word)
	print words
	print parsed['tools']
	print parsed['methods']

def main(recipeURL):
	recipeInfo = retrieveRecipe(recipeURL)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(recipeInfo)
	return
	recipe = buildRecipeObject(recipeInfo)
	print recipe.unicode

def tokenizeLine(string):
	
	line = string.split('^')
	numArgs = len(line)
	out = []

	for item in line:

		if item == '':

			out.append(item)

		else:

			if item[0] != '~':

				out.append(item)

			else:

				text = item.split('~')
				empty = False
				appended = False

				for word in text:

					if len(text) == 3 and text[1] == word and word != '':

						out.append(word)
						appended = True

					if empty and word == '' and not appended:

						out.append(word)
						empty = False
						appended = True

					else:

						if word == '':

							empty = True

	return out

def readIngredientFromLine(line):

	#fields = 0

	#if objectType == 'FOOD':
		
	#	isFood = True
	#	fields = 14

	#elif objectType == 'NUTIRENT':

	#	isNutrient = True
	#	fields = 6

	#else:

	#	print('objectType not recognized.')
	#	return None

	tokens = tokenizeLine(line)

	

	output = objects.ingredient()

	#	output.id = tokens[0]
	output.category = tokens[1]
	output.descriptor = tokens[2]
	output.name = tokens[3]
	#output.ComName = tokens[4]
	#	output.manufacName = tokens[5]
	#	output.survey = tokens[6]
	#	output.refDesc = tokens[7]
	#	output.refuse = tokens[8]
	#	output.sciName = tokens[9]
	#	output.nFactor = tokens[10]
	#	output.proFactor = tokens[11]
	#	output.fatFactor = tokens[12]
	#	output.carbFactor = tokens[13]

	return output

def readIngredientsFromFile(fileName):

	ingredientList = []

	with open(fileName, 'r') as f:

		while(True):

			line = f.readline()

			if not line:

				break

			ingredientList.append(readIngredientFromLine(line))

	return ingredientList

#main(sys.argv[1])
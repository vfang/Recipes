from scraper import retrieveRecipe
from objects import *
import pprint
import sys
import re

#list of predefined things
methods =[]
cuisines =[]
tools =["Apple corer", "Basting", 
"Biscuit cutter", "Biscuit press", "Blow torch", 
"Boil over preventer", "Bottle opener", "Bowl", 
"Bread knife", "Browning tray", "Butter curler", 
"Cake and pie server", "Cheese knife", "Cheesecloth", 
"Chef's knife", "Cherry pitter", "Chinoise", "Colander", 
"Corkscrew", "Crab cracker", "Cutting board", "Dough scraper", 
"Egg piercer", "Egg poacher", "Separating eggs", "Egg slicer", 
"Egg timer", "Fillet knife", "Urokotori", "Fish slice", 
"Flour sifter", "Food mill", "Funnel", "Garlic press", "Grapefruit knife", 
"Grater", "Gravy strainer", "Herb chopper", 
"Ladle", "Lame", "Lemon reamer", "Lemon squeezer", 
"Lobster pick", "Mandoline", "Mated colander pot", "Measuring jug", 
"Measuring spoon", "Meat grinder", "Meat tenderiser", "Meat thermometer", 
"Melon baller", "Mezzaluna", "Mortar and pestle", "Nutcracker", "Nutmeg grater", 
"Oven glove", "Pastry bag", "Pastry blender", "Pastry brush", "Pastry wheel", "Peel", 
"Peeler", "Pepper mill", "Pie bird", "Pizza cutter", "Potato masher", "Potato ricer",
"Pot-holder", "Poultry shears", "Potato ricer", "Roller docker", "Rolling pin",
"Salt shaker", "Weighing scale", "Scissors", "Scoop",
"Shellfish scraper", "Sieve", "Slotted spoon", "Spatula", "Spider",
"Sugar thermometer", "Tamis", "Tin opener", "Tomato knife", "Tongs", "Trussing needle",
"Whisk", "Wooden spoon", "Zester","pan","pot","knife","oven","microwave",
"wok","strainer","skillet","spoon","fork"]

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
	recipe = Recipe(name=recipeInfo['title'],author= recipeInfo['author'], cooktime=recipeInfo['time'], servings=recipeInfo['servings'], rating=recipeInfo['rating'])
	directions = parseDirections(recipeInfo['directions'])
	ingredients = parseIngredients(recipeInfo['ingredients'])
	recipe.directions = recipeInfo['directions']
	recipe.tools= directions.tools
	recipe.methods = directions.methods
	recipe.ingredients= ingredients
	return recipe

def parseIngredients(ingredients):#return ingredient object for each ingredient and find a descriptor and preparation
	pass
def parseDirections(directions):#return a dictionary with directions, tools, and methods
	pass
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

	

	output = ingredient()

	#	output.id = tokens[0]
	output.category = tokens[1]
	output.descriptor = tokens[2]
	#	output.shortDesc = tokens[3]
	output.name = tokens[4]
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

	with open(fileName, 'r', encoding="utf8") as f:

		while(True):

			line = f.readline()

			if not line:

				break

			ingredientList.append(readIngredientFromLine(line))

	return ingredientList

main(sys.argv[1])
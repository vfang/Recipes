from scraper import retrieveRecipe
from objects import *
import pprint
import sys
import re

#list of predefined things
tools =['pan','']
ingredient_category = []
methods =[]
cuisines =[]
ingredients_descriptor = []



def buildRecipeObject(recipeInfo):#recipeInfo is a dictionary
	recipe = Recipe(name=recipeInfo['title'],author= recipeInfo['author'], cooktime=recipeInfo['time'], servings=recipeInfo['servings'], rating=recipeInfo['rating'])
	directions = parseDirections(recipeInfo['directions'])
	ingredients = parseIngredients(recipeInfo['ingredients'])
	recipe.directions = directions.directions
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
	recipe = buildRecipeObject(recipeInfo)
	print recipe.unicode


main(sys.argv[1])
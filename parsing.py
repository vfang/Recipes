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

#define ingredient categories
ingredient_category.append('0100')		#	Dairy and Egg Products
ingredient_category.append('0200')		#	Spices and Herbs
ingredient_category.append('0300')		#	Baby Foods
ingredient_category.append('0400')		#	Fats and Oils
ingredient_category.append('0500')		#	Poultry Products
ingredient_category.append('0600')		#	Soups, Sauces, and Gravies
ingredient_category.append('0700')		#	Sausages and Luncheon Meats
ingredient_category.append('0800')		#	Breakfast Cereals
ingredient_category.append('0900')		#	Fruits and Fruit Juices
ingredient_category.append('1000')		#	Pork Products
ingredient_category.append('1100')		#	Vegetables and Vegetable Products
ingredient_category.append('1200')		#	Nut and Seed Products
ingredient_category.append('1300')		#	Beef Products
ingredient_category.append('1400')		#	Beverages
ingredient_category.append('1500')		#	Finfish and Shellfish Products
ingredient_category.append('1600')		#	Legumes and Legume Products
ingredient_category.append('1700')		#	Lamb, Veal, and Game Products
ingredient_category.append('1800')		#	Baked Products
ingredient_category.append('1900')		#	Sweets
ingredient_category.append('2000')		#	Cereal Grains and Pasta
ingredient_category.append('2100')		#	Fast Foods
ingredient_category.append('2200')		#	Meals, Entrees, and Side Dishes
ingredient_category.append('2500')		#	Snacks
ingredient_category.append('3500')		#	American Indian/Alaska Native Foods
ingredient_category.append('3600')		#	Restaurant Foods

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
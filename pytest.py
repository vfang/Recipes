import parsing
import lists
import scraper

lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
lists.updateNameDB()
recipeURL = 'http://allrecipes.com/Recipe/Vegetarian-Korma/Detail.aspx?soid=recs_recipe_1'
recipeInfo = scraper.retrieveRecipe(recipeURL)

i = parsing.parseIngredients(recipeInfo['ingredients'])

for ing in i:
	print ing.unicode()
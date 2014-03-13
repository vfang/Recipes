import parsing
import lists
import scraper

lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
lists.updateNameDB()
recipeURL = 'http://allrecipes.com/Recipe/Chef-Johns-Pasta-Primavera/Detail.aspx?soid=carousel_0_rotd&prop24=rotd'
recipeInfo = scraper.retrieveRecipe(recipeURL)

i = parsing.parseIngredients(recipeInfo['ingredients'])

for ing in i:
	print ing.unicode()
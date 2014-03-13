import parsing
import lists
import scraper

lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
lists.updateNameDB()
recipeURL = 'http://allrecipes.com/Recipe/Beef-Stew-V/Detail.aspx?event8=1&prop24=SR_Thumb&e11=beef%20stew&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i5'
recipeInfo = scraper.retrieveRecipe(recipeURL)

i = parsing.parseIngredients(recipeInfo['ingredients'])

for ing in i:
	print ing.unicode()
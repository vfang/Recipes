import lists,scraper,parsing,objects,json, sys, pprint

def main(recipeURL):
	lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
	lists.updateNameDB()


	recipeInfo = scraper.retrieveRecipe(recipeURL)
	recipe = parsing.buildRecipeObject(recipeInfo)
	
	# INGEDIENTS
	ingredients = recipe.ingredients
	JSONIngredients = []
	for ing in ingredients:
		ing = {
				"name": ing.name,
				"quantity": ing.amount,
				"measurement": ing.unit,
				"descriptor": ing.descriptor,
				"preparation": ing.preparation 
			}
		JSONIngredients.append(json.dumps(ing))
	
	# COOKING METHODS
	methods = recipe.primaryMethods
	tools = recipe.tools

	recipeJSON = {
					"ingredients": JSONIngredients,
					"cooking method": methods,
					"cooking tools": tools,
				}

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(recipeJSON)
	
	return json.dumps(recipeJSON)

main(sys.argv[1])
def getMeats(ingredients):
	# Get me a list of the meats in the recipe (should we include seafood?)
	pass

def vegTransformer(recipe):
	meats = getMeats(recipe.ingredients)

	if len(meats):
		# Transform ingredient list

		# Transform directions, based on modifications to ingredients list
	else:
		# There are no meats in this recipe => already vegetarian
		print "No transformation performed, recipe contains no meat"

	return recipe

'''
Notes for Vegetarian substitutions:
- Tofu 
	* good for pork, chicken, beef (use extra-firm tofu)
	* typically used to replace meat-heavy dishes (stir-fry, salad, fajitas)
	* still need to season tofu, but maybe not as much as the meat
	* probably need to reduce cooking time
- Beans
	* Can use to substitute for ground meat in things like chili, etc
	* Use sturdier beans (black, pinto, red kidney - canned beans)
- Remove all meat
	* For recipes that already contain proprotionally very little meat, and/or lots of other proteins
	* Remove all if meat is not the main ingredient
- Mushroom
	* Portobello to replace large pieces/slabs of meat (burger patty, steak, sandwich meat, etc)
- Eggplant
	* Similar to mushroom, but perhaps for chicken and turkey? (chicken parmigiana)
'''
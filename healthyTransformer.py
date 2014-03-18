import lists, re, copy

# Lists
from lists import poultryAndGame as poultryAndGame,\
livestock as livestock, \
stocks as stocks, \
meats as meats, \
seafood as seafood, \
prepared as prepared, \
vegSubstitutions as vegSubstitutions, \
healthySubstitutions as healthySubstitutions,\
legumes as legumes

##############################
##### HEALTHY TRANSFORMER ####
##############################
def healthyTransformer(recipe):
	healthyRecipe = recipe

	for ingredient in healthyRecipe.ingredients:
		substitution = ""
		if ingredient.name in healthySubstitutions:
			baseIng = healthySubstitutions[ingredient.name]
			if ingredient.descriptor in baseIng:
				print baseIng[ingredient.descriptor]
				substitution = baseIng[ingredient.descriptor]
			else:
				if baseIng[""]:
					print baseIng[""]
					substitution = baseIng[""]
				else:
					print "Nothing to substitute"

		# PERFORM SUBSTITUTION
		if substitution:
			newIng = performHealthySub(ingredient, substitution)
			ingredient = newIng

	return healthyRecipe


'''
Substitutions not in list:
QTY SUBSTITUTIONS
Reduce sugar (75%)	
two egg whties - one whole egg

METHODS
oven/pan-fry - deep fry (cut fat)
steam - boil (steaming removes fewer nutrients)

OTHER
white meat poultry - dark meat poultry 
beef - bison
ground beef - ground turkey
'''

def performHealthySub(ingredient, recipe, substitution):
	ingredients = healthySubIngredients(ingredient, recipe.ingredients, substitution)
	# steps = healthySubSteps(ingredient, ingredients["origIng"], recipe.directions)

	recipe.ingredients = ingredients["ingredients"]
	# recipe.directions = steps

	return recipe

def healthySubIngredients(ingredient, substitution):
	newIng = parsing.parseIngredient({"name":substitution, "amount": ""})
	newIng.amount = ingredient.amount
	newIng.unit = ingredient.unit
	return newIng


# ## What does this do?
# 	substitution = {"name": newIng.name, "descriptor": newIng.descriptor}
# 	origIng = copy.deepcopy(ingredient)
# 	ingIndex = ingList.index(ingredient)
# 	if substitution:
# 		for field in substitution:
# 			if substitution[field]:
# 				if field == "name":
# 					ingList[ingIndex].name = substitution[field]
# 					print "NAME"
# 				elif field == "descriptor":
# 					ingList[ingIndex].descriptor = substitution[field]
# 	else:
# 		# REMOVE INGREDIENT
# 		ingList.pop(ingIndex)


# 	return {"ingredients": ingList, "origIng": origIng}

def printRecipe(recipe, transformType):	
	recipe.name = "%s Version of - " % transformType + recipe.name
	print recipe.unicode()
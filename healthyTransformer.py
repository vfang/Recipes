import lists, re, copy,parsing

# Lists
from lists import healthySubstitutions as healthySubstitutions


##############################
##### HEALTHY TRANSFORMER ####
##############################
def healthyTransformer(recipe):
    healthyRecipe = recipe
    healthyRecipe.name = 'Healthy ' + healthyRecipe.name 
    subbedIngs = {}

    for ingredient in healthyRecipe.ingredients:
        substitution = ""
        if ingredient.name in healthySubstitutions:
            baseIng = healthySubstitutions[ingredient.name]
            if ingredient.descriptor in baseIng:
                substitution = baseIng[ingredient.descriptor]
                print 'Substituting ', ingredient.name, ' for ', substitution
            else:
                if baseIng[""]:
                    substitution = baseIng[""]
                    print 'Substituting ', ingredient.name, ' for ', substitution
                else:
                    print "Nothing to substitute"

        # PERFORM SUBSTITUTION
        print ingredient.carbs,ingredient.fat
        if substitution:
            newIng = healthySubIngredient(ingredient, substitution)
            ind = healthyRecipe.ingredients.index(ingredient)
            healthyRecipe.ingredients[ind] = newIng

        elif float(ingredient.fat) > 9.0 and 'low' not in ingredient.descriptor and 'fat' not in ingredient.descriptor and not ingredient.category == '0900' and not ingredient.category == '1100':
            newIng = healthySubIngredient(ingredient, fat = True)
            subbedIngs[ingredient.name] = newIng.name
            ind = healthyRecipe.ingredients.index(ingredient)
            healthyRecipe.ingredients[ind] = newIng
            print 'Substituting ', ingredient.name, ' for ', newIng.name

        elif float(ingredient.carbs) > 3.5 and 'low' not in ingredient.descriptor and 'carb' not in ingredient.descriptor and not ingredient.category == '0900' and not ingredient.category == '1100':
            newIng = healthySubIngredient(ingredient, carb = True)
            subbedIngs[ingredient.name] = newIng.name
            ind = healthyRecipe.ingredients.index(ingredient)
            healthyRecipe.ingredients[ind] = newIng
            print 'Substituting ', ingredient.name, ' for ', newIng.name

    dir = healthyRecipe.directions
    for step in dir:
        #step = str(step)
        newStep = step.split()

        for word in newStep:
            if word in healthySubstitutions:
                ind = newStep.index(word)
                newStep[ind] = healthySubstitutions[word]
                if not isinstance(newStep[ind], basestring):
                    newStep[ind] = newStep[ind][""]

            elif word in subbedIngs:
                ind = newStep.index(word)
                newStep[ind] = subbedIngs[word]

        newStep = ' '.join(newStep)
        ind = dir.index(step)
        dir[ind] = newStep

    healthyRecipe.directions = dir

    healthyRecipe.steps = parsing.makeSteps(healthyRecipe.directions, healthyRecipe.tools, healthyRecipe.primaryMethods, healthyRecipe.secondaryMethods)


    return healthyRecipe


def performHealthySub(ingredient, recipe, substitution):
	#ingredients = healthySubIngredients(ingredient, substitution)
	# steps = healthySubSteps(ingredient, ingredients["origIng"], recipe.directions)

	#recipe.ingredients = ingredients["ingredients"]
	# recipe.directions = steps

	return recipe

def healthySubIngredient(ingredient, substitution = '', carb = False, fat = False):
    if substitution:
        newIng = parsing.parseIngredient({"name":substitution, "amount": ""})
        
    elif carb:
        newIng = parsing.parseIngredient({"name": 'low carb ' + ingredient.descriptor + ' ' + ingredient.name + ', ' + ingredient.preparation, "amount": ""})

    elif fat:
        newIng = parsing.parseIngredient({"name": 'low fat ' + ingredient.descriptor + ' ' + ingredient.name + ', ' + ingredient.preparation, "amount": ""})

    newIng.unit = ingredient.unit
    newIng.amount = ingredient.amount
    return newIng



def printRecipe(recipe, transformType):	
	recipe.name = "%s Version of - " % transformType + recipe.name
	print recipe.unicode()
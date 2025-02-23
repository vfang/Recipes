import lists, re, copy,parsing

# Lists
from lists import healthySubstitutions as healthySubstitutions


##############################
##### HEALTHY TRANSFORMER ####
##############################
def healthyTransformer(recipe):
    healthyRecipe = recipe
    subbedIngs = {}

    for ingredient in healthyRecipe.ingredients:
        substitution = ""
        if ingredient.name in healthySubstitutions:
            baseIng = healthySubstitutions[ingredient.name]
            if ingredient.descriptor in baseIng:
                substitution = baseIng[ingredient.descriptor]
            else:
                if baseIng[""]:
                    substitution = baseIng[""]
                else:
                    print "Nothing to substitute"

        # PERFORM SUBSTITUTION
        if '.' not in ingredient.carbs:
            ingredient.carbs = '0.00'
        if '.' not in ingredient.fat:
            ingredient.fat = '0.00'
        try:
            if substitution:
                newIng = healthySubIngredient(ingredient, substitution)
                ind = healthyRecipe.ingredients.index(ingredient)
                healthyRecipe.ingredients[ind] = newIng
                print 'Substituting ', ingredient.name, ' for ', substitution

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
        except:
            try:
                float(ingredient.fat)
            except:
                print ingredient.fat, 'cannot be converted to a float'
            try:
                float(ingredient.carbs)
            except:
                print ingredient.carbs, 'cannot be converted to a float'

    dir = healthyRecipe.directions
    for step in dir:
        #step = str(step)
        newStep = step.split()

        for word in newStep:
            if word.endswith(','):
                word = word[:-1]
            if word in healthySubstitutions:
                try:
                    ind = newStep.index(word)
                except:
                    word = word + ','
                    ind = newStep.index(word)
                    word = word[:-1]

                newStep[ind] = healthySubstitutions[word]
                if not isinstance(newStep[ind], basestring):
                    newStep[ind] = newStep[ind][""]

            elif word in subbedIngs:
                
                try:
                    ind = newStep.index(word)
                    
                except:
                    word = word + ','
                    ind = newStep.index(word)
                    word = word[:-1]

                newStep[ind] = subbedIngs[word]

        newStep = ' '.join(newStep)
        ind = dir.index(step)
        dir[ind] = newStep

    healthyRecipe.directions = dir

    healthyRecipe.steps = parsing.makeSteps(healthyRecipe.directions, healthyRecipe.tools, healthyRecipe.primaryMethods, healthyRecipe.secondaryMethods)


    return healthyRecipe

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
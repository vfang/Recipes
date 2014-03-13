import scraper
import objects
import lists
import string
import pprint
import sys

#define ingredient categories
#~0100~^~Dairy and Egg Products~
#~0200~^~Spices and Herbs~
#~0300~^~Baby Foods~
#~0400~^~Fats and Oils~
#~0500~^~Poultry Products~                      Meat
#~0600~^~Soups, Sauces, and Gravies~
#~0700~^~Sausages and Luncheon Meats~           Meat
#~0800~^~Breakfast Cereals~
#~0900~^~Fruits and Fruit Juices~
#~1000~^~Pork Products~                         Meat
#~1100~^~Vegetables and Vegetable Products~
#~1200~^~Nut and Seed Products~
#~1300~^~Beef Products~                         Meat
#~1400~^~Beverages~
#~1500~^~Finfish and Shellfish Products~        Meat
#~1600~^~Legumes and Legume Products~
#~1700~^~Lamb, Veal, and Game Products~         Meat
#~1800~^~Baked Products~
#~1900~^~Sweets~
#~2000~^~Cereal Grains and Pasta~
#~2100~^~Fast Foods~
#~2200~^~Meals, Entrees, and Side Dishes~
#~2500~^~Snacks~
#~3500~^~American Indian/Alaska Native Foods~
#~3600~^~Restaurant Foods~

def buildRecipeObject(recipeInfo):	#recipeInfo is a dictionary
	recipe = objects.Recipe(name=recipeInfo['title'],
		author= recipeInfo['author'], 
		cookTime=recipeInfo['time'], 
		servings=recipeInfo['servings'], 
		rating=recipeInfo['rating'])
	recipe.ingredients = parseIngredients(recipeInfo['ingredients'])
	recipe.directions = recipeInfo['directions']
	toolsAndMethods = parseDirections(recipeInfo['directions'],recipe.ingredients)	
	recipe.tools= toolsAndMethods['tools']
	recipe.methods = toolsAndMethods['methods']
	#print recipe.tools, recipe.methods,recipe.directions,recipe.ingredients
	return recipe

def parseIngredient(dict):
    amount = dict['amount']
    name = dict['name']

    amount = amount.split()

    if len(amount) > 2:
        a = ''
        for x in range(1, len(amount)):
            a += ' ' + amount[x]
        unit = a
    else:
        try:
            unit = amount[1]
        except:
            unit = 'not specified'
    amount = amount[0]

    if amount > 1:
        if name.endswith('s'):
            name = name[:-1]

    ing = findIngredient(name)
    ing.amount = amount
    ing.unit = unit

    #name = name.split()
    #sName = []

    #for word in name:
    #    if word.endswith(','):
    #        word = word[:-1].lower()
     #       sName.append(word)
    #    else:
    #        sName.append(word)

    #for word in sName:
    #    if word == 'and':
    #        pass
    #    elif word.lower() not in ing.descriptor and word.endswith('ed'):
    #        ing.preparation += word + ' and '
    #    elif word.lower() not in ing.descriptor:
    #        ing.preparation += word + ' '

    #if ing.preparation.endswith(' and '):
    #   ing.preparation = ing.preparation[:-5]

    ing.updateString()

    return ing

def findIngredient(ingr):	#Maps a string to the corresponding ingredient in the ingredient database
    ingr = ingr.lower()
    items = ingr.split()

    descriptors = []
    preparations = []

    soupOrSauce = False
    spiceOrPowder = False
    babyFood = False
    dairyProduct = False
    rawFood = False
    meatProduct = False
    sweetProduct = False

    primeIng = ''

    for item in items:
        if item.endswith(','):
            primeIng = item
            break

    if primeIng == '':
        filter = []
        if 'for' in items:
            ind = items.index('for')
            for j in range(0, ind):
                filter.append(items[j])
        elif 'with' in items:
            ind = items.index('with')
            for j in range(0, ind):
                filter.append(items[j])
        else:
            filter = items

        primeIng = filter[len(filter) - 1]

    primeIndex = items.index(primeIng)

    for x in range(0, primeIndex):
        descriptors.append(items[x])

    p = items[(primeIndex + 1):]
    for item in p:
        preparations.append(item)

    if primeIng.endswith(','):
        primeIng = primeIng[:-1]

    if primeIng == 'ketchup':
        primeIng = 'catsup'

    if primeIng == 'zucchinis':
        primeIng = 'zucchini'

    primeIng = primeIng.lower()

    if primeIng == 'soup' or primeIng == 'sauce' or primeIng == 'paste':
        soupOrSauce = True

    if primeIng == 'spice' or primeIng == 'powder' or primeIng == 'salt':
        spiceOrPowder = True

    if 'baby' in items:
        babyFood = True

    if ('cheese' in primeIng 
        or 'milk' in primeIng 
        or 'cream' in primeIng 
        or 'yogurt' in primeIng 
        or 'whey' in primeIng 
        or 'egg' in primeIng 
        or 'butter' in primeIng):
        dairyProduct = True

    if 'fresh' in items or 'raw' in items:
        rawFood = True

    if ('meat' in items 
        or 'beef' in items 
        or 'pork' in items 
        or 'chicken' in items 
        or 'fish' in items):
        meatProduct = True

    if ('sugar' in items 
        or 'syrup' in items 
        or 'sweetener' in items 
        or 'pudding' in items 
        or 'candies' in items 
        or 'candy' in items 
        or 'honey' in items 
        or 'frosting' in items
        or 'topping' in items
        or 'pie filling' in items
        or 'pectin' in items
        or 'marmalade' in items
        or 'molasses' in items
        or 'jelly' in items
        or 'jam' in items
        or 'fruit butter' in items):
        sweetProduct = True

    matches = []

    for DBing in lists.ingredientDB:

        matchScore = 0.0

        match = False
        soup = False
        spice = False
        baby = False
        dairy = False
        raw = False
        meat = False
        sweet = False

        des = DBing.descriptor.split()
        nam = DBing.name.split(',')

        if DBing.category == '0600':
            soup = True

        if DBing.category == '0200':
            spice = True

        if DBing.category == '0300':
            baby = True

        if DBing.category == '0100':
            dairy = True

        if (DBing.category == '0500' 
            or DBing.category == '0700' 
            or DBing.category == '1000' 
            or DBing.category == '1300' 
            or DBing.category == '1500' 
            or DBing.category == '1700'):
            meat = True

        if DBing.category == '1900':
            sweet = True

        if 'RAW' in DBing.name:
            raw = True

        for word in nam:
            if primeIng not in word.lower():
                pass
            else:
                match = True
                if primeIng == word.lower():
                    matchScore += 100
                else:
                    matchScore += 50
                break

        for word in descriptors:

            if word == 'and':
                pass
            else:
                if word not in DBing.descriptor.lower():
                    pass
                else:

                    match = True


                    if word in lists.colors:
                        r = .1
                    
                    elif descriptors.index(word) == len(descriptors) - 1:
                        r = .8
                        
                    else:
                        r = 1 #float(len(des)) / float(len(sItems))

                    for d in des:
                        if word in d.lower():

                            if word == 'jalapeno':
                                pass

                            c = ''
                            if d.endswith(','):
                                c = d[:-1]
                            if word == c or word == d.lower():
                                matchScore += 2.0 / ((des.index(d) + 1.0) * r)
                            else:
                                matchScore += 1.0 / ((des.index(d) + 1.0) * r)
                            break

        if match:
            ing = objects.Ingredient()
            ing.name = DBing.name
            ing.origName = ingr # VF: I need this for transformer, remove after search is fixed
            ing.descriptor = DBing.descriptor
            
            if preparations != []:
                pass

            for word in preparations:
                ing.preparation += word + ' '
            
            ing.category = DBing.category
            ing.protein = DBing.protein

            if soup and not soupOrSauce:
                matchScore = matchScore / 3.0
            if spice and not spiceOrPowder:
                matchScore = matchScore / 2.0
            if baby and not babyFood:
                matchScore = matchScore / 2.0
            if dairy and not dairyProduct:
                matchScore = matchScore / 2.0
            if rawFood and not raw:
                matchScore = matchScore / 2.0
            if meat and not meatProduct:
                matchScore = matchScore / 2.0
            if sweetProduct and not sweet:
                matchScore = matchScore / 2.0

            tup = (ing, matchScore)
            matches.append(tup)

    result = objects.Ingredient()
    topIndex = 0
    topScore = 0
    for find in matches:
        if find[1] > topScore:
            result = find[0]
            topIndex = matches.index(find)
            topScore = find[1]

    return result

def parseIngredients(ingredients):
    ings = []
    for ing in ingredients:
        ings.append(parseIngredient(ing))
    return ings

def parseDirections(directions,ingredients):#return a dictionary with directions, tools, and methods
	exclude = set(string.punctuation)
	ingredientsList = []
	for ing in ingredients:
		ingredientsList.append(ing.name)
	#ingredientsList =['barbecue sauce']
	#print ingredientsList
	#cprint directions
	words = []
	parsed = {"tools":[],"methods":[]}
	#ignoreWords = ['a','the','in','at','and','or','on','to']
	for sentence in directions:
		sentence = ''.join(ch for ch in sentence if ch not in exclude)
		w = sentence.split()
		for word in w:
			word = word.lower()
			if word not in words: #and word not in ignoreWords:
				words.append(word)

	for word in words:
		nextWordIndex = words.index(word)+1
		double_word =''

		try:
			double_word = word+' '+words[nextWordIndex]
		except:
			double_word = word
		try:
			lastTool = parsed['tools'][-1]
		except:
			lastTool = ''

		if word not in lastTool:
			if double_word in lists.tools:
				parsed['tools'].append(double_word)
			elif word in lists.tools:
				if double_word not in ingredientsList:
					parsed['tools'].append(word)

		if double_word in lists.methods:
			parsed['methods'].append(double_word)

		elif word in lists.methods:
			if double_word not in ingredientsList:
				parsed['methods'].append(word)

	return parsed

def tokenizeLine(string):
	line = string.split('^')
	numArgs = len(line)
	out = []
	for item in line:
		if item == '':
			out.append(item)
		else:
			if item[0] != '~':
				out.append(item)
			else:
				text = item.split('~')
				empty = False
				appended = False
				for word in text:
					if len(text) == 3 and text[1] == word and word != '':
						out.append(word)
						appended = True
					if empty and word == '' and not appended:
						out.append(word)
						empty = False
						appended = True
					else:
						if word == '':
							empty = True
	return out

def readIngredientFromLine(line):
	#fields = 0
	#if objectType == 'FOOD':
	#	isFood = True
	#	fields = 14
	#elif objectType == 'NUTIRENT':
	#	isNutrient = True
	#	fields = 6
	#else:
	#	print('objectType not recognized.')
	#	return None
	tokens = tokenizeLine(line)
	output = objects.Ingredient()
	#	output.id = tokens[0]
	output.category = tokens[1]
	output.descriptor = tokens[2].lower()
	output.name = tokens[3]
	#output.ComName = tokens[4]
	#	output.manufacName = tokens[5]
	#	output.survey = tokens[6]
	#	output.refDesc = tokens[7]
	#	output.refuse = tokens[8]
	#	output.sciName = tokens[9]
	#	output.nFactor = tokens[10]
	output.protein = tokens[11]
	output.fat = tokens[12]
	output.carbs = tokens[13]
	return output

def readIngredientsFromFile(fileName):
	ingredientList = []
	with open(fileName, 'r') as f:
		while(True):
			line = f.readline()
			if not line:
				break
			ingredientList.append(readIngredientFromLine(line))
	return ingredientList

def main(recipeURL):
	#temporary
	lists.ingredientDB = readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
	lists.updateNameDB()
	###
	recipeInfo = scraper.retrieveRecipe(recipeURL)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(recipeInfo)
	recipe = buildRecipeObject(recipeInfo)
	print recipe.unicode()

# main(sys.argv[1])
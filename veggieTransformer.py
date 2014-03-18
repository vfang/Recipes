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
##### VEGGIE TRANSFORMER #####
##############################
def veggieTransformer(recipe):
	ingredients = recipe.ingredients
	vegRecipe = recipe
	numMeats = 0
	for ingredient in ingredients:
		substitution = ""
		name = ingredient.name
		descriptorMeat = findMeatDescriptor(ingredient.descriptor)
		# STOCKS

		if name in stocks:
			substitution = vegSubstitutions["stock"]
		# MEATS
		elif name in meats or descriptorMeat in meats:
			descriptorMeat = findMeatDescriptor(ingredient.descriptor)
			if re.search("(?i)ground", ingredient.descriptor):
				if ingredient.name in poultryAndGame:
					substitution = vegSubstitutions["ground poultry"]
				else:
					substitution = vegSubstitutions["ground livestock"]
			elif name in poultryAndGame or descriptorMeat in poultryAndGame or isStirFry(recipe) or isDeepFried(recipe):
				substitution = vegSubstitutions["poultry"]
			elif name in livestock or descriptorMeat in livestock or name in prepared:
				substitution = vegSubstitutions["livestock"]
			elif name in seafood or descriptorMeat in seafood:
				substitution = vegSubstitutions["seafood"]
			else:
				substitution = None
		# PERFORM SUBSTITUTION
		if substitution:	
			vegRecipe = performVegSub(ingredient, vegRecipe, substitution)
			numMeats += 1
	if not numMeats:
		unveggieTransformer(recipe)
	else:
		printRecipe(vegRecipe, "Vegetarian")

	return vegRecipe

def unveggieTransformer(recipe):
	# If recipe has legumes, replace with meat
	ingredients = recipe.ingredients
	steps = recipe.steps
	for ingredient in ingredients:
		name = ingredient.name
		fullName = ingredient.descriptor + ingredient.name
		if name in legumes or fullName in legumes:
			oldIng = copy.deepcopy(ingredient)
			ingredient.name = "chicken"
			ingredient.descriptor = "skinless, boneless"
			steps = meatifySteps(ingredient, oldIng, steps)
			break
	recipe.ingredients = ingredients
	recipe.steps = steps

	printRecipe(recipe, "Un-Veggie")

	return recipe
	
def meatifySteps(ingredient, oldIng, steps):
	name = oldIng.name
	fullName = oldIng.descriptor + oldIng.name
	for step in steps:
		direction = step.direction
		if "bean" not in fullName:
			if re.search("(?i)(%s|%s)" % (name, fullName) , direction):
				step.direction = re.sub("(?i)(%s|%s)" % (name, fullName), ingredient.name, direction)
		else:
			if re.search("(?i)(%s|%s)" % (name, fullName) , direction):
				step.direction = re.sub("(?i)%s" % fullName, ingredient.name, direction)

	return steps

##### SUBSTITUION METHODS ######
def performVegSub(ingredient, recipe, substitution):
	origIng = copy.deepcopy(ingredient)
	vegSubIngredients(ingredient, recipe.ingredients, substitution)
	steps = vegSubSteps(ingredient, origIng, recipe.steps)
	recipe.steps = steps

	return recipe

def vegSubIngredients(ingredient, ingList, substitution):
	if substitution:
		for field in substitution:
			if substitution[field]:
				if field == "name":
					ingredient.name = substitution[field]
				elif field == "descriptor":
					ingredient.descriptor = substitution[field]
				elif field == "preparation":
					ingredient.preparation = substitution[field]
	else:
		ingList.pop(ingList.index(ingredient))

def vegSubSteps(newIng, origIng, steps):
	newSteps = steps
	# print "!!! Substituting ", origIng.name," ", origIng.descriptor, " with ", newIng.name, " ", newIng.descriptor 
	for i,step in enumerate(steps):
		if hasattr(step, "direction"):
			step = step.direction
			newStep = step
			# STOCKS
			if origIng.name in stocks:
				if re.search("(?i)(bouillon|stock|broth)", step):
					splitWord = re.search("(?i)(bouillon|stock|broth)", step).group()
					descriptor = step.split(splitWord)[0].split(' ')[-2]
					sub = " ".join([newIng.descriptor, newIng.name])
					if descriptor in origIng.descriptor:
						newStep = re.sub("(?i)%s%s" % (origIng.descriptor, origIng.name), sub, step)
					else:
						newStep = re.sub("(?i)%s" % origIng.name, sub, newStep) 
			# MEATS
			if origIng.name in meats:
				if re.search("(?i)ground", origIng.descriptor):
					newStep = re.sub("(?i)ground %s" % origIng.name, newIng.name, step)
				elif re.search("(?i).*%s.*" % origIng.name, step):
					newStep = re.sub("(?i)%s" % origIng.name, newIng.name, newStep)
			elif findMeatDescriptor(origIng.descriptor):
				meat = findMeatDescriptor(origIng.descriptor)
				if re.search("(?i).*%s.*" % meat, step):
					newStep = re.sub("(?i)%s" % meat, newIng.name, newStep)

			newStep = sanitizeMeatDirections(newStep, newIng)

			# Replace udpated step
			newSteps[i].direction = newStep

	return newSteps

def findMeatDescriptor(descriptor):
	words = descriptor.split(' ')
	meat = ''
	# print words
	for word in words:
		if word in meats:
			meat = word
			break
	return meat

def sanitizeMeatDirections(step, newIng):		# Get rid of meat related directions
	meatyWords = ["grease", "until", "fat", "meat"]
	sentences = step.split(".")
	meatlessStep = ""
	for sentence in sentences:
		for word in meatyWords:
			if word == "until":
				if re.search("(?i).*(%s|%s).*" % (newIng.name, 'meat'), sentence):
					if re.search("(?i).*%s" % word, sentence):
						sentence = re.sub("(?i) until.*[;]", ";", sentence)
						sentence = re.sub("(?i) until.*$", "", sentence)
			elif word == "meat":
				if re.search("(?i).* %s" % word, sentence):
					sentence = ""
			else:
				if re.search("(?i).*%s" % word, sentence):
					if re.search("(?i).*%s.*[,;]" % word, sentence):
						sentence = re.sub("(?i).*%s.*[,;]" % word, "", sentence)
					else:
						sentence = re.sub("(?i).*%s.*" % word, "", sentence)
					sentence = re.sub('^[,:;] ', "", sentence)
					sentence = re.sub("^\s+", "", sentence).capitalize()
		if sentence:
			if meatlessStep:
				meatlessStep += "." + sentence
			else:
				meatlessStep += sentence

	return meatlessStep

##### HELPERS ######
def isStirFry(recipe):
	pat = "stir-fry"
	isStirFry = False
	if re.search("(?i).*%s.*" % pat, recipe.name):
		isStirFry = True

	return isStirFry


def isDeepFried(recipe):
	isFried = False
	if "fry" in recipe.primaryMethods:
		isFried = True

	return isFried

##### PRINTING ######
def printRecipe(recipe, transformType):	
	recipe.name = "%s Version of - " % transformType + recipe.name
	print recipe.unicode()

class Recipe:

    def updateString(self):

        self.string = ''
        self.string += 'Name: ' + self.name + '\n'
        self.string += 'Ingredients: \n'
        for ing in self.ingredients:
            self.string += ing.unicode() + '\n'

        self.string += 'Directions: \n'
        for direction in self.directions:
            self.string += direction +','
        #self.string += self.directions + '\n'
        self.string += '\nAuthor: ' + self.author + '\n'
        self.string += 'Cook Time: ' + self.cookTime + '\n'
        self.string += 'Servings: ' + str(self.servings) + '\n'
        self.string += 'Rating: ' + str(self.rating) + '\n'
        self.string += 'Tools: \n'

        for tool in self.tools:
            self.string += tool + ','

        self.string += '\nMethods: \n'

        for method in self.methods:
            self.string += method + ','

        self.string += '\nCuisine: ' + self.cuisine + '\n'

    def __init__(self, 
        name = None,
        ingredients = None,
        directions = None,
        author = None,
        cookTime = None,
        servings = None,
        rating = None,
        tools = None,
        methods = None,
        cuisine = None):

        self.string = ''

        if name == None:
            self.name = ''
        else:
            self.name = name

        if ingredients == None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

        if directions == None:
            self.directions = 'None'
        else:
            self.directions = directions

        if author == None:
            self.author = ''
        else:
            self.author = author

        if cookTime == None:
            self.cookTime = ''
        else:
            self.cookTime = cookTime

        if servings == None:
            self.servings = 0.0
        else:
            self.servings = servings

        if rating == None:
            self.rating = 0.0
        else:
            self.rating = rating

        if tools == None:
            self.tools = []
        else:
            self.tools = tools

        if methods == None:
            self.methods = []
        else:
            self.methods = methods

        if cuisine == None:
            self.cuisine = ''
        else:
            self.cuisine = cuisine

    def unicode(self):
        self.updateString()
        return self.string

class Ingredient:
    def updateString(self):
        self.string = ''
        self.string += 'Name: ' + self.name + '\n'
        self.string += 'Amount: ' + self.amount + '\n'
        self.string += 'Units: ' + self.unit + '\n'
        self.string += 'Descriptor: ' + self.descriptor + '\n'
        self.string += 'Preparation: ' + self.preparation + '\n'
        self.string += 'Category: ' + self.category + '\n'
        self.string += 'Protein: ' + self.protein + '\n'
        self.string += 'Fat: ' + self.fat + '\n'
        self.string += 'Carbs: ' + self.carbs + '\n'

    def __init__(self,
        name = None,
        origName = None,
        amount = None,
        unit = None,
        descriptor = None,
        preparation = None,
        category = None,
        protein = None,
        fat = None,
        carbs = None,
        id = None):

        if id == None:
            self.id = '00000'
        else:
            self.id = id

        if name == None:
            self.name = ''
        else:
            self.name = name

        if origName == None:
            self.origName = ''
        else:
            self.origName = origName
            
        if amount == None:
            self.amount = '0.0'
        else:
            self.amount = amount

        if unit == None:
            self.unit = 'Not specified'
        else:
            self.unit = unit

        if descriptor == None:
            self.descriptor = 'None'
        else:
            self.descriptor = descriptor

        if preparation == None:
            self.preparation = 'None'
        else:
            self.preparation = preparation

        if category == None:
            self.category = ''
        else:
            self.category = category

        if protein == None:
            self.protein = '0.00'
        else:
            self.protein = protein

        if fat == None:
            self.fat = '0.00'
        else:
            self.fat = fat

        if carbs == None:
            self.carbs = '0.00'
        else:
            self.carbs = carbs

    def unicode(self):
        self.updateString()
        return self.string

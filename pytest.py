import parsing
import lists

lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
lists.updateNameDB()

i = parsing.parseIngredient('imitation')
print i.descriptor






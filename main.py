import lists,scraper,parsing,objects
import veggieTransformer
import healthyTransformer
import cuisineTransformer
cuisineTypes = ['indian','mexican','chinese']

def main():
    lists.ingredientDB = parsing.readIngredientsFromFile('FOOD_DATA/FOOD_DES.txt')
    lists.updateNameDB()
    debug = True

    #Welcome message
    print "Welcome to SVJ Recipe Transformer created by Josiah Evans, Vanessa Fang and Salil Gupta"
    #Recipe input
    recipeURL = raw_input("Please input a recipe url from allrecipes.com:")

    print 'Loading recipe from allrecipes.com...'
    recipeInfo = scraper.retrieveRecipe(recipeURL)
    print 'Building recipe object...'
    recipe = parsing.buildRecipeObject(recipeInfo)

    print "Thanks! Now choose a transformation.\n We have three options:\n For a vegetarian tranformation (or 'un-vegetarian') type 0\n For a healthy transformation type 1\n For a cuisine transformation type 2"
    transformationType = int(raw_input("Transformation Selection: "))
    if transformationType ==0:
        print "Thanks! You have selected a veggie transformation. We are processing your request!"
        vegRecipe = veggieTransformer.veggieTransformer(recipe)
        veggieTransformer.printRecipe(vegRecipe, "Vegetarian")
    elif transformationType ==1:
        print "Thanks! You have selected a healthy transformation. We are processing your request!"
        healthyRecipe = healthyTransformer.healthyTransformer(recipe)
        healthyTransformer.printRecipe(healthyRecipe, "Healthy")
    elif transformationType ==2:
        print "Thanks! You have selected a cuisine transformation. Please choose a cuisine type:\n For Indian type 0 \n For Mexican type 1 \n for Chinese Type 2"
        cuisineType = int(raw_input("Cuisine Type: "))

        if cuisineType ==0:
            cuisineTransformer.cuisineChange(recipe,cuisineTypes[0])
        elif cuisineType ==1:
            cuisineTransformer.cuisineChange(recipe,cuisineTypes[1])
        elif cuisineType == 2:
            cuisineTransformer.cuisineChange(recipe,cuisineTypes[2])
        else:
            print "Sorry! But you must have typed an incorrect cuisine number!"
    else:
        print "Sorry! But you must have typed an incorrect transformation number!"

main()

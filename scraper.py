from bs4 import BeautifulSoup
from urllib2 import urlopen

def retrieveRecipe(url):
	recipePage = urlopen(url)
	soup = BeautifulSoup(recipePage.read())
	recipeInfo = {}

	# Recipe Components
	recipeInfo["title"] = soup.find(id="itemTitle").string
	recipeInfo["rating"] = soup.find(itemprop="ratingValue")["content"]
	recipeInfo["author"] = soup.find("span", {"id": "lblSubmitter"}).text
	recipeInfo["servings"] = soup.find(id="lblYield").string
	recipeInfo["time"] = soup.find_all("span", {"class":"time"})
	if recipeInfo["time"]:
		recipeInfo["time"] = recipeInfo["time"][0].text

	ingredientsListing = soup.findAll(itemprop="ingredients")
	ingredients = []
	for ingredient in ingredientsListing:
		if ingredient.find_next(id="lblIngName"):
			nextEl = ingredient.find_next(id="lblIngName")
			if nextEl["class"][0] == "ingred-heading" or nextEl.string.replace(u'\xa0', u' ') == " ":
				continue
			else:
				amount = ""
				name = ""
				if ingredient.find_next(id="lblIngAmount"):
					amount = ingredient.find_next(id="lblIngAmount").string
				if ingredient.find_next(id="lblIngName"):
					name = ingredient.find_next(id="lblIngName").string
				ingredients.append({"name": name, "amount": amount})
	recipeInfo["ingredients"] = ingredients

	directionsListing = soup.find_all("span", {"class":"plaincharacterwrap break"})
	directions = []
	for direction in directionsListing:
		directions.append(direction.string)
	recipeInfo["directions"] = directions


	return recipeInfo


'''def main(recipeURL):
	#recipeURL = 'http://allrecipes.com/Recipe/Basil-Chicken-over-Angel-Hair/Detail.aspx?soid=carousel_0_rotd&prop24=rotd'
	recipeInfo = retrieveRecipe(recipeURL)

	# Pretty print recipe info
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(recipeInfo)


main(sys.argv[1])'''

#  EXAMPLE OUTPUT
# retrieveRecipe('http://allrecipes.com/Recipe/Basil-Chicken-over-Angel-Hair/Detail.aspx?soid=carousel_0_rotd&prop24=rotd')
# {   'author': u'Wendy Mercadante',
#     'directions': [   u'In a large pot of salted boiling water, cook angel hair pasta until it is al dente, about 8 to 10 minutes. Drain, and set aside.',
#                       u'In a large skillet, heat oil over medium-high heat. Saute the onions and garlic. Stir in the tomatoes, chicken, basil, salt and hot pepper sauce. Reduce heat to medium, and cover skillet. Simmer for about 5 minutes, stirring frequently, until mixture is hot and tomatoes are soft.',
#                       u'Toss sauce with hot cooked angel hair pasta to coat. Serve with Parmesan cheese.'],
#     'ingredients': [   {   'amount': u'1 (8 ounce) package',
#                            'name': u'angel hair pasta'},
#                        {   'amount': u'2 teaspoons', 'name': u'olive oil'},
#                        {   'amount': u'1/2 cup',
#                            'name': u'finely chopped onion'},
#                        {   'amount': u'1 clove', 'name': u'garlic, chopped'},
#                        {   'amount': u'2 1/2 cups', 'name': u'chopped tomatoes'},
#                        {   'amount': u'2 cups',
#                            'name': u'boneless chicken breast halves, cooked and cubed'},
#                        {   'amount': u'1/4 cup', 'name': u'chopped fresh basil'},
#                        {   'amount': u'1/2 teaspoon', 'name': u'salt'},
#                        {   'amount': u'1/8 teaspoon',
#                            'name': u'hot pepper sauce'},
#                        {   'amount': u'1/4 cup', 'name': u'Parmesan cheese'}],
#     'rating': u'4.31783',
#     'servings': u'4 servings',
#     'time': u'35  mins',
#     'title': u'Basil Chicken over Angel Hair'}

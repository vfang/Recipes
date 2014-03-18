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

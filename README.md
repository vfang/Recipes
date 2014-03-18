SVJ Recipes
========
<b>Language:</b> Python 2.7 <br>
<b>Dependencies:</b> beautifulsoup4 (4.3.2)<br>
installed using pip<br>
sudo pip install beautifulsoup4<br>

FOOD_DATA folder sourced from USDA

<b>To Run: </b>
run python main.py and follow prompts

<b>To Autograde: </b>
```
python autograder.py 'some url from AllRecipes'
```
autograder.py prints ingredients, cooking methods, and cooking tools in format listed on the assignment sheet. Please see <b>objects.py</b> for complete ingredient, recipe, step models

Structure should be: 
```
Recipes\
	App\
		README.md
		__init__.py
		main.py
		lists.py
		parsing.py
		scraper.py
		veggieTransformer.py
		cuisineTransformer.py
		healthyTransformer.py
		autograder.py
		objects.py
		FOOD_DATA\
```

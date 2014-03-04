Recipes uses Flask 0.10.1 and Python 2.7

========

To set up Flask with virtualenv:

>> virtualenv Recipes
>> cd Recipes
>> . bin/activate
>> pip install Flask
>> mkdir app
>> cd app
>> git clone https://github.com/vfang/Recipes.git

========

In root directory (Recipes), create a file runFlask.py, and paste:

#!bin/python
from app import app
app.run(debug = True)


Then chmod runFlask.py:
>> chmod a+x runFlask.py

** This allows you to run ./runFlask.py in cmd line to start Flask's development server (will run at http://127.0.0.1:5000/)


========

Structure should be: 

Recipes\
	runFlask.py
	App\
		static\
			Css and Js files
		templates\
			html templates
		README.md
		__init__.py
		views.py


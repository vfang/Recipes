#list of predefined things
methods =[]
cuisines =[]
tools =["Apple corer", "Basting", 
"Biscuit cutter", "Biscuit press", "Blow torch", 
"Boil over preventer", "Bottle opener", "Bowl", 
"Bread knife", "Browning tray", "Butter curler", 
"Cake and pie server", "Cheese knife", "Cheesecloth", 
"Chef's knife", "Cherry pitter", "Chinoise", "Colander", 
"Corkscrew", "Crab cracker", "Cutting board", "Dough scraper", 
"Egg piercer", "Egg poacher", "Separating eggs", "Egg slicer", 
"Egg timer", "Fillet knife", "Urokotori", "Fish slice", 
"Flour sifter", "Food mill", "Funnel", "Garlic press", "Grapefruit knife", 
"Grater", "Gravy strainer", "Herb chopper", 
"Ladle", "Lame", "Lemon reamer", "Lemon squeezer", 
"Lobster pick", "Mandoline", "Mated colander pot", "Measuring jug", 
"Measuring spoon", "Meat grinder", "Meat tenderiser", "Meat thermometer", 
"Melon baller", "Mezzaluna", "Mortar and pestle", "Nutcracker", "Nutmeg grater", 
"Oven glove", "Pastry bag", "Pastry blender", "Pastry brush", "Pastry wheel", "Peel", 
"Peeler", "Pepper mill", "Pie bird", "Pizza cutter", "Potato masher", "Potato ricer",
"Pot-holder", "Poultry shears", "Potato ricer", "Roller docker", "Rolling pin",
"Salt shaker", "Weighing scale", "Scissors", "Scoop",
"Shellfish scraper", "Sieve", "Slotted spoon", "Spatula", "Spider",
"Sugar thermometer", "Tamis", "Tin opener", "Tomato knife", "Tongs", "Trussing needle",
"Whisk", "Wooden spoon", "Zester","pan","pot","knife","oven","microwave",
"wok","strainer","skillet","spoon","fork"]
ingredientDB = []
ingNameDB = {}

def updateNameDB():
	for ing in ingredientDB:
		ingNameDB[ing.name] = ing
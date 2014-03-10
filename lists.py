#list of predefined things
methods =["Bake", "Barbecue", "Baste", 
"Biomass briquettes", "Blacken", "Blanch", "Boil-up",
"Boil", "Braise", "Bread crumbs", "Brine", "Broast", "Brochette", 
"Brown", "caramelize", "Carry over cooking", "Casserole", "Charbroiler", 
"Chaunk", "Clay pot cooking", "Coddle", "Concasse", "Conche", "Confit",
"Cooking with alcohol", "Cream", "Culinary triangle", "Curdle", "Cure", 
"Deep fry", "Deglaze ", "Degrease", "Dredge ", "Dry roast", "Dry", 
"En papillote", "En vessie", "Engastration", "Engine Cooking",
"Flambé", "Foam ", "Fondue", "Fry", "Gentle fry", "Glaze", 
"Grill", "Infusion", "Juice","Maceration", "Marinate", "Pan fry",
"Par-cook", "Parboil", "Paste", "Pellicle ", "Pickle", 
"Poach", "Pre-ferment", "Pressure cooking", "Pressure fry", "Proof", 
"Purée", "Red cooking", "Reduction ", "Render", "Ricing ", "Roast",
"Robatayaki", "Rotisserie", "Saute", "Seare", "Season", "Shallow fry",
"Shrivelling", "Simmer", "Slow cook", "Smoke ", "Smother", "Souring", 
"Sous-vide", "Spatchcock", "Spherification", "Steam", "Steep", "Stew", 
"Stir fry","Sugar pan", "Sweat ", "Tataki", "Tenderize","Thicken","mix"]

cuisines =['chinese','italian','indian','american','british','mexican','spanish',
'japanese','korean','thai','filipino','german','french','middle eastern','mediterranian',
'ethiopian']

tools =["Apple corer", 
"Biscuit cutter", "Biscuit press", "Blow torch", 
"Boil over preventer", "Bottle opener", "Bowl", 
"Bread knife", "Browning tray", "Butter curler","baking pan", 
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
"Sugar thermometer","slow cooker" "Tamis", "Tin opener", "Tomato knife", "Tongs", "Trussing needle",
"Whisk", "Wooden spoon", "Zester","pan","pot","knife","oven","microwave",
"wok","strainer","skillet","spoon","fork"]

ingredientDB = []
ingNameDB = {}

def updateNameDB():
	for ing in ingredientDB:
		ingNameDB[ing.name] = ing
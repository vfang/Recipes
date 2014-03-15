#list of predefined things
units = ['cups','cup','teaspoon','tablespoon','teaspoons','tablespoons','gallon','liter'
'pound','pounds','gram','grams']

preparations = ['chopped','minced','sliced','crushed','melted','dried','grated','pounded','ground'
'diced','cubed','shredded','peeled']
descriptions = ['warm','sweet','fresh']

methods =['bake', 'barbecue', 'baste', 'biomass briquettes',
'blacken', 'blanch', 'boil-up', 'boil', 'broil','braise', 'bread crumbs',
'brine', 'broast', 'brochette', 'brown', 'caramelize', 'carry over cooking',
'casserole', 'charbroiler', 'chaunk', 'clay pot cooking', 'coddle',
'concasse', 'conche', 'confit', 'cooking with alcohol', 'chop','cut','cream',
'culinary triangle', 'curdle', 'cure', 'deep fry', 'deglaze ',
'degrease', 'dredge ', 'dry roast', 'dry', 'en papillote', 'en vessie',
'engastration', 'engine cooking', 'flambe', 'foam ', 'fondue', 'fry',
'gentle fry', 'glaze', 'grill','grease', 
'infusion', 'juice', 'maceration', 'marinate', 'pan fry', 
'par-cook', 'parboil','paste','pellicle ', 'pickle', 'poach', 
'pre-ferment', 'pressure cooking', 'pressure fry', 'proof', 'puree', 
'red cooking', 'reduction ', 'render', 'ricing ', 'roast', 'robatayaki', 
'rotisserie', 'saute', 'seare', 'season', 'shallow fry', 'shrivelling', 
'simmer', 'slow cook','shred','smoke ', 'smother', 'souring', 'sous-vide', 'spatchcock', 
'spherification', 'steam', 'steep', 'stew', 'stir','stir fry', 'sugar pan', 'sweat ', 
'tataki', 'tenderize', 'thicken', 'mix','preheat', 'scald', 'drain', 'mash', 'pour', 'spread', 'combine'
'head']

cuisines=['chinese', 'italian', 'indian', 'american',
'british', 'mexican', 'spanish', 'japanese', 'korean',
'thai', 'filipino', 'german', 'french', 'middle eastern',
'mediterranian', 'ethiopian']

tools=['apple corer', 'biscuit cutter', 'biscuit press', 'blow torch', 
'boil over preventer', 'bottle opener', 'bowl', 'bread knife', 'browning tray', 
'butter curler', 'baking pan', 'cake and pie server', 'cheese knife', 
'cheesecloth', "chef's knife", 'cherry pitter', 'chinoise', 'colander', 
'corkscrew', 'crab cracker', 'cutting board', 'dough scraper', 'egg piercer', 
'egg poacher', 'separating eggs', 'egg slicer', 'egg timer', 'fillet knife', 
'urokotori', 'fish slice', 'flour sifter', 'food mill', 'funnel', 'garlic press', 
'grapefruit knife', 'grater', 'gravy strainer','grill' 'herb chopper', 'ladle',
'lame', 'lemon reamer', 'lemon squeezer', 'lobster pick', 'mandoline', 
'mated colander pot', 'measuring jug', 'measuring spoon', 'meat grinder', 
'meat tenderiser', 'meat thermometer', 'melon baller', 'mezzaluna', 
'mortar and pestle', 'nutcracker', 'nutmeg grater', 'oven glove', 'pastry bag', 
'pastry blender', 'pastry brush', 'pastry wheel', 'peel', 'peeler', 
'pepper mill', 'pie bird', 'pizza cutter', 'potato masher', 'potato ricer', 
'pot-holder', 'poultry shears', 'potato ricer', 'roller docker', 
'rolling pin', 'salt shaker', 'weighing scale', 'scissors', 'scoop', 
'shellfish scraper', 'sieve', 'slotted spoon', 'spatula', 'spider', 
'sugar thermometer', 'slow cookertamis', 'tin opener', 'tomato knife', 
'tongs', 'trussing needle', 'whisk', 'wooden spoon', 'zester', 'pan', 'oven broiler',
'pot', 'knife', 'oven', 'microwave', 'wok', 'strainer', 'skillet', 'spoon', 'fork','slow cooker','saucepan']

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white', 'black', 'brown']

##############################
# Lists for Transformers
poultryAndGame = ['chicken','duck','turkey','goose', 'quail', 'rabbit', 'venison']
livestock = ['beef','veal', 'bison', 'goat', 'lamb', 'mutton', 'pork']
prepared = ['bacon', 'ham', 'meatball', 'pepperoni', 'salami', 'sausage']
seafood = ['crab', 'crayfish', 'lobster', 'shrimp', 'prawn', 'anchovy', 'basa', 
			'bass', 'catfish', 'carp', 'cod', 'crappie', 'eel', 'flounder', 'grouper', 'haddock',
			'halibut', 'herring', 'kingfish', 'mackerel', 'mahi mahi', 'marlin', 'milkfish', 
			'orange roughy', 'pacific saury', 'perch', 'pike', 'pollock', 'salmon', 
			'sardine', 'sole', 'swordfish', 'tilapia', 'trout', 'tuna', 'walleye', 'oyster', 'oysters', 'clam', 'clams']
meats = poultryAndGame + livestock + prepared + seafood
stocks = ["stock", "broth", "bouillon"]
vegSubstitutions = {
				"ground poultry": {"name": "beans", "descriptor": "canned cannellini", "preparation": "drained"},
				"ground livestock": {"name": "beans", "descriptor": "canned red kidney", "preparation": "drained"},
				"poultry": {"name": "tofu", "descriptor": "firm", "preparation": "drained"},
				"livestock": {"name": "mushroom", "descriptor": "portobello", "preparation": ""},
				"stock": {"name": "", "descriptor": "vegetable", "preparation": ""},
				"seafood": {"name": "tofu", "descriptor": "firm", "preparation": "drained"},
				}

healthySubstitutions = {
	"milk": {"": "skim milk"} ,
	"mayonnaise": {"": "light mayonnaise"},
	"sauce": {"soy": "low-sodium soy sauce", "": ""},
	"yogurt": {"": "low-fat yogurt"},
	"butter": {"peanut": "almond butter", "": "olive oil"},
	"cheese": {"cream": "fat-free ricotta cheese", "": "reduced-fat cheese"},
	"bread": {"white": "whole-grain bread", "": ""},
	"pasta": {"": "whole-grain pasta"},
	"white rice": {"white": "brown rice", "": ""},
	"cream": {"heavy": "evaporated skim milk", "sour": "greek yogurt","ice": "low-fat ice cream", "":""},
	"potato": {"":"sweet potato"},
	"potatoes": {"": "sweet potatoes"},
	"shortening": {"":"margarine"},
}

##############################

ingredientDB = []
ingNameDB = {}

def updateNameDB():
	for ing in ingredientDB:
		ingNameDB[ing.name] = ing




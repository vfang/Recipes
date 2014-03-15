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
meats = poultryAndGame + livestock + prepared
stocks = ["stock", "broth", "bouillon"]
vegSubstitutions = {
				"ground poultry": {"name": "beans", "descriptor": "canned cannellini", "preparation": "drained"},
				"ground livestock": {"name": "beans", "descriptor": "canned red kidney", "preparation": "drained"},
				"poultry": {"name": "tofu", "descriptor": "firm", "preparation": "drained"},
				"livestock": {"name": "mushroom", "descriptor": "portobello", "preparation": ""},
				"stock": {"name": "", "descriptor": "vegetable", "preparation": ""},
				}

healthySubstitutions {
	"milk": "skim milk",
	"mayonnaise": "light mayonnaise",
	"soy sauce": "low-sodium soy sauce",
	"yogurt": "low-fat yogurt",
	"peanut butter": "natural peanut butter",
	"cheese": "reduced-fat cheese",
	"white bread": "whole-grain bread",
	"pasta": "whole-grain pasta",
	"white rice": "brown rice",
	"butter": "olive oil",
	"heavy cream": "evaporated skim milk",
	"beef": "bison",
	"ground beef": "ground turkey",
	"potato": "sweet potato",
	"potatoes": "sweet potatoes",
	"sour cream": "greek yogurt",
	"shortening": "margarine",
	"cream cheese": "fat-free ricotta cheese"
}
##############################

ingredientDB = []
ingNameDB = {}

def updateNameDB():
	for ing in ingredientDB:
		ingNameDB[ing.name] = ing




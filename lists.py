#list of predefined things
secondaryMethods =[ 'baste','beat' 'biomass briquettes',
'brochette', 'carry over cooking', 'charbroiler', 'chaunk', 'clay pot cooking', 'coddle',
'concasse', 'conche', 'confit', 'cooking with alcohol', 'chop','cut','cream',
'culinary triangle', 'curdle', 'cure', 'deglaze ',
'degrease', 'dredge ','dry', 'en papillote', 'en vessie',
'engastration', 'engine cooking',  'foam ', 'fondue','glaze','grease', 
'infusion', 'juice', 'maceration', 'marinate',  
'par-cook', 'paste','pellicle ', 'pickle',  
'pre-ferment','proof', 'puree', 
'red cooking', 'reduction', 'render', 'ricing ', 'robatayaki', 
'rotisserie','season', 'shrivelling', 
'shred','smother', 'souring', 'sous-vide', 'spatchcock', 
'spherification', 'steep', 'stew', 'stir', 'sugar pan', 'sweat ', 
'tataki', 'tenderize', 'thicken', 'mix','mince' 'scald', 'drain', 'mash',
'pour', 'spread', 'combine','coat','refrigerate','rinse','dredge','pound']

primaryMethods = ['bake','barbecue','boil', 'broil','brown','braise','flambe','broast','dry roast','stir fry', 'stir-fry',
'saute','slow cook','shallow fry','pressure cooking','pressure cook', 'pressure fry','poach','pan fry','pan-fry','grill',
'brochette','caramelize','blacken','seare','deep fry','deep-fry', 'parboil','roast','steam','fry',
'gentle fry','simmer','smoke','preheat','heat']

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
'shellfish scraper', 'sieve', 'slotted spoon', 'spatula', 'spider', 'meat mallet',
'sugar thermometer', 'slow cookertamis', 'tin opener', 'tomato knife', 
'tongs', 'trussing needle', 'whisk', 'wooden spoon', 'zester', 'pan', 'oven broiler',
'pot', 'knife', 'oven', 'microwave', 'wok', 'strainer', 'skillet', 'spoon', 'fork','slow cooker','saucepan']

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white', 'black', 'brown']

##############################
# Lists for Transformers
poultryAndGame = ['chicken', 'duck', 'turkey', 'goose', 'quail', 'rabbit', 'venison', 'new world quail', 'pheasant', 'grouse', 'pigeon', 'ostrich', 'emu', 'cornish hen', 'partridge', 'dove', 'guinea fowl']
livestock = ['beef','veal', 'bison', 'goat', 'lamb', 'mutton', 'pork', 'steak', 'chuck','moose','deer']
prepared = ['bacon', 'ham', 'meatball', 'pepperoni', 'salami', 'sausage']
seafood = ['crab', 'crabmeat', 'crayfish', 'lobster', 'shrimp', 'prawn', 'anchovy', 'basa', 'bass', 'catfish', 'carp', 'cod', 'crappie', 'eel', 'flounder', 'grouper', 'haddock', 'halibut', 'herring', 'kingfish', 'mackerel', 'mahi mahi', 'marlin', 'milkfish', 'orange roughy', 'pacific saury', 'perch', 'pike', 'pollock', 'salmon', 'sardine', 'sole', 'swordfish', 'tilapia', 'trout', 'tuna', 'walleye', 'oyster', 'oysters', 'clam', 'clams', 'snapper', 'loc', 'snail', 'conch', 'scallop', 'escargot', 'abalone', 'mussel', 'octopus', 'cuttlefish']
meats = poultryAndGame + livestock + prepared + seafood
stocks = ["stock", "broth", "bouillon"]
legumes = ['abura-age','aburage','aka miso','akamiso','anasazi beans','appaloosa bean','apricot seed','arhar','arhar dal','asuki bean','atsuage','atsu-age','awase miso','azufrado bean','baby lima bean','bamboo yuba','barley miso','bayo bean','bean cheese','bean curd','bean curd sheets','bean curd skins','bean curd stick','bean paste','bean stick','beechmast','beluga black lentil','beluga lentil','bengal gram','black aduki bean','black adzuki bean','black azuki bean','black bean','black beans in salted sauce','black chickpeas','black gram','black lentil','black salted fermented bean','black turtle bean','bolita bean','bonavist bean','borlotti bean','boston bean','boston navy bean','breadnut seeds','brown lentil','brown rice miso','brown speckled cow bean','buah keras','butternut','butterscotch calypso bean','calypso bean','canaria bean','canario bean','chana dal','channa dal','chestnut lima bean','chili bean','chilke urad','chinese black bean','chinese yuba','chowli dal','christmas lima bean','chufa','coco bean','coco blanc bean','continental lentil','crab eye bean','cranberry bean','daal','dal','dark miso','deep-fat fried tofu','deep-fried tofu','dermason bean','dhaal','dhal','dhall','doufu','dow fu kon','dow see','dried bean curd stick','dried bean stick','dried chestnut','egyptian bean','egyptian lentil','egyptian white broad bean','european soldier bean','extra-firm tofu','eye of goat bean','eye of the goat bean','fagioli','fagiolo romano','fayot','fazolia bean','fermented bean cake','fermented bean curd','fermented black bean','fermented soy cheese','firm tofu','flageolet','foo yi','foo yu','french green lentils','fried bean curd','frijo bola roja','frijole negro','fu jook pei','fu yu','fuji mame','genmai miso','german lentil','gram dal','great northern bean','green gram','green lentil','hang yen','haricot bean','haricot blanc bean','hatcho miso','hat-cho miso','hyacinth bean','inaka miso','inariage','indian bean','indian brown lentil','jackson wonder bean','kala channa','kali dal','kemiri','kidney bean','kinu-goshi','kirazu','kluwak kupas','kyoto shiro miso','lablab bean','lablab beanval','lentilles du puy','lentilles vertes du puy','ling chio','ling jiao','ling kio','ling kok','lingot bean','lupini bean','maicoba bean','maine yellow eye','mame miso','mamemiso','mape','marron','marrow bean','masar','masar dal','masoor','masoor dal','masur dal','matki','mayocoba bean','medium tofu','mellow miso','mexican black bean','mexican red bean','miso','moath','molasses face bean','moong dal','mortgage lifter bean','mortgage runner bean','mugi miso','mung bean','mung pea','mungo bean','mussoor','mussoor dal','nama nori san','nama-age','nato','natto','nattou','navy bean','nigari tofu','okara','orca bean','pea bean','peanuts','pearl haricot','pecan','peruano bean','peruvian bean','petite beluga lentil','pignoli','pignolia','pignolo','pine kernel','pink bean','pink lentil','pinolea','pinoli','pinto bean','pinyon','plant protein','preserved bean curd','pressed tofu','prince bean','protein crumbles','purple appaloosa bean','puy lentils','rajma','rattlesnake bean','red ball bean','red bean','red eye bean','red kidney bean', 'beans','red lentil','red miso','refried beans','regular tofu','roasted soybeans','roman bean','rosecoco bean','salted black bean','salty black bean','saluggia','salugia bean','scarlet runner bean','sendai miso','shell bean','shinshu miso','shiro miso','shiromiso','sieva bean','silken tofu','skinned and split black lentils','small red bean','small white bean','snoober','soft tofu','soy cheese','soy mayonnaise','soy milk skins','soy nut butter','soy nuts','soy sour cream','soy yogurt','soya cheese','soya mayonnaise','soybean curd','soybean paper','soybean paste','soynut butter','soynuts','spanish black bean','spanish tolosana bean','speckled brown cow bean','split black lentils','split lablab beans','steuben yellow bean','steuben yellow eye bean','sui-doufu','swedish brown bean','sweet miso','sweet white miso','tempe','tempeh','textured soy protein','textured vegetable protein','texturized soy protein','texturized vegetable protein','tofu','tofu mayonnaise','tofu sour cream','tolosana bean','tongues of fire bean','toor','toor dal','tremmocos','trout bean','tur','tur dal','turtle bean','turtle soup bean','tuvar','tuvar dal','tvp','uba','unohana','urad dal','usuage','usu-age','val dal','vallarta bean','vegetable protein','water caltrop','wet bean curd','whit bean','white kidney bean','white lentils','white miso','white pea bean','yankee bean','yellow indian woman bean','yellow lentils','yellow miso','yin yang bean','yuba']
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

cuisines = {
	"indian":{
		"meats":['chicken','mutton','lamb'],
		"cheese":['cottage cheese'],
		"sauces":['tomato puree','lentils(dal)'],
		"spices":['turmeric','garam masala','cumin'],
		"herbsAndGarnish":['garlic','ginger','cardamon','almonds','coriander'],
		"breads":['naan'],
		"veggies":['potatoes','tomatoes','onions','okra','carrots','peas','beans']
	},
	"mexican":{
		"meats":['chicken','pork'],
		"cheese":['Oaxaca cheese'],
		"sauces":['refried beans','chipotle','salsa','guacamole','red mole'],
		"spices":['cumin','chili powder','cayene'],
		"herbsAndGarnish":['cilantro','lime','garlic','chipotle'],
		"breads":['tortilla'],
		"veggies":['onions','corn','tomato','bell peppers']
	},
	"chinese":{
		"meats":['chicken','pork'],
		"cheese":['remove'],
		"sauces":['soy sauce','oyster sauce','teriyaki sauce','sriracha','hoisin sauce','sesame oil'],
		"spices":None,
		"herbsAndGarnish":['ginger','garlic','green onion','chili peppers','basil'],
		"breads":None,
		"veggies":['onions','bok choy','cabbage','water chesnuts','bell peppers']
	},
}



ingredientDB = []
ingNameDB = {}

def updateNameDB():
	for ing in ingredientDB:
		ingNameDB[ing.name] = ing




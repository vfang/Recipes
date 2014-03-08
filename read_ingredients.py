#Modules to import
from objects import *
#Functions

def tokenizeLine(string):
	
	line = string.split('^')
	numArgs = len(line)
	out = []

	for item in line:

		if item == '':

			out.append(item)

		else:

			if item[0] != '~':

				out.append(item)

			else:

				text = item.split('~')
				empty = False
				appended = False

				for word in text:

					if len(text) == 3 and text[1] == word and word != '':

						out.append(word)
						appended = True

					if empty and word == '' and not appended:

						out.append(word)
						empty = False
						appended = True

					else:

						if word == '':

							empty = True

	return out

def readObjectFromLine(line):

	#fields = 0

	#if objectType == 'FOOD':
		
	#	isFood = True
	#	fields = 14

	#elif objectType == 'NUTIRENT':

	#	isNutrient = True
	#	fields = 6

	#else:

	#	print('objectType not recognized.')
	#	return None

	tokens = tokenizeLine(line)

	

	output = ingredient()

#	output.id = tokens[0]
	output.category = tokens[1]
	output.descriptor = tokens[2]
	#	output.shortDesc = tokens[3]
	output.name = tokens[4]
	#	output.manufacName = tokens[5]
	#	output.survey = tokens[6]
	#	output.refDesc = tokens[7]
	#	output.refuse = tokens[8]
	#	output.sciName = tokens[9]
	#	output.nFactor = tokens[10]
	#	output.proFactor = tokens[11]
	#	output.fatFactor = tokens[12]
	#	output.carbFactor = tokens[13]

	return output

def readObjectsFromFile(fileName):

	objectList = []

	with open(fileName, 'r', encoding="utf8") as f:

		while(True):

			line = f.readline()

			if not line:

				break

			objectList.append(readObjectFromLine(line))

	return objectList










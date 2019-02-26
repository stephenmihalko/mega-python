import json	# for reading json text files
import difflib	# for determining differences in strings

def definition(word):
	# This is the most likely result and the result that requires the least actual work!
	if word.lower() in data:
		# This joins the definitions with the newline character - the more pythonic way!
		return "\n".join(data[word.lower()])
	
	# Maybe they're looking for something like "USA"
	elif word.upper() in data:
		return "\n".join(data[word.upper()])
	
	# Maybe they're looking for a proper noun!
	elif word.capitalize() in data:
		return "\n".join(data[word.capitalize()])
	
	# Maybe they misspelled it.
	else:
		# Getting the four best matches
		potentials = difflib.get_close_matches(word.lower(), data.keys(), n=4)
		
		# Ask if they wanted the closest word in the dictionary, then recursion to get that definition.
		if len(potentials) > 0:
			print("The word is not in the dictionary. Did you mean one of the following?")
			for ndx, el in enumerate(potentials):
				print(ndx+1, el)
			choice = input("0 No, none of these\n")
			return definition(potentials[int(choice)-1]) if int(choice)-1 < len(potentials) and int(choice) != 0 else "Sorry about that."
		else:
			return "The word does not exist. Please try again."

# This is a dictionary where words are keys and definitions are values.
with open("data.json") as fh:
	data = json.load(fh)

	# Ask the user for a word.
	wd = input("Please enter a word: ")

	# Get the definition and print it.
	print(definition(wd))


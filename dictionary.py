import json	# for reading json text files
import difflib	# for determining differences in strings

def definition(word):
	word = word.lower()
	# This is the most likely result and the result that requires the least actual work!
	if word in data:
		return data[word]
	else:
		potentials = difflib.get_close_matches(word, data.keys())
		if len(potentials) > 0:
			return data[potentials[0]] if input("The word does not exist. Did you mean '%s'? Enter Y or N: " % potentials[0]) == "Y" else "Sorry about that."
		else:
			return "The word does not exist. Please try again."

# This is a dictionary where words are keys and definitions are values.
with open("data.json") as fh:
	data = json.load(fh)

	# Ask the user for a word.
	wd = input("Please enter a word: ")

	# Get the definition and print it.
	print(definition(wd))


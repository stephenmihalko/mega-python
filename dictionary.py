import json	# for reading json text files
import difflib	# for determining differences in strings

def definition(word):
	word = word.lower()
	if word in data:
		return data[word]
	else:
		potential = difflib.get_close_matches(word, data.keys(), n = 1)
		return ("The word does not exist. Did you mean %s?" % potential[0])

# This is a dictionary where words are keys and definitions are values.
data = json.load(open("data.json"))

# Ask the user for a word.
wd = input("Please enter a word: ")

# Get the definition and print it.
print(definition(wd))



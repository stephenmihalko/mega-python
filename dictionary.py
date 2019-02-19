import json

def definition(word):
	if word in data.keys():
		return data[word]
	else:
		return "The word does not exist."

# This is a dictionary where words are keys and definitions are values.
data = json.load(open("data.json"))

# Ask the user for a word.
wd = input("Please enter a word: ")

# Get the definition and print it.
print(definition(wd))



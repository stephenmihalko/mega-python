import json

# This is a dictionary where words are keys and definitions are values.
data = json.load(open("data.json"))


def definition(word):
	if word in data.keys():
		return data[word]
	else:
		return "The word does not exist."

# Band name generator
import random


titles = ["gignatic", "sour", "steamy", "gross", "stupid", "ironic", "greasy",
		  "tangy", "smelly", "small", "inventive", "spherical", "spiritual", "green",
		  "blue", "pot bellied", "pickled", "prickly"]

adjs = ["tiny", "fat", "shiny", "ecclectic", "fluffy", "bright", "corrupt",
		"aggressive", "thoughtless", "delirious", "amazing"]

plural_nouns = ["apples", "bears", "frogs", "mice", "eggs", "herbs", "rabbits",
				"indians", "unicorns", "spices", "mammoths", "pony tails"]

def title():
	#chooses title for the name
	return random.choice(titles)

def adj():
	#chooses an adjective for the name
	return random.choice(adjs)

def plural_noun():
	#uses a plural noun for the name
	return random.choice(plural_nouns)

def main():
	while True:
		name = raw_input("Enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()

main()
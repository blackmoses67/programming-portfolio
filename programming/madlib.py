def mad():
	adj1 = raw_input("Please enter an adjective: ")
	adj2 = raw_input("Please enter an adjective: ")
	bird = raw_input("Please enter a type of bird: ")
	room = raw_input("Please enter the name of a room in a house: ")
	verb_past = raw_input("Please enter a past tense verb: ")
	verb1 = raw_input("Please enter a verb: ")
	relative_name = raw_input("Please enter the name of a relative: ")
	noun1 = raw_input("Please enter a noun: ")
	liquid = raw_input("Please enter a liquid: ")
	verb2 = raw_input("Please enter a verb ending in -ing: ")
	body_part = raw_input("Please enter a part of the body: ")
	noun2 = raw_input("Please enter a plural noun: ")
	verb3 = raw_input("Please enter a verb ending in -ing: ")
	noun3 = raw_input("Please enter a noun: ")
	print "\n"

	print "it was a " + adj1 + ", cold Novenber day."
	print "I woke up to the " + adj2 + " smell of " + bird
	print "roasting in the " + room + " downstairs."
	print "I " + verb_past + " down the stairs to see if I"
	print "could help " + verb1 + " the dinner."
	print "My mom said, 'See if " + relative_name + " needs a fresh"
	print noun1 + ".' So I carried a tray of glasses full of " + liquid
	print "into the " + verb2 + " room. When I got there, I"
	print "couldn't believe my " + body_part + "! There were"
	print noun2 + " " + verb3 + " on the " + noun3 + "!"
	print "\n"
	print "I hope you enjoyed the story!"
	print "\n"

def main():
	print "Welcome to the Mad Lib Game!"
	print "Just follow the directions and you will write an incredible story!"
	game = 1
	while game == 1:
		mad()
		a = int(raw_input("enter 0 to play again or any number to quit: "))
		game += a
	print "Thanks for playing!"
main()
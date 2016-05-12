#band name generator
import sys
import random

def main(argv):
	#These are the lists of different words that will be used for the name
	print "This is fun"
	adjective_title = ['Tiny', 'fat', 'Gigantic', 'Extrordinary',
	'Weak', 'Wild', 'Tragic', 'Tubby', 'Little', 'Fantastic', 'Big',
	'corrupt', 'aggressive', 'stupid', 'steamy']

	adjective = ['Casual', 'Kind', 'Careful', 'Terible', 'Smashing', 'Angry',
	'Shameless', 'Sour', 'Stale', 'Strange', 'silver', 'smelly', 'magical',
	'courageous', 'fierce', 'colorless', 'thoughtless', 'smart', 'dangerous']

	plural_noun = ['Frogs', 'Grapes', 'Llamas', 'Eggs', 'Rats', 'Knights'
	'mammoths', 'rabbits', 'sloths', 'unicorns', 'indians']

	while True:
		#This puts it all together
		name = raw_input('enter your name >>> ')
		title = random.choice(adjective_title)
		adjs = random.choice(adjective)
		noun = random.choice(plural_noun)
		print title, name, "and the", adjs, noun
		
		

if __name__ == "__main__":
	main(sys.argv)
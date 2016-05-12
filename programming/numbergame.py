def show_instructions():
	print """Pick a number between 1 and 1000
	and I will try to guess it.

	I can do this in no more than 10 guesses.

	After each guess, enter:
	0 - if I was correct
	-1 - if I was too high
	1 - if I was too low
	"""

def take_guess(high, low):
	guess = 
	keep_asking = 1
	while keep_asking == 1:
		print guess
		answer = raw_input("Was I right? ")
		if answer == "0":
			print "I got it right"
			keep_asking = 0
		elif answer == "-1":
			print "I will go lower"
			keep_asking = 0
		elif answer == "1":
			print "I will go higher"
			keep_asking = 0
		else:
			print "-1, 0, or 1"
	print "\n"
	return answer

def main():
	show_instructions()
	high = 1000
	low = 1
	guesses = 1
	while high > low:
		response = take_guess(high, low)
		if response == "0":
			high = 0
		elif response == "-1":
			high = guess - 1
			guesses += 1
		elif response == "1":
			low = guess + 1
			guesses += 1

	if high == low:
		print high
	print guesses

main()
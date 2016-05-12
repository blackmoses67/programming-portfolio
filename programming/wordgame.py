#I guess I have to make rock paper scissors again...
games = 0
player = 0
round_number = int(raw_input("How many games would you like to play? >>> "))
while games < round_number:
	word = raw_input("enter a word >>> ")
	word_length = len(word)
	print "now, how long was the word you chose?"
	word_length2 = int(raw_input("how long? >>> "))
	if word_length2 == word_length:
		print "you were correct!"
		print word_length
		games += 1
	else:
		print "Incorrect! your guess was"
		print word_length2
		print "the answer was"
		print word_length
		games += 1
print "good game, I hope to play again sometime."
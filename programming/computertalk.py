#this will look like the computer is talking to me
turn = 0
while turn > 8:
	print "Hello, my name is imac."
	turn +=1
	raw_input("What is your name? >>> ")
	turn +=1
	print "That is a very interesting name."
	turn +=1
	raw_input("Where did it come from? >>> ")
	turn +=1
	print "Outstanding! Mine came from the mind of a man from Texas and a type of tree."
	turn +=1
	print "What do you do for a living?"
	turn +=1
	a = raw_input("do you work? (y or n) >>> ")
	if a == "y":
		print "Where? >>>"
		turn +=1
	elif a == "n":
		print "That is unfortunate."
		turn +=1
	else:
		print "You could have just said you did not want to talk about it."
		turn +=1
	print "Well, I hope all goes well for you no matter how your situation changes."
	turn +=1
	print "Good-bye!"
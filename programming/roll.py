#die
import random

def roll_die(sides):
	x = random.randrange(1, sides+1)
	return x

def main():
	x = int(raw_input("how many sides? "))
	while True:
		print roll_die(x)

main()
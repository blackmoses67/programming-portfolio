#game of pig
import random

def roll_die(sides):
	x = random.randrange(1, sides+1)
	return x

def take_turn():
	turn_points = 0
	keep_rolling = 1
	raw_input("press enter to begin:")
	while keep_rolling == 1:
		x = roll_die(6)
		print "you rolled a(n)", x
		if x == 1:
			turn_points -= turn_points
			keep_rolling -= 1
		else:
			turn_points += x
			print turn_points
			keep_playing = raw_input("keep playing? y/n: ")
			if keep_playing == 'y':
				keep_rolling += 0
			else:
				keep_rolling -= 1
	print "you scored", turn_points, "points"
	return turn_points

def show_instrunctions():
	print """Welcome to the Game of Pig.  To win, be the
player with the most points at the end of the
game.  The game ends at the end of a round where
at least one player has 100 or more points.

On each turn, you may roll the die as many times
as you like to obtain more points.  However, if
you roll a 1, your turn is over, and you do not
obtain any points that turn."""

def main():
	show_instrunctions()
	p1 = 0
	p2 = 0
	while p1 < 100 and p2 < 100:
		print "player 1 has", p1, "points"
		print "player 2 has", p2, "points"
		p1 += take_turn()
		print "Player 1 now has", p1, "points"
		p2 += take_turn()
		print "Player 2 now has", p2, "points"
	print "player 1 finished with", p1, "points"
	print "player 2 finished with", p2, "points"
	if p1 > p2:
		print "player 1 wins"
	elif p2 > p1:
		print "player 2 wins"
	else:
		print "the game is a tie."

main()
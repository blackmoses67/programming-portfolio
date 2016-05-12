def main():
	pts = 0
	shotsMade = 0
	shotsTaken = 0
	reb = 0
	ast = 0
	stl = 0
	blk = 0
	mins = 0
	games = 1
	while games <= 82:
		print "\n"

		#points per game
		p = float(raw_input("Enter Points: "))
		pts += p
		PPG = pts / games
		print "Player scored", p, "Points in this game"
		print "Player has scored", pts, "Points this season"
		print "Player averages", PPG, "Points per game"
		print "\n"

		#field goal percentage
		sm = float(raw_input("Enter shots made: "))
		st = float(raw_input("Enter shots taken: "))
		print "\n"
		shotsMade += sm
		shotsTaken += st
		print "He has made", shotsMade, "this season"
		print "He has taken", shotsTaken, "this season"
		print "\n"
		seasonFGP = shotsMade / shotsTaken
		gameFGP = sm / st
		print "The player shot", gameFGP, "percent in this game"
		print "The player averages", seasonFGP, "this season"
		print "\n"

		#rebounds per game
		r = float(raw_input("Enter Rebounds: "))
		reb += r
		RPG = reb / games
		print "Player got", r, "Rebounds in this game"
		print "Player has gotten", reb, "Rebounds this season"
		print "Player averages", RPG, "Rebounds per game"
		print "\n"

		#assists per game
		a = float(raw_input("Enter Assists: "))
		ast += a
		APG = ast / games
		print "Player got", a, "Assists in this game"
		print "Player has gotten", ast, "Assists this season"
		print "Player averages", APG, "Assists per game"
		print "\n"

		#steals
		s = float(raw_input("Enter Steals: "))
		stl += s
		SPG = stl / games
		print "Player got", s, "Steals in this game"
		print "Player has gotten", stl, "Steals this season"
		print "Player averages", SPG, "Steals per game"
		print "\n"

		#blocks
		b = float(raw_input("Enter Steals: "))
		blk += b
		BPG = blk / games
		print "Player got", b, "Blocks in this game"
		print "Player has gotten", blk, "Blocks this season"
		print "Player averages", BPG, "Blocks per game"
		print "\n"

		#minutes
		m = float(raw_input("Enter minutes played: "))
		mins += m
		MPG = mins / games
		print "Player played", m, "Minutes this game"
		print "Player averages", MPG, "Minutes per game"
		print "\n"

		print "Are you finished?"
		end = raw_input("end or no: ")
		if end == "end":
			break

	print "the season has ended"

main()

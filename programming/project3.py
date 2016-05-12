#lets start something new.
def NewPass():
	password = ""
	while len(password) < 5:
		print "please enter a new password."
		password += raw_input("Enter a new password: ")
		return password

def main():
	NewPass()
	
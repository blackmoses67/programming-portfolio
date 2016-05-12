# encryption program
import random

def PrintDescription():
	print """
This program encrypts and decrypts messages, using multiple encryption methods.
Input files must be in the same directory as this program.
Output files will be created in this same directory.
"""

def StartMenu():
	print """
Do you want to encrypt or decrypt?
(e)ncrypt
(d)ecrypt
(q)uit
"""
	choice = ''
	while choice != 'e' and choice != 'd' and choice != 'q':
	    choice = raw_input("choose: ")
	
	return choice
	
def MethodMenu():
	print """
Which method do you want to use?
(c)aesarian fixed offset
(p)seudo-random offset
(s)ubstitution cipher
"""
	choice = ''
	while choice != 'c' and choice != 'p' and choice != 's':
		choice = raw_input("choose: ")
	
	return choice

def Caesarian(fin, fout, encrypt_or_decrypt_choice, alphabet):
    # Determine the offset by generating a random number in the correct range.
    # This will be the same random number, if the password sent to random.seed is the same.
    offset = random.randrange(1,len(alphabet))
    if encrypt_or_decrypt_choice=='d':
        offset = -offset
    print "Using the secret offset of", offset

    # Read every line of the input file.
    for line1 in fin:
        # Alter each character of the line1, putting the result into line2.
        line2 = ""
        for c in line1:
            if c in alphabet:
                pos1 = alphabet.find(c)
                pos2 = (pos1+offset)%len(alphabet)
                line2 += alphabet[pos2]
        # Write each resulting line2 to the output file.
        fout.write(line2)

def PseudoRandom(fin, fout, encrypt_or_decrypt_choice, alphabet):
	# Read every line of the input file.
    for line1 in fin:
        # Alter each character of the line1, putting the result into line2.
        line2 = ""
        for c in line1:
            if c in alphabet:
            	# get a random offset for every character in each line
            	offset = random.randrange(1,len(alphabet))
            	if encrypt_or_decrypt_choice=='d':
        			offset = -offset
                pos1 = alphabet.find(c)
                pos2 = (pos1+offset)%len(alphabet)
                line2 += alphabet[pos2]
        # Write each resulting line2 to the output file.
        fout.write(line2)

def Substitution(fin, fout, encrypt_or_decrypt_choice, alphabet):
	alphabetList = []
	for char in alpabet:
		alphabetList.append(ch)
	random.shuffle(alphabetList)

	subAlph = "".join(alphabetList)

	for line1 in fin:
		line2 = ""
		for c in line1:
			if c in alphabet:
				pos = alphabet.find(c)
				line2 += subAlph[pos]
		fout.write(line2)

def main():
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?! \t\n\r"
	PrintDescription()
	
	while True:
		option = StartMenu()
		print "option is ", option
		if option == 'q':
			break
		method_option = MethodMenu()
		source_file = raw_input("What source file? ")
		dest_file = raw_input("What destination file? ")
		password = raw_input("What password? ")
		
		try:
			fin = open(source_file, "rb")
			fout = open(dest_file, "wb")
		except:
			print "Cannot read file"
			continue
		random.seed(password)
		
		if method_option == 'c':
			Caesarian(fin, fout, option, alphabet)
		elif method_option == 'p':
			PseudoRandom(fin, fout, option, alphabet)
		else:
			Substitution(fin, fout, option, alphabet)
		
		fin.close()
		fout.close()
		
	
	print "Good Bye"

main()
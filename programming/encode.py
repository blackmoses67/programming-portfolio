#Decoder

#save a message to a file

#encrypt the message to a separate file

#option to decrypt a file

#ord
#code number for a letter
def main():
	message = raw_input("Enter your message: ")
	plain_message = open("plain.txt", "w")
	plain_message.write(message)
	plain_message.close()

main()
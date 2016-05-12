# anagram program to find all the combinations of characters
# to help with scrabble

def ana(beg, end):
	if len(end) ==1:
		return [beg+end]

	f = []
	for i in range(len(end)):
		f += [beg+end[i]]
		f += ana(beg+end[i], end[:i]+end[i+1:])
	return f

def anagrams(letters):
	#get the words for dictionary
	dictionary = []
	try:
		dictionary_file = open("american-english.txt", "rb")
	except:
		print "Dictionary file not found."
		dictionary = None

	for line in dictionary_file:
		dictionary.append(line.strip())

	real_words = []
	words = ana("", letters)
	print "number of anagrams: ", len(words)

	for word in words:
		if len(word) > 1 and (word in dictionary):
			real_words.append(word)

	return real_words

def main():
	tiles = raw_input("Enter your tiles: ")
	words = anagrams(tiles)

	for word in words:
		print word

main()
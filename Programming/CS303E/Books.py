# File: Books.py

# Description: A program used to analyze and compare the vocabulary of two authors

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 11/30/15

# Date Last Modified: 11/30/15



# pulls punctuation out of each line; converts line to just words
def filter_string(st):

	# start with empty string
	s = ""

	# loop through each letter in string
	for i in range (len(st)):

		# loop to check if apostrophes are followed by "s"
		# if so, gets rid of apostrophe and "s" is seperated
		# ("s" will be removed later)
		if (st[i] == '\''):
			if (st[-1] == '\''):
				s += " "
			elif (st[i + 1] != 's'):
				s += st[i]
			else:
				s += ' '

		# if the character is not a letter, removes it
		elif (st[i] >='A') and (st[i] <= 'z'):
			s += st[i]
		else:
			s += ' '
	return s


# create word dictionary from the comprehensive word list
def create_word_dict ():

	in_file = open("./words.txt", "r")
	word_dict = {}

	for line in in_file:
		line = line.strip()
		line = line.lower()
		word_dict[line] = 1

	return word_dict	

# returns a dictionary of words and their frequencies
def getWordFreq (book):

	# open file for reading
	story = open("./" + book, 'r')

	# create all data sets
	word_set = set()
	word_dict = {}
	total_words = 0

	# iterate through each line of story
	for line in story:

		# pull data from each line and format it
		line = line.strip()
		line = filter_string(line)

		# temp_list still includes "s" values
		temp_list = line.split()
		word_list = []

		# loop to append word_list all elements that aren't "s"
		for i in range(len(temp_list)):
			if (temp_list[i] != "s"):
				word_list.append(temp_list[i])

		# runs through each element and adds values to data sets accordingly
		for word in word_list:
			word_set.add(word)
			total_words += 1

			if word in word_dict:
				word_dict[word] += 1

			else:
				word_dict[word] = 1

	# close file
	story.close()

	# import a comprehensive dictionary to see if certain words even exist
	comp_dict = create_word_dict()

	# create an empty list for all capital values
	caps = []

	# loop which runs through word_dict, searches for capital values,
	# and adds them to caps
	for key in word_dict:
		if (str(key) >= "A" and str(key) <= "Z"):
			caps.append(key)

	# loop which cleans word_dict of unneccessary capital values
	for el in caps:
		el_lower = el.lower()

		# if the lower exists as well, it adds all its values to 
		# lower key and gets rid of the upper
		if el_lower in word_dict:
			word_dict[el_lower] += word_dict[el]
			del word_dict[el]

		else:
			# if this is met, he used the word once and it was 
			# at the beginning of a sentence; convert to lower
			if el_lower in comp_dict:
				word_dict[el_lower] = 1
				del word_dict[el]

			# in this case, it's probably a name of an imaginary
			# place or person; get rid of it
			else:
				del word_dict[el]

	# return tuple consisting of all valuable information about vocab
	return (word_dict, total_words)



# compares the distinct words in two dictionaries
def wordComparison (data1, data2):

	# import data from data sets
	distinct_words1, tot_words1 = data1
	distinct_words2, tot_words2 = data2

	# find set differences
	author1_solo = set(distinct_words1) - set(distinct_words2)
	author2_solo = set(distinct_words2) - set(distinct_words1)

	# find number of distinct elements in each difference
	num_distinct1 = len(author1_solo)
	num_distinct2 = len(author2_solo)

	# add the frequency of the words in the difference for both
	sum_freq1 = 0
	for i in author1_solo:
		sum_freq1 += distinct_words1[i]

	sum_freq2 = 0
	for i in author2_solo:
		sum_freq2 += distinct_words2[i]

	# calculate relative frequecies
	rel_freq1 = 100 * (len(author1_solo) / sum_freq1)
	rel_freq2 = 100 * (len(author2_solo) / sum_freq2)

	# export data in a list
	compare1 = [num_distinct1, rel_freq1]
	compare2 = [num_distinct2, rel_freq2]


	return [compare1, compare2]



def main():

	#open books
	book1 = input("Enter name of first book: ")
	book2 = input("Enter name of second book: ")
	print ()

	#input authors
	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")
	print ()

	# pulls all data from tuple returned from getWordFreq function
	word_freq1, tot_words1 = getWordFreq(book1)
	word_freq2, tot_words2 = getWordFreq(book2)

	#uses data to make tuples
	authors = (author1, author2)
	tot_words = (tot_words1, tot_words2)
	word_freq = (word_freq1, word_freq2)

	# print loop using the tuples
	for i in range (2):
		print (authors[i])
		print ("Total distinct words = ", len(word_freq[i]))
		print ("Total words (including dupicates) = ", tot_words[i])
		print ("Ratio (% of total distinct words to total words) = ", 
			100 * (len(word_freq[i]) / tot_words[i]))
		print ()

	# import comparison list
	compare = wordComparison (getWordFreq(book1), getWordFreq(book2))

	print ("{} used {} words that Hardy did not use.".format
		(authors[0], compare[0][0]))
	print ("Relative frequency of words used by {} not in common with Hardy = {}".format
		(authors[0], compare[0][1]))
	print ()

	print ("{} used {} words that Dickens did not use.".format
		(authors[1], compare[1][0]))
	print ("Relative frequency of words used by {} not in common with Dickens = {}".format
		(authors[1], compare[1][1]))
	print ()



	

	

	

	



main()
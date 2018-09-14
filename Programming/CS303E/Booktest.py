# File: Books.py

# Description: A program used to analyze and compare the vocabulary of two authors

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 11/30/15

# Date Last Modified: 11/30/15

# create word dictionary from the comprehensive word list
def create_word_dict (book):
	
	story = open("./" + book, 'r')
	word_set = set()
	word_dict = {}
	total_words = 0

	for line in story:
		line = tale.readline()
		line = line.strip()
		line = line.lower()
		line = filter_string(line)
		word_list = line.split()

		for word in word_list:
			word_set.add(word)
			total_words += 1

			if word in word_dict:
				word_dict[word] += 1

			else:
				word_dict[word] = 1

	story.close()

	return word_dict

# removes punctuation marks from a string
def parseString (st):
	return None

# returns a dictionary of words and their frequencies
def getWordFreq (file):
	return None

# compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
	return None


def filter_string(st):
	s = ""
	for ch in st:
		if (ch >='a') and (ch <= 'z'):
			s += ch
		else:
			s += ' '
	return s

def main():

	book1 = input("Enter name of first book: ")
	book2 = input("Enter name of second book: ")

	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")

	wordFreq1 = getWordFreq(book1)
	wordFreq2 = getWordFreq(book2)

	wordComparison (author1, wordFreq1, author2, wordFreq2)

	

	statement = [word_set, word_dict, total_words, word_list]
	statement_s = ["word_set", "word_dict", "total_words", "word_list"]
	for i in range (4):
		print ("{:>15} = {}".format(statement_s[i], statement[i]))



main()
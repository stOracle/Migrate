# File: ISBN.py

# Description: An algorithm designed to test validity of ISBN numbers

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 10/21/2015

# Date Last Modified: 10/22/2015

# error checking function, returns 'valid' or 'invalid'
def check(mat_a, mat_s2): 

	# makes sure isbn is proper length
	if (len(mat_a) != 10):
		return "invalid"

	# makes sure the last character is either between 0 and 10;
	# at this point, any x's have been changed to tens
	if not ((mat_a[-1] >= 0) and (mat_a[-1] <= 10)):
		return "invalid"

	# makes sure the rest of the characters are digits
	for i in range (len(mat_a) - 1):
		if not ((mat_a[i] >= 0) and (mat_a[i] <= 9)):
			return "invalid"

	# checks if the last digit of s2 is divisible by 11
	if (mat_s2[-1] % 11 != 0):
		return "invalid"

	# if it passes all tests, return as valid
	return "valid"

def main():
	#open out reading file and the output writing file
	input_file = open ("./isbn.txt", "r")
	output_file = open ("isbnOut.txt", "w")

	# create a 2D matrix which will contain 2-element sets as elements with the form [isbn, Valid?]
	out = []

	# list of acceptable characters
	acceptable = ['0','1','2','3','4','5','6','7','8','9','10']

	# runs a procedure for each isbn in the file
	for line in input_file:

		# state our given isbn
		isbn = line

		#create a new variable for the edited isbn; strip and get rid of hyphens
		isbn_diff = isbn.strip()
		
		# create list to contain information about said isbn; 
		# given isbn will always be first element stripped
		condition = []
		condition.append(isbn_diff)

		isbn_diff = isbn_diff.replace("-", "")

		# create empty matrix to put all elements of isbn_diff into
		a = []

		# create matrices for our partial sums
		s1 = []
		s2 = []

		# loop to append matrix a with all elements in isbn_diff
		for i in range (len(isbn_diff)):
			a.append(isbn_diff[i])

		# loop to change all strings to integers; 
		# also changes 'x' or 'X' to a ten value
		for i in range (len(a)):

			# changes x's to 10's
			if (a[i] == 'x') or (a[i] == 'X'):
				a[i] = 10

			# if a character isn't a digit, it becomes a -1
			elif (acceptable.count(a[i]) == 0):
				a[i] = -1

			else: 
				a[i] = a[i]

			# changes all elements from str to int
			a[i] = int(a[i])

		# loop to build s1 using partial sums
		for i in range (len(a)):

			#for the first value, merely append it to s1; we don't add anything to it
			if (i == 0):
				s1.append(a[i])

			# for the rest of the values, append s1 with the value plus the last value in s1
			else:
				s1.append(a[i] + s1[i - 1])

		# loop to append s2 with partial sums of s1
		for i in range (len(s1)):

			# for first value, merely add it to s2
			if (i == 0):
				s2.append(s1[i])

			# for the rest of the values, append s2 with the value plus the last value in s2
			else:
				s2.append(s1[i] + s2[i - 1])

		# check if sum_s2 is divisible by eleven and append matrix accordingly
		condition.append(check(a, s2))

		# append our condition list to out
		out.append(condition)

	for i in range (len(out)):
		output_file.write("{:<13}  {}\n".format(out[i][0], out[i][1]))

	# close the files
	input_file.close()
	output_file.close()

main()
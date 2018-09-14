# File: Benford.py

# Description: A program to test Benford's law using the 2009 Census

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 11/23/15

# Date Last Modified: 11/23/15

#function to find first decimal of a number
def red(num):
	n = int(num)
	while (n > 9):
		n = n // 10
	return str(n)

def main():
	#establish dictionary
	pop_freq = {}
	for i in range (1, 10):
		pop_freq[str(i)] = 0

	#open file
	in_file = open("./Census_2009.txt", "r")

	#get rid of header
	header = in_file.readline()

	#variable to keep count of how many numbers
	tot_val = 0

	#iterate for every line
	for line in in_file:
		line = line.strip()
		pop_data = line.split()

		#pull out number in interest
		pop_num = pop_data[-1]

		#use function to reduce number to first digit
		value = red(pop_num)

		#add a value to the key for value
		pop_freq[value] += 1

		#for every iteration, add 1 to keep track of how many numbers
		tot_val += 1

	#print loop
	for i in range (10):

		#first line is header
		if (i == 0):
			print ("{:<8}{:<8}{}".format("Digit", "Count", "%"))

		#other lines are dependent on key
		else:
			print ("{:<8}{:<8}{:.1f}".format
				(i, pop_freq[str(i)], 100 * (pop_freq[str(i)] / tot_val)))

	#close file
	in_file.close()



main()
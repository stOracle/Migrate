# File: FibonacciBase.py

# Description: A program to convert a number base ten to base fibonacci

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 11/9/15

# Date Last Modified: 11/9/15

# function which creates a list of fibonacci numbers all lower than or equal to the number
def fib_list (n):

	# start the fib list with the first two elements
	fib = [1, 2]

	# loop which appends the fib list with all fib elements less than or equal to number
	while (fib[-1] + fib[-2] <= n):
		fib.append(fib[-1] + fib[-2])

	# reverse the list to make it easier to work with
	fib.reverse()

	return fib

# function which takes num and returns a string of its binary representation of fib elements
def convert_fib_base (num):

	# first, make the list we use
	fib = fib_list (num)

	# start num_fib as empty string
	num_fib = ""

	# loop which runs through every element of fib 
	for i in range (len(fib)):

		# when fib[i] is less than the number, add a "1" to num_fib and subtract the number
		if num >= fib[i]:
			num_fib += "1"
			num -= fib[i]

		# if the number is too big to subtract, it will add a "0" and not subtract
		else:
			num_fib += "0"

	return num_fib

def main():
	# call for a number
	num = int(input("Enter a number: "))

	# print the results
	print (num, "=", convert_fib_base (num) + " (fib)")


main()
# ___________________________HOMEWORK 2: Problem 3_______________________________
# -------------------------------------------------------------------------------
# Implement the Bisection algorithm. Modify the algorithm such that your program 
#   outputs the iteration number for each iteration of the algorithm.
#   Find the root of f(x) = e^x - x^2 + 3x - 2 within an error of 10^-8.
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

import math
# -------------------------------------------------------------------------------
# find_iter function finds the amount of iterations necessary to contain 
# error within the parameter
# -------------------------------------------------------------------------------

def find_iter(a, b, error):

	k = 0
	while (abs(b - a) / 2**k > error):
		k += 1
	return k

# -------------------------------------------------------------------------------
# function that evalues f(x) at value x
# -------------------------------------------------------------------------------

def f(x):
	value = (math.exp(x) - x**2 + 3*x - 2)
	return value

# -------------------------------------------------------------------------------


def main():

	print("\n\n{:^70}".format("Homework 2: Problem 3"))
	print("{:-^70}".format(""))
	print("{:^70}".format("After entering the domain and allotted error, all output data will"))
	print("{:^70}".format("be rounded to 4 decimal scientific notation."))
	print("{:^70}".format("The program does not round in calculations"))
	print("{:-^70}".format(""))

	a = int(input("\n\n{:>34}: ".format("Enter the start of the domain")))
	b = int(input("{:>34}: ".format("Enter the end of the domain")))
	error = eval(input("{:>34}: ".format("Enter the error (e.g., 10**-8)")))
	print ()

	num_it = find_iter(a, b, error)
	k = 0

	for i in range (num_it):
		k += 1
		c = .5 * (b + a)

		print ("{:>33} = {}".format("Iteration number", k))
		print ("{:>33} = {:.3e}".format("Approximate root (c)", c))
		print ("{:>33} = {:.3e}".format("f(c)", f(c)))
		print ()
		
		if (f(c) == 0):
			print ("The root of f(x) is x = {}.".format(c))
			break
		elif (f(c) * f(a) < 0):
			b = c
		else:
			a = c

main()
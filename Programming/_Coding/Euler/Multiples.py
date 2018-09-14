#  File: multiples.py

#  Author: Stephen Rauner

#  Date Created: 4/7/17

#  Date Last Modified: 4/7/17

# Problem Description: 
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.'''

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def multiples(n):
	valid = []
	count = 1
	while (count < n):
		if (count % 3 == 0) or (count % 5 == 0):
			valid.append(count)
		count += 1
	print()
	print(valid)
	print()
	tally = 0
	for el in valid:
		tally += el

	return tally

def main():
	num = int(input("Enter number: "))
	print(multiples(num))

main()
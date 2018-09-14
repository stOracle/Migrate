# File: CreditCard.py

# Description: A program to test the validity of a user-entered credit card

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 10/25/2015

# Date Last Modified: 10/27/2015

# This function checks if a credit card number is valid
def is_valid (digit):

	# Start with an empty matrix
	digit1 = []

	# Check if the cc number is the correct length
	if ((len(digit) < 15) or (len(digit) > 16)):
		return "Not a 15 or 16-digit number"

	else:

		# loop to append digit1 after Luhn's test
		for i in range (len(digit)):
			if (i % 2 == 1):
				digit1.append(digit[i])
			else:
				digit1.append(digit[i] * 2)
				if (digit1[i] > 9):
					num = 0
					num += digit1[i] % 10
					digit1[i] = digit1[i] // 10
					num += digit1[i]
					digit1[i] = num

		# Algorithm to sum all elements of digit1
		sum_d = 0
		for i in range (len(digit1)):
			sum_d += digit1[i]

		# Test if Luhn's test passes
		if (sum_d % 10 == 0):
			return True
		else:
			return "Invalid credit card number"


# This function returns the type of credit card; uses string of cc num
def cc_type (cc_num):

	if (cc_num[:2] == "34") or (cc_num[:2] == "37"):
		return "American Express"

	elif ((cc_num[:4] == "6011") or (cc_num[:3] == "644") or (cc_num[:2] == "65")):
		return "Discover"

	elif ((int(cc_num[:2]) >= 50) and (int(cc_num[:2]) <= 55)):
		return "MasterCard"

	elif (cc_num[0] == "4"):
		return "Visa"

	else:
		return ""





def main():

	# Prompt user to enter card number; enters as string
	card = str(input("Enter 15 or 16-digit credit card number:"))

	# Make an empty list to append
	digit = []

	# Appending digit with every 'letter' of the string of card 
	# 	and changing to integers
	for i in range (len(card)):
		digit.append(card[i])
		digit[i] = int(digit[i])

	# Only if digit passes all validity tests will it move on to 
	#	formatting in this step
	if (is_valid(digit) == True):
		print()
		print ("Valid {} credit card number".format(cc_type(card)))

	# For all cases where is_valid is false, print the reason it's invalid;
	#	(this is built in to the function)
	else:
		print ()
		print (is_valid(digit))

main()


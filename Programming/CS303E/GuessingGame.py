# File: GuessingGame.py

# Description: A game which guesses the users number (between 1 and 100)

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 11/2/15

# Date Last Modified: 11/2/15

def main():

	# Start with the introduction
	print ("\nGuessing Game")
	print ("\nThink of a number between 1 and 100 inclusive.")
	print ("And I will guess what it is in 7 tries or less.")

	# begin is if the user wants to play or not
	begin = str(input("\nAre you ready? (y/n): "))

	# error checking
	while (begin != 'y') and (begin != 'n'):
		begin = str(input("\nAre you ready? (y/n): "))

	# once user enters a 'y', the guessing game will proceed
	if (begin == 'y'):

		# acc stands for accuracy; i set it to 3 arbitrarily.
		# this is what will change to -1, 0, or 1 based on accuracy.
		acc = int (3)

		# start high and low at initial range - they will change later
		high = 100
		low = 1
		mid = (high + low) // 2

		# count keeps track of what guess the game is on
		count = 1

		# loop to continue the game until the count is too high
		# or the user enters a 0 value for acc.
		while ((acc != 0) and (count < 8)):

			# formatted string to reveal the program's guess, 
			# plus an input string to adjust acc
			print ("\nGuess {} : The number you thought was {}".format (count, mid))
			acc = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
			
			# error checking for acc - repeats the last two steps 
			# when the user doesn't enter the right number
			while ((acc > 1) or (acc < -1)):
				print ("\nGuess {} : The number you thought was {}".format (count, mid))
				acc = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))

			# if our number is too low, we raise the low value and adjust the mid		
			if (acc == -1):
				low = mid + 1
				mid = (high + low) // 2

			# if our number is too high, we reaise the high value and adjust the mid
			elif (acc == 1):
				high = mid -1
				mid = (high + low) // 2

			# adds one to the count to represent the next guess
			count += 1

		# ff the while loop was exited because of the count, then it shows the error message
		if ((count >= 8) and (acc != 0)):
			print ("\nEither you guessed a number out of range or you had an incorrect entry.")

		# this condition is only met when the user enters zero before the 8th guess
		else:
			print ("\nThank you for playing the Guessing Game.")

	# if user enters 'n', the game is over
	else:
		print ("\nBye")






main()
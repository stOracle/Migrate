# File: 

# Description: Deal.py

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 10/6/15

# Date Last Modified: 10/7/15

import math
import random

def main():

	#prompt user to enter amount of trials to iterate
	num_trials = int(input("Enter number of times you want to play:"))

	#define our tally keeper for number of wins
	sum_wins = 0

	#print first line of table
	print ("\n{:^11}{:^11}{:^11}{:^11}".format("Prize", "Guess", "View", "New Guess"))

	#a loop to play through the game num times
	for game in range(num_trials):
		prize = random.randint(1,3)
		guess = random.randint(1,3)

		#define view with a conditional parameter
		view = 1
		while ((view == prize) or (view == guess)):
			view += 1

		#define newGuess with a conditional parameter
		newGuess = 1
		while ((newGuess == view) or (newGuess == guess)):
			newGuess += 1

		#conditional to tally the wins during the playthroughs
		if (newGuess == prize):
			sum_wins += 1

		#print for each iteration
		print("{:^11}{:^11}{:^11}{:^11}".format(prize, guess, view, newGuess))

	#calulate probability given num trials
	prob_switch = sum_wins / num_trials
	prob_stay = 1 - prob_switch	

	print("\nProbability of winning if you switch = {:.2f}".format(prob_switch))
	print("Probability of winning if you do not switch = {:.2f}".format(prob_stay))

main()
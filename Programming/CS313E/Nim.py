#  File: Nim.py

#  Description: An algorithm to help approximate the optimal first move in Nim

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 2/1/16

#  Date Last Modified: 2/3/16

# --------------------------------------------------------------------------------

# function which takes all data from .txt file and makes a 2D list out of it
def extract():

	# open file and read first line to assign num_games
	in_file = open("./nim.txt")
	num_games = int(in_file.readline())

	# loop to create a 2D list containing all the .txt file's information
	# heaps[i][j] represents the jth heap in the ith game
	heaps = []
	for i in range(num_games):

		heap = in_file.readline()
		heap = heap.split()

		# loop to convert values to int
		for i in range(len(heap)):
			heap[i] = int(heap[i])
		heaps.append(heap)

	in_file.close()
	return heaps

# --------------------------------------------------------------------------------

# finds the Nim Sum of all elements of list a
# X = nim_sum(a) = a[0]^a[1]^...^a[N]
def nim_sum (a):

	nim_sum = a[0]
	for i in range (len(a) - 1):
		nim_sum = nim_sum ^ a[i + 1]
	return nim_sum

# --------------------------------------------------------------------------------

# given a list of heaps, ind_nSum(a) returns a list of the individual Nim_sums 
# returns [p1, p2, ..., pN]
def ind_nSum(a):

	pqr = []
	X = nim_sum(a)
	for el in a:
		ind_nim_sum = el^X
		pqr.append(ind_nim_sum)
	return pqr

# --------------------------------------------------------------------------------

def main():

	print()

	# construct the 2D list of data of all games we will play
	heaps = extract()

	#iterate through every game
	for game in heaps:
		# checks if game will be lost before applying algorithm		
		if (nim_sum(game) == 0):
			print ("Lose Game")
		else:
			# create list of individual Nim Sums
			pqr = ind_nSum(game)

			# loop looking for the first heap where P[i] < game[i]
			for i in range(len(game)):
				if (game[i] > pqr[i]):
					move = game[i] - pqr[i]
					print ("Remove {} counters from Heap {}".format(move, i + 1))
					break


main()

# --------------------------------------------------------------------------------
# Stephen Rauner
#  File: MagicSquare.py

#  Description: A program to populate an NxN matrix with all numbers in [1,N*N]
#               s.t. all rows, columns, and diagnols add to the same number. 

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 2/3/15

#  Date Last Modified: 2/7/15

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# make an empty (N + 1) x (N + 1) matrix; populate with zeroes;
# the extra row and column are buffers to aid the process.
def dummy(dim):
	blank = []
	for i in range (dim + 1):
		row = []
		for j in range (dim + 1):
			row.append(0)
		blank.append(row)
	return blank

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# populate a 2D list with numbers from 1 to N*N
def makeSquare(dim):
	# create an empty matrix
	edit = dummy(dim)

	# spot is an index for where in edit we will place the number;
	# it's initial value is where we start the process.
	spot = [dim - 1, int((dim - 1) * .5)]
	edit[spot[0]][spot[1]] = 1

	# a while loop which iterates until we have filled the matrix.
	count = 2
	while (count <= dim ** 2):

		# every DIMth iteration, we run into a occupied cell and
		# must jump up a row.
		if (count % dim == 1):
			spot[0] -= 1
			edit[spot[0]][spot[1]] = count

		# for all other iterations, we move right and left.
		else:
			spot[0] += 1
			spot[1] += 1

			# if spot points to the 'buffer' row, adjust accordingly.
			if (spot[0] == dim):
				spot[0] -= dim
			if (spot[1] == dim):
				spot[1] -= dim
			edit[spot[0]][spot[1]] = count

		count += 1

	# shave is what is returned; it is edit after we 'shave' 
	# off the buffer row and column.
	shave = []
	for i in range (len(edit) - 1):
		row = []
		for j in range (len(edit) - 1):
			row.append(edit[i][j])
		shave.append(row)

	return shave

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# print the magic square in a neat format where the numbers are right justified
def printSquare(m, dim):
	print ("\nHere is a {} x {} magic square: \n".format(dim, dim))

	# formatting loop
	for i in range (dim):
		form = ""
		for j in range (dim):
			form += "{:>4}".format(m[i][j])
		print(form)

	print()
	return None

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# function to check sums to see if the matrix is 'magic'
def checkSquare (m):
	dim = len(m)

	# set our target value (based on formula)
	target = int(.5 * (dim ** 3 + dim))

	# create a list of all the sums we will test.
	sums = []

	# first, we calculate the sum of the rows and append them to sums
	for i in range(dim):
		sum_row = 0
		for j in range(dim):
			sum_row += m[i][j]
		sums.append(sum_row)

	# repeat the same for the columns
	for j in range(dim):
		sum_column = 0
		for i in range(dim):
			sum_column += m[i][j]
		sums.append(sum_column)

	# repeat the same for the diagonal starting at (0,0)
	sum_diag_00 = 0
	for i in range(dim):
		sum_diag_00 += m[i][i]
	sums.append(sum_diag_00)

	# repeat the same for the diagonal starting at (dim-1,0)
	sum_diag_dim0 = 0
	for i in range(dim):
		sum_diag_dim0 += m[(dim - 1) - i][i]
	sums.append(sum_diag_dim0)
	
	# this tests every element in sum to make sure they all add to
	# the desired target. If they don't, we only return an error message.
	for el in sums:
		if (el != target):
			print ("Code is broken.")
			return None

	# if we pass the loop, everything equals target and we can
	# print the following.
	print("Sum of row = ", target)
	print("Sum of column = ", target)
	print("Sum diagonal (UL to LR) = ", target)
	print("Sum diagonal (UR to LL) = ", target)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def main():

	# prompt the user to enter an odd number 3 or greater
	dim = int(input("\nPlease enter an odd number: "))
	while ((dim % 2 == 0) or (dim < 3)):
		dim = int(input("Please enter an odd number: "))

	# create the magic square
	magic = makeSquare(dim)

	# print the magic square
	printSquare(magic, dim)

	# Verify that it is a magic square
	checkSquare(magic)

main()
#  File: TestSparseMatrix.py

#  Description: Sparse matrix representation has a single linked list
#               having the row, column, and non-zero data in each link

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 4/13/16

#  Date Last Modified: 4/14/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Link (object):

# /////////////////////////////////////////////////////////////////////////////////

	def __init__ (self, row, col, data, next = None):

		self.row = row
		self.col = col
		self.data = data
		self.next = None

# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):

		return str(self.data)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class SparseMatrix (object):

# /////////////////////////////////////////////////////////////////////////////////

	def __init__ (self, row = 0, col = 0):

		self.num_rows = row
		self.num_cols = col
		self.matrix = None

# /////////////////////////////////////////////////////////////////////////////////

	# setElement() performs an assignment operation a[i][j] = value
	# if value is 0 the link (if it exists) is deleted
	# if value is non-zero then the current value is updated (if a 
	# link already exists) or a new link is added
	def setElement (self, row, col, data):

		if (data == 0):
			self.deleteLink (row, col)
		else:
			self.insertLink (row, col, data)

# /////////////////////////////////////////////////////////////////////////////////

	def insertLink (self, row, col, data):

		if (data == 0):
			return

		newLink = Link (row, col, data)

		if (self.matrix == None):
			self.matrix = newLink
			return

		previous = self.matrix
		current = self.matrix

		while ((current != None) and (current.row < row)):
			previous = current
			current = current.next

		# if the row is missing
		if ((current != None) and (current.row > row)):
			previous.next = newLink
			newLink.next = current
			return

		# on the row, search by column
		while ((current != None) and (current.col < col)):
			previous = current
			current = current.next

		# if link is already there do not insert but reset data
		if ((current != None) and (current.row == row) and (current.col == col)):
			current.data = data
			return

		# now insert newLink
		previous.next = newLink
		newLink.next = current

# /////////////////////////////////////////////////////////////////////////////////

	# deletes and returns a Link if it is there or None otherwise
	def deleteLink (self, row, col):

		previous = self.matrix
		current = self.matrix

		# can't delete nothing
		if (current == None):
			return
		# when the spot is the first link, set the pointer to the next element
		elif ((current.row == row) and (current.col == col)):
			self.matrix = current.next
			return
		# otherwise, hone in by first getting the right row
		while ((current != None) and (current.row < row)):
			previous = current
			current = current.next

		# if the row in question isn't there, return
		if ((current != None) and (current.row > row)):
			return
		# Now hone in on the column
		while ((current != None) and (current.col < col)):
			previous = current
			current = current.next
		# if the col in question isn't there, return
		if ((current != None) and (current.col > col)):
			return
		# yay! We finally found it. Delete it
		elif ((current != None) and (current.row == row) and (current.col == col)):
			previous.next = current.next

# /////////////////////////////////////////////////////////////////////////////////

	# return a row of the sparse matrix
	def getRow (self, row_num):

		# create a blank list
		a = []

		# search for the row
		current = self.matrix
		if (current == None):
			return a

		while ((current != None) and (current.row < row_num)):
			current = current.next

		if ((current != None) and (current.row > row_num)):
			for i in range (self.num_cols):
				a.append(0)
			return a

		if ((current != None) and (current.row == row_num)):
			for j in range (self.num_cols):
				if (current.col == j):
					a.append (current.data)
					current = current.next
				else:
					a.append(0)

		return a

# /////////////////////////////////////////////////////////////////////////////////

	# return a column of the sparse matrix
	def getCol (self, col_num):

		# create blank list
		b = []

		# my process is to run through each row and 'pick' out the row'th element
		current = self.matrix
		for i in range (self.num_rows):

			# failsafe
			if (current == None):
				break
			# this makes sure i matches current.row
			if (current.row > i):
				continue

			# for every element on the ith row
			while (current != None) and (current.row == i):

				# when we have nothing, get out
				if (current == None):
					break

				# this is for when there is data in the spot
				if (current.col == col_num):
					b.append(current.data)

				# this is for when we are at last element and we 
				# haven't gotten to the row yet
				elif (current.next == None):
					if (current.col < col_num):
						b.append(0)
						break
					else:
						break
				
				# this is for when the row has a 0 in the spot
				elif (current.col < col_num) and (current.next.col > col_num):
					b.append(0)
				elif ((current.col > col_num) and (current.next.col > col_num)
						and (current.next.row > current.row)):
					b.append(0)
				elif ((current.col < col_num) and 
					((current.next.col > col_num) or (current.next.col == 0))):
					b.append(0)

				current = current.next

		return b

# /////////////////////////////////////////////////////////////////////////////////

	# add two sparse matrices
	def __add__ (self, other):

		if ((self.num_rows != other.num_rows) or (self.num_cols != other.num_cols)):
			return None

		sCurrent = self.matrix
		oCurrent = other.matrix		

		new = SparseMatrix(self.num_rows, self.num_cols)

		while True:

			# break the loop when both are exhausted
			if ((sCurrent == None) and (oCurrent == None)):
				break

			# The next two are to combat when one has data where the
			# other has a 0, or is exhausted
			if ((oCurrent == None) or (sCurrent.row < oCurrent.row)):
				new.insertLink(sCurrent.row, sCurrent.col, sCurrent.data)
				sCurrent = sCurrent.next
			elif ((sCurrent == None) or (sCurrent.row > oCurrent.row)):
				new.insertLink(oCurrent.row, oCurrent.col, oCurrent.data)
				oCurrent = oCurrent.next

			# this is for when they have the same row
			else:
				# the next two are to combat when one has data where the
				# other has a 0
				if (sCurrent.col < oCurrent.col):
					new.insertLink(sCurrent.row, sCurrent.col, sCurrent.data)
					sCurrent = sCurrent.next
				elif (sCurrent.col > oCurrent.col):
					new.insertLink(oCurrent.row, oCurrent.col, oCurrent.data)
					oCurrent = oCurrent.next

				# finally! They have the same row and col. Add them
				else:
					new.insertLink(sCurrent.row, 
						sCurrent.col, sCurrent.data + oCurrent.data)
					sCurrent = sCurrent.next
					oCurrent = oCurrent.next

		return new

# /////////////////////////////////////////////////////////////////////////////////

	# multiply two sparse matrices
	def __mul__ (self, other):

		# check if it's possible
		if (self.num_cols != other.num_rows):
			return None

		# create new matrix
		new = SparseMatrix(self.num_rows, other.num_cols)

		# hold is to hold the data before I use setElement to make it a list
		hold = []

		# for each row, pull the row we are multiplying with
		for i in range (new.num_rows):
			new_row = []
			row = self.getRow(i)

			# for each column, pull the appropriate column
			for j in range (new.num_cols):
				sum_n = 0
				col = other.getCol(j)

				# multiply throughout the row and column
				for k in range(other.num_rows):
					sum_n += row[k] * col[k]

				new_row.append(sum_n)
			hold.append(new_row)

		# take the info from the 2D list we made and 
		# convert it into a linked list
		for i in range (len(hold)):
			for j in range (len(hold[0])):
				new.setElement(i, j, hold[i][j])

		return new

# /////////////////////////////////////////////////////////////////////////////////

	# return a string representation of the matrix
	def __str__ (self):

		s = "  "
		current = self.matrix

		# if the matrix is empty return blank string
		if (current == None):
			return s

		for i in range (self.num_rows):
			for j in range (self.num_cols):
				if ((current != None) and (current.row == i) and (current.col == j)):
					s += "{:>5}".format(current.data)
					current = current.next
				else:
					s += "{:>5}".format(0)

			s += "\n  "

		return s

# /////////////////////////////////////////////////////////////////////////////////

	# this is a special print function to lay out the info for 
	# every link in the list.
	def specPrint(self):

		prev = self.matrix
		current = self.matrix

		if (current == None):
			return

		print("{:^5}{:^5}{:^5}".format("Row", "Col", "Data"))
		print("-"*15)

		while (current != None):
			print ("{:^5}{:^5}{:^5}".format(current.row, current.col, current.data))
			current = current.next

		print()

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def readMatrix (inFile):

	line = inFile.readline().rstrip("\n").split()
	row = int(line[0])
	col = int(line[1])
	mat = SparseMatrix (row, col)

	for i in range (row):
		line = inFile.readline().rstrip("\n").split()
		for j in range (col):
			elt = int(line[j])
			if (elt != 0):
				mat.insertLink(i, j, elt)

	# dummy line
	line = inFile.readline()

	return mat

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():

	inFile = open("matrix.txt", "r")

	title1 = "Test Matrix Addition"
	print("\n" + title1)
	print("-" * len(title1) + "\n")

	# populate the matrices
	matA = readMatrix(inFile)
	print(" Matrix A:\n")
	print(matA)
	matB = readMatrix(inFile)
	print(" Matrix B:\n")
	print(matB)

	# add the matrices
	matC = matA + matB
	print(" Matrix A + Matrix B:\n")
	print(matC)

	title2 = "Test Matrix Multiplication"
	print("\n" + title2)
	print("-" * len(title2) + "\n")

	# populate the matrices
	matP = readMatrix (inFile)
	print(" Matrix P:\n")
	print (matP)
	matQ = readMatrix (inFile)
	print(" Matrix Q:\n")
	print (matQ)

	# multiply the matrices
	matR = matP * matQ
	print(" Matrix P * Matrix Q:\n")
	print(matR)

	title3 = "Test setting a Zero Element to a Non-Zero Value"
	print("\n" + title3)
	print("-" * len(title3) + "\n")

	print(" Matrix A:\n")
	print(matA)
	matA.setElement (1, 1, 5)
	print(" Matrix A after setElement(1, 1, 5):\n")
	print (matA)

	title4 = "Test setting a Non-Zero Element to Zero"
	print("\n" + title4)
	print("-" * len(title4) + "\n")

	print(" Matrix A:\n")
	print(matA)
	matA.setElement (1, 1, 0)
	print(" Matrix A after setElement(1, 1, 0):\n")
	print (matA)

	title5 = "Test Getting a Row"
	print("\n" + title5)
	print("-" * len(title5) + "\n")

	print(" Matrix P:\n")
	print(matP)
	row = matP.getRow(1)
	print(" Row 1 of Matrix P:\n")
	print ("{:>7}{}".format("", row))

	title6 = "Test Getting a Column"
	print("\n" + title6)
	print("-" * len(title6) + "\n")

	print(" Matrix Q:\n")
	print(matQ)
	col = matQ.getCol(0)
	print(" Column 0 of Matrix Q:\n")
	print ("{:>7}{}".format("", col))

	# close the file
	inFile.close()

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

main()
#  File: TestDenseMatrix.py

#  Description: Matrix is represented as 2-D list

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 4/13/16

#  Date Last Modified: 4/14/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Matrix (object):

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

	def __init__ (self, row = 0, col = 0):

		self.matrix = []
		self.row = row
		self.col = col

# /////////////////////////////////////////////////////////////////////////////////

	def __add__ (self, other):

		if (self.row != other.row) or (self.col != other.col):
			return None

		new_matrix = Matrix(self.row, self.col)

		for i in range (self.row):
			new_row = []
			for j in range (self.col):
				new_row.append(self.matrix[i][j] + other.matrix[i][j])
			new_matrix.matrix.append(new_row)

		return new_matrix

# /////////////////////////////////////////////////////////////////////////////////

	def __mul__ (self,other):

		if (self.col != other.row):
			return None

		mat = Matrix(self.row, other.col)

		for i in range (self.row):
			new_row = []
			for j in range (other.col):
				sum_n = 0
				for k in range (other.row):
					sum_n += self.matrix[i][k] * other.matrix[k][j]
				new_row.append(sum_n)
			mat.matrix.append(new_row)

		return mat

# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):

		s = ""

		for i in range (self.row):
			for j in range (self.col):
				if (j == 0):
					s += "  {:>5}".format(str(self.matrix[i][j]))
				else:
					s += "{:>5}".format(str(self.matrix[i][j]))
			s = s + "\n"

		return s

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def readMatrix(inFile):

	line = inFile.readline()
	line = line.strip()
	line = line.split()
	row = int(line[0])
	col = int(line[1])

	mat = Matrix (row, col)

	for i in range (row):
		line = inFile.readline()
		line = line.strip()
		line = line.split()
		for j in range (col):
			line[j] = int(line[j])
		mat.matrix.append(line)

	# dummy read
	line = inFile.readline()

	return mat

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():

	# open file
	inFile = open("matrix.txt", "r")

	print("\nTest Matrix Addition")
	print("-" * 20 + "\n")

	# populate the matrices
	matA = readMatrix(inFile)
	print("Matrix A:\n")
	print(matA)
	matB = readMatrix(inFile)
	print("Matrix B:\n")
	print(matB)

	# add the matrices
	matC = matA + matB
	print("Matrix A + Matrix B:\n")
	print(matC)

	print("\nTest Matrix Multiplication")
	print("-" * 26 + "\n")

	# populate the matrices
	matP = readMatrix (inFile)
	print ("Matrix P:\n")
	print (matP)
	matQ = readMatrix (inFile)
	print ("Matrix Q:\n")
	print (matQ)

	# multiply the matrices
	matR = matP * matQ
	print("Matrix P * Matrix Q:\n")
	print(matR)

	# close the file
	inFile.close()

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

main()
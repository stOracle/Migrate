class Matrix (object):
	def __init__(self, row = 0, col = 0):
		self.matrix = []
		self.row = 0
		self.col = 0
	def __add__(self, other):
		if (self.row != other.row) or (self.col != other.col):
			return None

		mat = Matrix (self.row, self.col)

		for i in range (self.row):
			new_row = []
			for j in range (self.col):
				new_row.append(self.matrix[i][j] + other.matrix[i][j])
			mat.matrix.append(new_row)

		return mat

	def __mul__ (self, other):
		if (self.col != other.row):
			return None

		mat = Matrix(self.row, other.col)

		for i in range(self.row):
			new_row = []
			for j in range (other.col):
				sum_n = 0
				for k in range (other.row):
					sum_n += self.matrix[i][k] * other.matrix[k][j]
				new_row.append(sum_n)

			mat.matrix.append(new_row)

	# NOW DO IT WITH LINKEDLIST

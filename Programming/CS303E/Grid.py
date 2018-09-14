# File: Grid.py

# Description: An algorithm to find the greatest product of 4 adjacent members of an NxN matrix

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 10/27/15

# Date Last Modified: 10/27/15

#finds the transpose matrix of b
def transpose (b):
	t = []
	for j in range (len(b[0])):
		g = []
		for i in range (len(b)):
			g.append (b[i][j])
		t.append(g)
	return t

# simplifies a 2-D list by converting each 
# list-element to the max of said list
def simplify (b):
	sim = []
	for i in range (len(b)):
		max_row = b[i][0]
		for j in range (len(b[0])):
			if (b[i][j] > max_row):
				max_row = b[i][j]
		sim.append(max_row)

	max_elem = sim[0]
	for j in range (len(sim)):
		if (sim[j] > max_elem):
			max_elem = sim[j]

	return max_elem

# prints the product of diagonal going left to right

def slash (b):

	slash = []

	for col in range (len(b) - 3):
		col = []

		i_shift = 0

		for i in range (len(b) - 3):
			j_shift = 0
			prod = 1
		for j in range (len(b) - 3):
			prod = prod * b[i + j][i + j]
		count += 1
		row.append (prod)
	slash.append (row)

	print (slash[0])



	#specifies a row of grid
	#for r in range (len(b) - 3):
		#row = []
		#count = 0

		#specifies an element in the ith row
		#for i in range (len(b) - 3):

			#starts the product at 1
			#prod = 1
			#counter = 0

			#for j in range (4):
				#prod = prod * b[i + counter][i + count]
				#counter += 1
			#row.append (prod)
			#count += 1
		#slash.append(row)
		#count += 1
	#for k in range (len(slash)):
	#print (slash[0])
	#return slash

# gives 2-D list: horizontal = row[product @ element] calculating the product from a spot from a row, in the horizontal direction.
def hor (b):

	hor = []

	#iterates for every row in matrix
	for i in range (len(b)):
		row = []

		#loop to find 4-way product for each element in 1 row
		for elem in range (len(b) - 3):

			#start at 1 to find product for each element
			prod = 1

			#calculates the prodcut of 4 consecutive elements
			for j in range (elem, elem + 4):
				prod = prod * b[i][j]

			row.append(prod)

		hor.append(row)

	return hor


def main():

	#open file for reading
	in_file = open ("./grid.txt", "r")

	#setting variable 'dim' to equal the first line (i.e., the dimension)
	dim = in_file.readline()
	dim = dim.strip()
	dim = int (dim)

	#starting the 2D list we will import all the rows into
	grid = []

	for i in range (dim):
		line = in_file.readline()
		line = line.strip()
		nums = line.split()
		for j in range (dim):
			nums[j] = int (nums[j])

		grid.append (nums)

	grid_trans = grid[:]
	grid_trans = transpose(grid_trans)
	grid_reverse = grid[:]
	grid_reverse.reverse()

	#the master list will contain the max value from each method of searching
	master = []

	hor_list = hor (grid)
	hor_max = simplify (hor_list)
	master.append (hor_max)

	vert_list = hor (grid_trans)
	vert_max = simplify (vert_list)
	master.append (vert_max)

	slash_b_list = slash(grid)
	slash_b_max = simplify (slash_b_list)
	master.append(slash_b_max)

	print (slash_b_max)

	#slash_f_list = slash_f (grid)
	#slash_f_max = simplify (slash_f_list)
	#master.append(slash_f_max)

	max_product = master[0]
	for i in range (len(master)):
		if (master[i] > max_product):
			max_product = master[i]

	#for i in range (len(hor_list)):
		#print (hor_list[i])

	#print (simplify(hor_list))

	#for i in range (len(hor_sim)):
		#print ("Max of row {} = {}".format(i + 1, hor_sim[i]))
		#for j in range (len(hori[0])):
			#print ("hor[{}]: {}".format(i, hori[0]))



main()
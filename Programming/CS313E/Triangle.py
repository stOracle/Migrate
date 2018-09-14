#  File: Triangle.py

#  Description: A program to use different algorithm methods to solve the 
#				triangle path problem

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 4/18/16

#  Date Last Modified: 4/18/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

# subset collector
def subsets (a, b, idx):

	hi = len(a)
	path_list = []

	if (lo == hi):
		path_list.append(b)
		return path_list

	else:
		c = b[:]
		b.append(a[lo])
		subsets (a, c, lo + 1)
		subsets (a, b, lo + 1)

# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):

	path_list = subsets(grid, [], 0)
	print(path_list)

	return

# /////////////////////////////////////////////////////////////////////////////////

# returns the greatest path sum using greedy approach
def greedy (grid):

	gridSum = grid[0][0]
	idx = 0
	path = [gridSum]
	for i in range (1, len(grid)):
		a = grid[i][idx]
		b = grid[i][idx + 1]
		if (a > b):
			gridSum += a
			path.append(a)
		else:
			gridSum += b
			path.append(b)
			idx = idx + 1

	return [gridSum, path]

# /////////////////////////////////////////////////////////////////////////////////

# returns the greatest path sum using recursion
def rec_search (grid):

	return

# /////////////////////////////////////////////////////////////////////////////////

# returns the greatest path sum using dynamic programming
def dynamic_prog (grid):

	return

# /////////////////////////////////////////////////////////////////////////////////

# reads the file and returns a 2D list that represents the triangle
def readFile ():

	inFile = open("triangle.txt", "r")
	numLines = int(inFile.readline())
	triangle = []

	for i in range (numLines):
		line = inFile.readline().strip().split()
		for i in range (len(line)):
			line[i] = int(line[i])
		triangle.append(line)

	inFile.close()

	return triangle

# /////////////////////////////////////////////////////////////////////////////////

def main():

	# read triangle from file
	triangle = readFile()
	for el in triangle:
		print(el)

	# output greatest path from exhaustive search
	path = exhaustive_search(triangle)
	print (path)

	# output greatest path from greedy approach
	greedyAns = greedy(triangle)

	# output greatest path from recursive approach

	# output greatest path from dynamic approach

main()
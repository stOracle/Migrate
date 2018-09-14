#  File: Boxes.py

#  Description: A recursive algorithm to see if boxes fit in eachother

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 3/2/16

#  Date Last Modified: 3/3/16

# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////

class Box(object):

	# x, y, and z represent side lengths
	def __init__ (self, x = 0, y = 0, z = 0):

		dim = [x, y, z]
		dim.sort()
		dim.reverse()

		# x is largest of dimensions; z is smallest

		self.x = dim[0]
		self.y = dim[1]
		self.z = dim[2]

	def __str__ (self):
		s = "[{}, {}, {}]".format(self.x, self.y, self.z)
		return s

	# checks if other nests inside self
	def is_nest(self, other):

		if (self.x <= other.x) or (self.y <= other.y) or (self.z <= other.z):
			return False

		else:
			return True

# //////////////////////////////////////////////////////////////////////////////

# a print function I needed to iterate through lists of objects
def spec_print(a):
	a.reverse()
	for el in a:
		print(str(el))

# //////////////////////////////////////////////////////////////////////////////

# declare global subset list for recursion to call
subsets = []

def sub_sets (a, b, idx):

	global subsets

	if (idx == len(a)):

		# the second boolean is for when B and C both return the same subset
		if (len(b) > 1) and (subsets.count(b) == 0):
			subsets.append(b)
		return

	else:

		c = b[:]		
		if (len(b) < 1):
			
			b.append(a[idx])
			sub_sets(a, c, idx + 1)
			sub_sets(a, b, idx + 1)

		# if the last element of b nests a[idx], add it.
		if ((len(b) >= 1) and (b[-1].is_nest(a[idx]))):

			b.append(a[idx])
			sub_sets (a, c, idx + 1)
			sub_sets (a, b, idx + 1)

		# if it doesn't, get rid of it.
		else:
			sub_sets(a, c, idx + 1)

# //////////////////////////////////////////////////////////////////////////////

def main():

	# open file
	in_file = open(".\Boxes.txt", "r")
	num_box = int(in_file.readline())

	# make empty box list
	box_list = []

	# read through file and create a box object with each line of information
	for line in in_file:
		coor = line.split()
		x = int(coor[0])
		y = int(coor[1])
		z = int(coor[2])
		box_list.append(Box(x, y, z))

	# sort the boxes by the largest value
	box_list.sort(key = lambda x: x.x, reverse = True)

	# start the recursion
	b = []
	sub_sets(box_list, b, 0)

	# find the largest of the nests
	max_nest = 0
	for el in subsets:
		if len(el) >= max_nest:
			max_nest = len(el)

	# any subset of size max_nest will be appended to sols
	sols = []
	for el in subsets:
		if (len(el) == max_nest):
			sols.append(el)

	# print the solutions
	print("\nLargest Subset(s) of Nesting Boxes")
	for el in sols:
		spec_print(el)
		print()

main()
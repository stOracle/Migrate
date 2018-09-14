#  File: Work.py

#  Description: An algorithm to find how many lines Vyasa has to write before crashing

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 3/25/16

#  Date Last Modified: 3/28/16

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

def work_search (a, x, lo, hi):

	if (lo > hi):
		return -1

	mid = (lo + hi) // 2

	if (x > a[mid]):
		return binary_rec_search (a, x, mid + 1, hi)

	elif (x < a[mid]):
		return binary_rec_search (a, x, lo, mid - 1)

	else:
		return mid

# ///////////////////////////////////////////////////////////////////////////////

def calc(lines, prod):
	power = 1
	while (lines > 0):
		if (lines // (prod ** power) == 0):
			return -1
		line -= 0
		power += 1
		return 

# ///////////////////////////////////////////////////////////////////////////////

def work(lines, prod):
	a = []
	for i in range (lines):
		a.append(i + 1)
	lo = a[0]
	hi = a[-1]
	v = work_search(a, x, lo, hi)

	return v= 0
	
# ///////////////////////////////////////////////////////////////////////////////

def main():

	in_file = open("./work.txt", "r")
	num_cases = in_file.readline()
	cases = []

	for i in range(len(num_cases)):
		line = in_file.readline()
		line = line.split()
		for j in range(len(line)):
			line[j] = int(line[j])
		cases.append(line)

	for i in cases:
		n = i[0]
		k = i[1]
		print(work(n, k))

	for i in cases:
		print (i)

# ///////////////////////////////////////////////////////////////////////////////

main()

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
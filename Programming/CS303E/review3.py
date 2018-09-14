########Dictionary and its associated functions########



#1. [COMPLETE] Create a function that accepts a string as an input 
#parameter and then prints out the frequency of all the
#characters other than white space characters. Use a
#dictionary and parse the input string character by
#character. The character will be the key and the
#frequency of its occurence the value. Print all the
#key-value pairs at the end.

def q1 (st):
	st_dict = {}
	st = st.strip()
	st_list = st.split()
	for el in st_list:
		for i in range (len(el)):
			if el[i] in st_dict:
				st_dict[el[i]] += 1
			else:
				st_dict[el[i]] = 1


	return st_dict


########Set and its associated functions########


#2. write a function that accepts two lists of strings as input
#and returns a list that has only the strings common to both the input list. 
#Use a sets inside the function

def q2 (l1, l2):
	return None


########List and its associated functions########


#3. [COMPLETE] Create a 3x5 list populated with random numbers in the range [1, 100]

def q3 ():

	import random
	matrix = []
	for i in range (3):
		row = []
		for j in range (5):
			row.append(random.randint(1, 100))
		matrix.append(row)

	return matrix


#4. [COMPLETE] Write a function that takes as input two 2-D list and returns
#True if they are the same and False otherwise.

def q4 (a, b):

	if (len(a) != len(b)):
		return False
	elif (len(a[0]) != len(b[0])):
		return False
	else:
		for i in range (len(a)):
			for j in range (len(a[0])):
				if (a[i][j] != b[i][j]):
					return False
		return True


#5. [COMPLETE] Write a function that takes as input two 2-D list of the same
#size and returns a 2-D list that has the sum of the corresponding
#elements of the two lists.

def q5 (a, b):
	if ((len(a) != len(b)) or (len(a[0]) != len(b[0]))):
		return None
	else:
		mat_sum = []
		for i in range (len(a)):
			row = []
			for j in range (len(a[0])):
				row.append(a[i][j] + b[i][j])
			mat_sum.append(row)
		return mat_sum


#6. [COMPLETE] Write a function that takes as input a 2-D list and returns
#   a 2-D list with each row in reverse order.

def q6 (a):
	rev = []
	for i in range (len(a)):
		el_list = []
		for j in range (len(a[0])):
			el_list.append(a[i][j])
		el_list.reverse()
		rev.append(el_list)
	return rev


#7. [COMPLETE] Write a function that takes as input a 2-D list and returns a
#   2-D list with each column in reverse order.

def q7 (a):
	reflect = []
	for i in range (len(a)):
		reflect.append(a[-(i + 1)])

	return reflect


#8. [COMPLETE] Write a function that takes as input two 1-D list of the same
#   size and returns a single number that is the sum of the corresponding
#   products of the elements of the two lists.
#   a = [1, 2, 3]
#   b = [4, 5, 6]
#   Your function should return 1*4 + 2*5 + 3*6 = 32

def q8 (a, b):
	if (len(a) != len(b)):
		return None
	else:
		prod = 0
		for i in range (len(a)):
			prod += a[i] * b[i]

	return prod

#9. [Complete] Write a function that takes as input a 1-D list and returns True
#   if it is sorted in ascending order and False otherwise.

def q9 (a):
	for i in range (len(a) - 1):
		if (a[i] > a[i + 1]):
			return False
	return True


#10. Write a function that sums the rows, columns, and diagonals of a
#   2-D list.

def q10 (a):
	sum_rows = 0
	sum_cols = 0
	sum_diags = 0

	for i in range (len(a)):
		sum_row = 0
		for j in range (len(a[0])):
			sum_row += a[i][j]
		sum_rows += sum_row

	#for j in range (len(a[0])):
	return None


#11. Given a 1-D list of 3 numbers sort the list in ascending order
#   without using the built-in sort function or loops.

def q11 (a):
	sort_a = []
	if (a[0] <= 0):
		return None
  

#12. [COMPLETE] Given a 1-D list shuffle the contents of the list.

def q12 (a):
	import random
	shuffle = []
	used = []
	for i in range (len(a)):
		
		spot = random.randint(0, len(a) - 1)
		while (spot in used):
			spot = random.randint(0, len(a) - 1)
		shuffle.append(a[spot])
		used.append(spot)

	return shuffle




########Basic algorithms of sorting, searching, and merging########



#13. Consider the binary search code shown below. What is the last
#      value that is printed for count and mid when
#      a = [ 2, 5, 8, 9, 11, 14, 16, 19, 22, 25, 35, 41, 45, 55, 62]
#      x = 23

def q13 ():
	return None

def binarySearch (a, x):
	lo = 0
	hi = len(a) - 1
	count = 0
	print ()
	while (lo <= hi):
		count = count + 1
		mid = (lo + hi) // 2
		print (" count = ",count, "\n")
		print ("    lo = ",lo)
		print (" a[lo] = ",a[lo])
		print ("   mid = ", mid)
		print ("a[mid] = ",a[lo])
		print ("    hi = ",hi)
		print (" a[hi] = ",a[hi], "\n")
		if (x < a[mid]):
			hi = mid - 1
		elif (x > a[mid]):
			lo = mid + 1
		else:
			return mid
	return -1



########String and its associated functions########



#14. Write a function that takes as input two strings and returns True
#   if the two string are anagrams and False otherwise. The strings may
#   have spaces and punctuation marks and upper and lower characters. You
#   are only concerned that they have the same letters (case insensitive).

def q14 (s1, s2):

	strings = (s1, s2)
	dict_s1 = {}
	dict_s2 = {}
	dictionaries = (dict_s1, dict_s2)
	ch_sets = []

	for st in range (2):

		ch_set = set()
		string = strings[st]
		string = string.lower()
		string = string.strip()
		st_list = string.split()

		for el in st_list:
			for i in range (len(el)):
				if (el[i] >= "a") and (el[i] <= "z"):
					if el[i] in dictionaries[st]:
						(dictionaries[st])[ch] += 1
					else:
						(dictionaries[st])[ch] = 1
						ch_set.add(ch)

		ch_sets.append(ch_set)





	return None



########File manipulations for reading, writing, and appending########



#15. Write a function that takes as input two strings - username and
#   password and returns True if they match a username and password
#   combination in a password file and False otherwise. The password file 
#   is called passwd.txt and the username and passwords are stored one pair 
#   to a line and each pair of username and password is separated by a colon.
#   username1:password1
#   ...
#   usernameN:passwordN

def q15 ():
	return None



########Write recursive code from recurrence relations and write the output of########



#16. Write a recursive function that implements this recurrence relation
#   f(n) = 2 * f(n - 1) + n where f(0) = 0
#   What is f(8)?

def q16 (n):
	#base case
	if (n == 0):
		return 0
	else:
		return ((2 * q16(n-1)) + 1)



#17. Consider the recursive function shown below. What will it return
#   for recurse (45, 75)?
def recurse (m, n):
	print ("(m, n) = ({}, {})".format(m, n))
	if (m == n):
		return m
	elif (m > n):
		return recurse (m - n, n)
	else:
		return recurse (n - m, m)

def q17 ():
	return None









def main():
	# a = [[1, 2, 3], [0, 0, 0], [8,2,1]]
	# b = [[1, 2, 3], [1, 0, 1], [1, 2, 1]]
	# names = ["a", "b", "mat_sum"]
	# mat_sum = q5(a, b)
	# together = [a, b, mat_sum]

	# names2 = ["a", "a_reflect"]
	# together2 = [a, q7(a)]

	# # for el in range (len(together2)):
	# # 	print()
	# # 	for i in range (len(together2[el])):
	# # 		if (i == 1):
	# # 			print ("{:>15}{}".format(names2[el] + " = ", together2[el][i] ))
	# # 		else:
	# # 			print ("{:>15}{}".format("", together2[el][i] ))

	# c = [1,2,3,4,5,6,7,8,9]
	# d = [2,1,3]
	# e = [1,2,3]

	# print ("C = ", c)
	# print ("C shuffled = ", q12(c))

	# st = input(str("Enter string: "))
	# freq_st = q1(st)
	# print (freq_st)


	# a = [2,5,8,9,11,14,16,19,22,25,35,41,45,55,62]
	# print (binarySearch (a, 23))

	print (recurse (35, 700))

		




main()
def is_palin(s):
	for i in range (len(s) // 2):
		if (s[i] != s[-(i + 1)]):
			return False
	return True

def rotate (s, r):
	sub = s[-r:]
	return sub + s[:-r]

def count_word(line, find):
	line_list = line.split()
	count = 0
	for i in range (len(line_list)):
		if (line_list[i] == find):
			count += 1
	return count

def is_ascend (m):
	for i in range (len(m) - 1):
		if (m[i] > m[i + 1]):
			return False
	return True

def umm(m, n):
	sum_t = 0
	for i in range (3):
		sum_t += m[i] * n[i]
	return sum_t

def rand_matrix (r,c):
	import random
	x = []
	for i in range (r):
		row = []
		for j in range (c):
			row.append(random.randint(1, 100))
		x.append(row)
	return x

def fli (matrix):

	dup = []
	for i in range (len(matrix)):
		dup.append(matrix[i])
	
	for i in range (len(dup)):
		for j in range (len(dup[0]) // 2):
			
			dup[i][j], dup[i][-(j + 1)] = dup[i][-(j + 1)], dup[i][j]
		
	return dup

def reverse_num (n):
	m = 0
	while (n > 0):
		m *= 10
		m += n % 10
		n = n // 10
	return m

def is_palindromic (n):
	if (n == reverse_num(n)):
		return True
	else:
		return False


def q_5 ():
	for i in range (1000,10000):
		if ((not is_palindromic (i)) and (is_palindromic(i ** 3))):
			return i

def q_7 (in_file):
	out_file = open("./out.txt", "w")
	for line in in_file:
		if not line.isspace():
			line = line.strip()
			line = line.rstrip("\n")
			print (line)
			out_file.write(line + "\n")
	out_file.close()

def q_12 (st):
	s = ""
	for i in range (0, len(st), 2):
		s += st[i]
	return s

def q_16(size):
	m = []
	for i in range (size):
		row = []
		for j in range (size):
			if ((j == 0) or (j == size - 1) or (i == 0) or (i == size - 1)):
				row.append(1)
			else:
				row.append(0)
		m.append(row)
	return m


def make_board():
	import random

	m = []
	for i in range (8):
		row = []
		for j in range (8):
			row.append("-")
		m.append(row)

	n_i, n_j = random.randint(0,7), random.randint(0,7)
	p_i, p_j = random.randint(0,7), random.randint(0,7)

	m[n_i][n_j] = "N"
	m[p_i][p_j] = "P"

	return m


def q_9():
	import math
	board = make_board()
	for i in range (len(board)):
		st = ""
		for j in range (len(board)):
			if (j == len(board) - 1):
				st += str(board[i][j])
			else:
				st += str(board[i][j]) + " "
		print (st)

	for i in range (len(board)):
		for j in range (len(board)):
			if (board[i][j] == "N"):
				loc_N = [i, j]
			if (board[i][j] == "P"):
				loc_P = [i, j]

	if (abs(loc_N[0] - loc_P[0]) + abs(loc_N[1] - loc_P[1]) == 3):
		if ((loc_N[0] == loc_P[0]) or (loc_N[1] == loc_P[1])):
			return "Miss"
		else:
			return "Hit"

	else:
		return "Miss"


def sum_divisors(n):
	divisors = []
	for i in range (1, int((n //2 + 1))):
		if (n % i == 0):
			divisors.append(i)

	sum_d = 0
	for i in range (len(divisors)):
		sum_d += divisors[i]
	return sum_d

def max_div (rng):
	lo = rng[0]
	hi = rng[1]
	max_d = 0
	for i in range (lo, hi + 1):
		if (sum_divisors(i) > max_d):
			max_d = i
			sum_d = sum_divisors(i)
	return [max_d, sum_d]




def main():
	
	rng = str(input("enter a range (x and y): "))
	dom = rng.split()
	dom[0] = int(dom[0])
	dom[1] = int(dom[1])
	
	a = max_div (dom)
	print ("{} has highest sum at {}.".format(a[0], a[1]))

		




main()
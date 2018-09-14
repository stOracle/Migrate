def permute(a, lo):
	hi = len(a)
	if (lo == hi):
		print(a)
	else:
		for i in range (lo, hi):
			a[lo], a[i] = a[i], a[lo]
			permute (a, lo + 1)
			a[lo], a[i] = a[i], a[lo]

def subsets (a, b, lo):
	hi = len(a)
	if (lo == hi):
		print(b)
		return
	else:
		c = b[:]
		b.append (a[lo])
		subsets (a, c, lo + 1)
		subsets (a, b, lo + 1)

def combine (a, b, lo, size):
	hi = len(a)
	if (lo == hi):
		if (len(b) == size):
			print (b)
		return

	if (len(b) == size):
		print(b)
	else:
		c = b[:]
		b.append(a[lo])
		combine (a, c, lo + 1, size)
		combine (a, b, lo + 1, size)

def main():
	code = str(input("What do you want to run? "))
	if (code == "permute"):
		a = input(str("Enter the letters: "))
		A = []
		for i in range (len(a)):
			A.append(a[i])
		permute(A,0)
	if (code == "subsets"):
		a = [15, 9, 30, 21, 19]
		b = []
		subsets (a, b, 0)
	if (code == "combine"):
		a = ['A', 'B', 'C', 'D', 'E']
		b = []
		combine (a, b, 0, 3)


main()
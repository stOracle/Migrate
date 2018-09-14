def sub_sets (a, b, idx):
	if (idx == len(a)):
		print (b)
		return 
	else:
		c = b[:]
		b.append(a[idx])
		sub_sets (a, c, idx + 1)
		sub_sets (a, b, idx + 1)

def main():

	a = [10, 8, 5, 4]
	b = []
	sub_sets(a,b,0)




main()
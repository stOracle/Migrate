def main():
	input_file = open ("./isbn.txt", "r")
	output_file = open ("isbnOut.txt", "w")

	for line in input_file:
		isbn = line
		isbn_diff = isbn.strip()
		isbn_diff = isbn_diff.replace("-", "")
		a = []
		for i in range (len(isbn_diff)):
			a.append(isbn_diff[i])
		print ("isbn =", isbn, end = "\n")
		print ("isbn_diff =", isbn_diff, end = "\n")
		print ("a =", a, end = "\n")


main()
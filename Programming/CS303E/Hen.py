def main():

	answers = []
	print ()
	mod = int(input("{:>10}{}".format("", "Enter the Modulus: ")))
	print ()

	for x in range(mod):
		if (((13*(x**7)) - (42 * x) - 649) % mod == 0):
			answers.append(x)

	for el in answers:
		print ("{:>10}{} is a solution mod 81".format("", el))

	if (len(answers) == 0):
		print ()
		print ("{:>20}".format ("No Solutions"))



main()
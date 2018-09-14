def main():

	mod = int(eval(input("Enter the mod:")))
	quick = int(input("Quick:"))
	soln = []

	for i in range (mod):
		f_i = (i ** 2) + i + 46
		#print ("f({}) = {}".format(i, f_i))
		if (f_i % mod == 0):
			soln.append(i)
	#print ((763 ** 2) + 763 + 46)

	num = -46129
	mult = 0
	while (num < 0):
		num += mod 
		mult += 1
	print ("mult:", mult)
	god = (quick ** 2) + quick + 46
	print ("f({}) = {}".format(quick, god))

	print (soln)
main()
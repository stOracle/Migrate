def ferlittle(num):
	for a in range (2, num):
		if (a % 7 == 0) or (a % 13 == 0) or (a % 31 == 0):
			continue
		elif ((a ** (num - 1)) % num != 1):
			return [False, a]
		#elif (num % a == 0):
			#return [False, a]
	return [True]



def main():
	print ("\n{:>40}:".format("Fermat's Little Theorem"))
	print ("{:>36}".format("a^(p-1) % p == 1"))
	num = int(input("\nUse Fermat's little number to check for primality: "))
	sol = ferlittle(num)
	if (sol[0] == False):
		print ("{} is not prime: consider a = {}".format(num, sol[1]))
	else:
		print ("{} is prime".format(num))




main()

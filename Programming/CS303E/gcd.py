def gcd(m, n):

	if (n == 0):
		return m
	elif (m <= n):
		return gcd(m, n - m)
	elif (m > n):
		return gcd(m - n, n)


def main():
	m = int(input("Enter m: "))
	n = int(input("Enter n: "))

	GCD = gcd(m,n)

	print ("The GCD of {} and {} is {}.".format(m, n, GCD))


main()
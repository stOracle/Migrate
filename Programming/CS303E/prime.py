def is_prime (n):
	limit = int (n ** 0.5) + 1
	divisor = 2
	if (n == 2):
		return True
	while (divisor < limit):
		if (n % divisor == 0):
			return False
		divisor = divisor + 1
	return True

def main():
	num = int(input("Find the prime factorization of: "))
	num_fact = 0
	factor = ""
	form = num
	for part in range (2, int(num ** .5 + 1) + 5):
		if is_prime(num):
			factor = str(num)
			num_fact = 1
			break
		if is_prime(part):
			while (form % part == 0):
				num_fact += 1
				factor += str(part) + "*"
				form = form // part
	if (form != 1) and (form != num):
		factor += str(form)
		num_fact += 1
	print ("The prime factorization of", num, "is\n", factor)
	print ("The number of prime factors is =", num_fact)
	print ("Prime?", is_prime(num))

main()
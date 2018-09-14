import math

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
	print ()
	num = int(eval(input("Find the prime factorization of: ")))
	
	num_fact = 0
	factor = ""
	form = num
	
	for part in range (2, int(num ** .5) + 5):
		if is_prime(form):
			break
		if is_prime(num):
			factor = str(num)
			num_fact = 1
			break
		if is_prime(part):
			num_part = 0
			while (form % part == 0):
				num_part += 1
				num_fact += 1
				
				form = form // part
			if (num_part != 0):
				print(str(part) + "^" + str(num_part))
				factor += str(part) + "^" + str(num_part) + " * "
	if (form != 1) and (form != num):
		factor += str(form) + "^1"
		num_fact += 1
	if (form == 1):
		factor = factor[:-2]
	if (form == num):
		factor += str(num) + "^1"
		print (factor)
	print ("\nThe prime factorization of", num, "is\n\n", factor)
	print ()
	print ("The number of prime factors is =", num_fact)
	print ("\nPrime?", is_prime(num))

main()
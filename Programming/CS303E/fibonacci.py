def main():
	fib = [0,1]
	fib_even = []
	sum_at_j = []
	for i in range (2, 15):
		fib.append(fib[i - 2] + fib[i - 1])
	for i in range (0, len(fib), 2):
		fib_even.append(fib[i])


	for i in range (len(fib) // 2):
		sum_j = 0
		mini = [i]

		for j in range (i + 1):
			sum_j += fib_even[j]
		mini.append(sum_j)
		sum_at_j.append(mini)

	print ("{:>10} {}".format("fib:", fib))
	print ("{:>10} {}".format("fib_even:", fib_even))

	for i in range (len(sum_at_j)):
		if (i == 0):
			print("{:>10} {}".format("sum at j:", sum_at_j[i]))
		else:
			print ("{:>10} {}".format("",sum_at_j[i]))



main()
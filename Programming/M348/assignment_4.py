import math

'''
---------------------------------------------------------------------
vvvvvvvvvvvvvvvvvvvvvvvvvvvvv PROBLEM 4 vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
---------------------------------------------------------------------
'''

def g(x):

	y = math.exp(x) + (2 ** (-x)) + 2 * math.cos(x) - 6
	return y

def g_prime(x):

	y = math.exp(x) + (-2 * (2 ** (-x)) * (math.log(2))) - (2 * math.cos(x))
	return y

def newton():

	print("------------Problem 3-------------")

	p0 = float(input("\nEnter the value for P0: "))
	TOL = float(eval(input("Enter the Tolerance for error: ")))
	
	error = 1.0
	i = 1
	
	while (error > TOL):
	
		p = p0 - (g(p0) / g_prime(p0))
		error = abs(p - p0)
	
		print("\nIteration: {}".format(i))
		print("Approximate root: P = {}".format(p))
		
		p0 = p
		i += 1

'''
---------------------------------------------------------------------
vvvvvvvvvvvvvvvvvvvvvvvvvvvvv PROBLEM 4 vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
---------------------------------------------------------------------
'''

def f(x):
	
	y = (x ** 2) - (4 * x) + 4 - math.log(x)
	return y

def secant():

	print("------------Problem 4-------------")

	p0 = float(input("\nEnter the value for P0: "))
	p1 = float(input("Enter the value for P1: "))
	TOL = float(eval(input("Enter the Tolerance for error: ")))

	error = 1.0
	i = 1

	while (error > TOL):

		p = p1 - (f(p1) * ((p1 - p0) / (f(p1) - f(p0))))
		error = abs(p - p1)

		print("\nIteration {}:".format(i))
		print("Approximate root: P = {}".format(p))

		i += 1
		p0 = p1
		p1 = p

'''
---------------------------------------------------------------------
vvvvvvvvvvvvvvvvvvvvvvvvvvv INPUT vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
---------------------------------------------------------------------
'''

def main():

	print ("\nWhich problem would you like to run?")
	
	select = int(input("Enter 3 or 4: " ))
	if ((select > 4) or (select < 3)):
		select = int(input("Enter 3 or 4: "))

	print()

	if (select == 3):
		newton()

	if (select == 4):
		secant()

main()



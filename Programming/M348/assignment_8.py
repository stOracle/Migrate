import math

# ////////////////////////////////PROBLEM 4///////////////////////////////////////

def simpson(a, b, n):

	h = (b - a)/n
	XI0 = f(a) + f(b)
	XI1 = 0
	XI2 = 0
	for i in range(1, n):
		x = a + i*h
		if (i % 2 == 0):
			XI2 += f(x)
		else:
			XI1 += f(x)
	XI = (XI0 + 2 * XI2 + 4 * XI1) * (h / 3)
	return XI

def trap(a, b, n):
	h = (b - a)/n
	XI0 = f(a) + f(b)
	XI1 = 0
	for i in range(1, n):
		x = a + i * h
		XI1 += f(x)

	XI = (h / 2) * (XI0 + 2 * XI1)
	return XI

def f(x):
	a = math.exp(2*x)
	b = math.sin(3*x)
	return a * b

def main():
	a = 0
	b = 2
	iterations = [10, 100, 1000]

	print("\n---------SIMPSONS APPROXIMATION--------\n")
	for i in iterations:		
		print("n = {}; solution = {}".format(i, simpson(a, b, i)))

	print("\n---------TRAPEZOIDAL APPROXIMATION--------\n")
	for i in iterations:		
		print("n = {}; solution = {}".format(i, trap(a, b, i)))

main()
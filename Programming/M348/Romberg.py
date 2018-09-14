import math

def f(x):
	return (x**2)*math.log(x)

def main():
	value = float(input("Enter value: "))
	while (value != "done"):
		print (f(value))
		value = float(input("Enter value: "))



main()
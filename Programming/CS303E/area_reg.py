import math

n = int(input("Enter number of sides:"))
s = float(input("Enter length of side:"))

Area = (n * s ** 2) / (4 * math.tan(math.pi/n))

print(Area)
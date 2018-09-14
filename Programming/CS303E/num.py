#prompt the user to enter an integer
num = int(input("Enter a 4 digit integer:"))

#calculate and print first number
f = num // 1000

#calculate and print second number
s = (num - f * 1000) // 100

#calculate and print third number
t = (num - (f * 1000 + s * 100)) // 10

#calculate and print last number
l = num - (f * 1000 + s * 100 + t * 10)
print(l * 1000 + t * 100 + s * 10 + f)
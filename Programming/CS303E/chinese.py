mod = int(input("enter mod: "))
#val = int(input("enter x: "))

for i in range (mod):
	if ((((i ** 3) - (4 * i**2) - (2*i) -83) % mod) == 0):
		print (i)
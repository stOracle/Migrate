#prompt the user for monthly savings amount
dep = float(input("Enter the monthly saving amount:"))

#Calculate account balance after one month
rate = 1 + .05 / 12
m1 = dep * rate

#after second month
m2 = (m1 + dep) * rate

#after third month and so on
m3 = (m2 + dep) * rate
m4 = (m3 + dep) * rate
m5 = (m4 + dep) * rate
m6 = (m5 + dep) * rate

print("After the sixth month, the account value is" , m6 , end = ".")

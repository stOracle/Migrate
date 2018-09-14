#prompt user to enter their weight and height
w = float(input("Enter your weight in pounds:"))
h = float(input("Enter your height in inches:"))

#convert weight to kilograms
k = w * .45359237

#convert height to meters
m = h * .0254

#calculate bmi
bmi = k / m ** 2

#print BMI result
print("BMI is" , bmi , end=".")
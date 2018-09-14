#prompt the user to enter outside temperature in Fahrenheit
temp = float(input("Enter the temperature in Fahrenheit between -58 and 41:"))

#prompt user to enter wind velocity
vel = float(input("Enter the wind speed in miles per hour:"))

chill = float(35.74 + 0.6215 * temp - 35.75 * vel ** .16 + .4275 * temp * vel ** .16)
print("The wind chill index is" , chill , end=".")
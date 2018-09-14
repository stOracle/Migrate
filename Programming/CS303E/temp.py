#prompt the user to enter outside temperature in Fahrenheit
temp = input(int("Enter the temperature in Fahrenheit between -58 and 41:")
while((temp < -58) or (temp > 41)):
  temp = input(int("Enter the temperature in Fahrenheit between -58 and 41:")

#prompt user to enter wind velocity
vel = input(int("Enter the wind speed in miles per hour:")
while(vel < 2):
  vel = input(int("Enter the wind speed in miles per hour:")
print(temp + vel)


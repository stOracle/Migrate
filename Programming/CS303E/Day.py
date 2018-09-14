#  File: Day.py

#  Description: A program which tells the user the day of the week given a day, month, and year

#  Student Name: Stephen Rauner

#  Student UT EID: STR428

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 9/15/2015

#  Date Last Modified: 9/16/15

#create funtion to determine number of days of month
def num_day(year, mon):
  is_leap = (((year + 1) % 400 == 0) or ((year + 1) % 100 != 0) and ((year + 1) % 4 == 0))
  if ((mon == 11) or (mon == 1) or (mon == 3) or (mon == 5) or (mon == 6) or (mon == 8) or (mon == 10)):
    return 31
  elif ((mon == 2) or (mon == 4) or (mon == 7) or (mon == 9)):
    return 30
  elif ((mon == 12) and is_leap):
    return 29
  elif ((mon == 12) and not is_leap):
    return 28
  


def main():

  #prompt the user to enter year, month, and day
  c = int(input("Enter year:"))
  while((c < 1900) or (c > 2100)):
    c = int(input("Enter year:"))
  
  a = int(input("Enter month:"))
  while((a < 1) or (a > 12)):
    a = int(input("Enter month:"))

  #adjust values for months to fit the formula
  if (a == 1):
    a = 11
    c = c - 1
  elif (a == 2):
    a = 12
    c = c - 1
  else:
    a = a - 2

  b = int(input("Enter day:"))
  while((b < 1) or (b > num_day(c, a))):
    b = int(input("Enter day:"))

  #calculate century (using adjusted year for Jan and Feb)
  d = c // 100

  #eliminate first two digits of year
  c = c % 100

  #algorithm given
  w = (13 * a - 1) // 5
  x = c // 4
  y = d // 4
  z = w + x + y + b + c - 2 * d
  r = z % 7
  r = (r + 7) % 7

  #assign the day of the week using r
  if (r == 0):
    day = "Sunday"
  elif (r == 1):
    day = "Monday"
  elif (r == 2):
    day = "Tuesday"
  elif (r == 3):
    day = "Wednesday"
  elif (r == 4):
    day = "Thursday"
  elif (r == 5):
    day = "Friday"
  elif (r == 6):
    day = "Saturday"

  #print final result
  print("The day is" , day, end = ".")      
 
main()
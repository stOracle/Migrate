#  File: EasterSunday.py
#  Description: A program designed using Euler's Easter Day formula. Given the year, calculates what day of what month Easter will land on.
#  Student Name: Stephen T. Rauner
#  Student UT EID: STR428
#  Course Name: CS 303E
#  Unique Number: 50475
#  Date Created: 9/6/15
#  Date Last Modified: 9/6/15

def main():
 
  y = int(input("Enter year:"))			#user prompt

  a,b,c = (y % 19),(y//100),(y%100)		#values for a, b, and c
  d,e = (b//4),(b%4)				#values for d and e
  g = (8 * b + 13) // 25			#value for g
  h = (19 * a + b - d - g + 15) % 30		#Value for h
  j,k = (c//4),(c%4)				#value for j and k
  m = (a + 11 * h) // 319			#value for m
  r = (2 * e + 2 * j - k - h + m + 32) % 7	#value for r
  n = (h - m + r + 90) // 25			#value for n
  p = (h - m + r + n + 19) % 32			#value for p
  
  month = ""					#Using the data to apply to month
  if (n == 3):					
    month = "March"
  if (n == 4):
    month = "April"

  print ("In", y, "Easter Sunday is on", p, month, end=".")


main()






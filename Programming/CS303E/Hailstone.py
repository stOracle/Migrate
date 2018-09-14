#  File: Hailstone.py

#  Description: A program generating the number of "hailstone" operations for a range of numbers

#  Student Name: Stephen Rauner

#  Student UT EID: STR428

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 9/20/15

#  Date Last Modified: 9/20/15

def main():
  #define variables
  cycle_length = 0
  max_length = 0
  num_max = 0

  #prompt the user to enter the range
  lo = int(input("Enter starting number of the range:"))
  hi = int(input("Enter ending number of the range:"))

  #error checking of input
  while (lo <= 0) or (lo >= hi):
    lo = int(input("Enter starting number of the range:"))
    hi = int(input("Enter ending number of the range:"))
  
  #go through each number in that range (outer loop)
  while (lo <= hi): 

    #assign dummy variable num so lo doesn't loop forever and 
    #set cycle_length = 0 before each iteration of inner loop
    cycle_length = 0
    num = lo

    #inner loop to do calculations - stops when num == 1
    while (num != 1):

      #for each number in that range compute the cycle length
      if (num % 2 == 0):
        num = num // 2
        cycle_length += 1
      else:
        num = num * 3 + 1
        cycle_length += 1

    #if cycle length is greater than or equal to the max cycle length replace max cycle
    #length with current cycle length and num_max
    #with current number
    if (cycle_length >= max_length):
      num_max = lo
      max_length = cycle_length
 
    #moving on to next number
    lo += 1
  
  #outside of the two loops print out the result
  print("The number", num_max, "has the longest cycle of", max_length, end=".")
      
main()
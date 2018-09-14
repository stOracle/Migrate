#  File: Goldbach.py

#  Description: An algorithm to express all numbers in range() as a sum of two primes

#  Student Name: Stephen Rauner

#  Student UT EID: STR428

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 9/25/15

#  Date Last Modified: 9/25/15

# function for determining if n is prime
def is_prime (n):
  limit = int (n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor = divisor + 1
  return True

def main():

  #prompt the user to enter variables
  lo = int(input("Enter the lower limit:"))
  hi = int(input("Enter the upper limit:"))

  #error checking of user entered range
  while ((lo < 4) or (lo // 2 == 1) or (hi // 2 == 1) or (lo >= hi)):
    lo = int(input("Enter the lower limit:"))
    hi = int(input("Enter the upper limit:"))

  #first loop - input of all even integers in range
  for num in range (lo, (hi + 1), 2):

    #assign dummy variables
    num_1 = 0
    num_2 = 0

    #inner loop - runs through all numbers less than num
    for sub in range (2, num):

      #assign num_1 and num_2
      num_1 = sub
      num_2 = num - num_1

      #for all sums of num, test if the two numbers are both prime
      if ((is_prime (num_1)) and (is_prime(num_2)) and (num_1 <= num_2)):
        
        #print every passing option
        print(num, "=", num_1, "+", num_2)

      #when num_1 and num_2 are not prime, try new values
      else:
        num_1 += 1
        

main()
      
      
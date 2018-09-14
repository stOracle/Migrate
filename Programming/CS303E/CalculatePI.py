#  File: CalculatePI.py

#  Description: An alternate method of calculating the digits of pi

#  Student Name: Stephen Rauner

#  Student UT EID: STR428

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 10/2/15

#  Date Last Modified: 10/5/15

import math
import random

#built in function to compute Pi using random throws
def computePI (num_throws):

  #define variables
  counter = 1
  num_success = 0
  xPos = 0
  yPos = 0

  #loop to perform a random throw num_throws times
  while (counter <= num_throws):
    xPos, yPos = (random.uniform(-1.0,1.0), random.uniform(-1.0, 1.0))

    #neste loop: assign a success if throw is in circle
    if (math.hypot (xPos, yPos) < 1):
      num_success += 1
      counter += 1
    else:
      counter += 1

  #approximate pi by 4 * (pi/4) = pi
  approx_pi = 4 * (num_success / num_throws)
  return (approx_pi)    

#small function to call upon the difference of our approx value and the built in version
def diff_pi(num_throws):
  dif = computePI(num_throws) - math.pi
  return dif
  


def main():

  #print the first line of the chart
  print("Computation of PI using Random Numbers\n")

  #assign variable for num_trials
  num_trials = 100

  #assign a loop to print for each iteration
  while (num_trials <= 10000000):

    #formatted string which calls upon all functions
    print("Num = {:<9d}   Calculated PI = {:9.6f}   Difference = {:+9.6f}".format 
      (num_trials, computePI(num_trials), diff_pi(num_trials)))

    #moves loop to next iteration
    num_trials *= 10

  #print extra line and footer
  print()
  print("Difference = Calculated PI - math.pi")

main()


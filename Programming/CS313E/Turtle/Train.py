#  File: Train.py

#  Description: A turtle graphics attempt of drawing a choo-choo train

#  Student Name: Stephen Rauner 

#  Student UT EID: STR428

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 2/28/16

#  Date Last Modified: 2/29/16

import turtle
import math

def drawLine (ttl, x1, y1, x2, y2):

    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.penup()

def tracks(ttl, start_x, num):

	ttl.penup()
	ttl.goto(start_x, -310)

	y = -310

	w = 23
	h = 5


	for i in range(num):
		ttl.goto(start_x + (i*45), y)
		ttl.pendown()
		drawLine(ttl, start_x + (i * 45), y, start_x + (i * 45), y - h)
		drawLine(ttl, start_x + (i * 45), y - h, start_x + w + (i * 45), y - h)
		drawLine(ttl, start_x + w + (i * 45), y - h, start_x + w +(i * 45), y)
		ttl.penup()

def spokes(ttl, cen_x, cen_y, r):
	for i in range(8):
		ttl.penup()
		ttl.goto(cen_x, cen_y)
		ttl.tilt(45)
		ttl.pendown()
		ttl.forward(r - 10)

def wheels(ttl):
	# big wheel
	ttl.color("red")
	ttl.penup()
	ttl.goto(-200, -300)
	ttl.pendown()
	ttl.circle(50)

	ttl.penup()
	ttl.goto(-200, -290)
	ttl.pendown()
	ttl.circle(40)

	spokes(ttl, -200, -250, 50)

	ttl.penup()
	ttl.goto(-200, -260)
	ttl.pendown()
	ttl.circle(10)	

	# small wheel 1
	ttl.penup()
	ttl.goto(-30, -300)
	ttl.pendown()
	ttl.circle(40)

	ttl.penup()
	ttl.goto(-30, -290)
	ttl.pendown()
	ttl.circle(30)

	spokes(ttl, -30, -260, 40)

	ttl.penup()
	ttl.goto(-30, -265)
	ttl.pendown()
	ttl.circle(5)	

	# small wheel 2
	ttl.penup()
	ttl.goto(100, -300)
	ttl.pendown()
	ttl.circle(40)

	ttl.penup()
	ttl.goto(100, -290)
	ttl.pendown()
	ttl.circle(30)

	spokes(ttl, 100, -260, 40)

	ttl.penup()
	ttl.goto(100, -265)
	ttl.pendown()
	ttl.circle(5)

def main():

	turtle.title("Choo-Choo")
	turtle.setup(800, 800, 0, 0)
	turtle.speed(0)
	turtle.ht()
	ttl = turtle.Turtle()
	ttl.ht()

	drawLine(ttl, -300, -300, 300, -300)
	drawLine(ttl, -300, -310, 300, -310)
	count = 10
	tracks(ttl, -290, 13)
	wheels(ttl)




	turtle.done()

main()
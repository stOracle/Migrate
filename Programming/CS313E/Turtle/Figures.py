# Figures.py
# Makes different Figures

import turtle, math

def drawLine (ttl, x1, y1, x2, y2):

	ttl.penup()
	ttl.goto(x1, y1)
	ttl.pendown()
	ttl.goto(x2, y2)
	ttl.penup()

def drawPolygon(ttl, x, y, num_side, radius):
	sideLen = 2 * radius * math.sin(math.pi / num_side)
	angle = 360 / num_side
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	for iter in range (num_side):
		ttl.forward(sideLen)
		ttl.left(angle)
	ttl.penup()

def main():
	turtle.title('Geometric Figures')
	turtle.setup(700, 500)

	ttl = turtle.Turtle()

	# equilateral Triangle
	ttl.color ('blue')
	drawPolygon (ttl, -200, 0, 3, 50)

	# square
	ttl.color('red')
	drawPolygon (ttl, -50, 0, 4, 50)

	# pentagon
	ttl.color('forest green')
	drawPolygon (ttl, 100, 0, 5, 50)

	# draw octagon
	ttl.color ('DarkOrchid4')
	drawPolygon (ttl, 250, 0, 8, 50)

	# draw a line
	ttl.color ('gold4')
	drawLine (ttl, -200, -10, 325, -10)
	drawLine (ttl, -200, -15, 325, -15)

	# persist drawing
	turtle.done()

main()
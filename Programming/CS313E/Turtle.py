import turtle

def Hello():
	# Put label on top of page
	turtle.title ('Hello World')

	# Setup screen size
	turtle.setup (800, 800, 0, 0)

	# Move the color to origin
	turtle.penup()
	turtle.goto(0, 0)

	# set the color to navy
	turtle.color('navy')

	# Write the message
	turtle.write ('Hello World!', font = ('Times New Roman', 36, 'bold'))

	# hide the turtle
	turtle.hideturtle()

	# persist the drawing
	turtle.done()

def drawSquare (ttl, x, y, side):
	ttl.penup()
	ttl.goto(x, y)

	# set the pen in the +ve x direction
	# changing the direction (angle)
	ttl.setheading(0)

	ttl.pendown()
	for iter in range (4):
		ttl.forward(side)
		ttl.right(90)
	ttl.penup()
	

def squares():
	
	return None


def main():

	# put title
	turtle.title('Squares')

	# set window size
	turtle.setup(500, 500, 0, 0)

	# create the turtle object
	ttl = turtle.Turtle()

	# decide on the shape
	ttl.shape("turtle")

	# decide on speed (1, 10)
	ttl.speed(10)

	ttl.color('red')

	drawSquare(ttl, -50, -50, 50)
	drawSquare(ttl, 0, 0, 50)
	drawSquare(ttl, 50, 50, 50)
	drawSquare(ttl, -50, 50, 150)

	# fill a closed region
	ttl.fillcolor('purple')
	ttl.begin_fill()
	drawSquare (ttl, 0, 0, 50)
	ttl.end_fill()
	turtle.done()



	#Hello()
	#squares()

main()
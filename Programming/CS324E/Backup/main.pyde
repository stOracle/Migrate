from classes import *

def setup():
    # Setup the frame
    # Initialize all figures
    # Etc
    size(500,500)
    B1 = Ball(120, 120, 0)
    B1.velocity(7,3,0)
    B1.radius(50)
    
    B2 = Ball(200, 200, 0)
    B2.velocity(-6,4,0)
    B2.radius(25)
    B2.col("#00FF00")

    B3 = Ball(100, 200, 0)
    B3.velocity(-5,-5,0)
    B3.radius(33)
    B3.col("#0000FF")

# Demonstration code below.
global count
count = 0
def draw():
    background(150)
    
    # Do certain actions at particular times
    global count
    count += 1
    fig = figureList[1]
    if count == 200:
        fig.hide()
    elif count == 400:
        fig.show()
    elif count == 600:
        fig.pause()
    elif count == 800:
        fig.hide()
        fig.resume()
    elif count == 1000:
        fig.show()
    elif count == 1200:
        fig.kill()

    # Update the figures
    for figure in figureList:
        if not(figure.paused):
            figure.update()

    # Display the figures
    for figure in figureList:
        if figure.visible:
            figure.display()
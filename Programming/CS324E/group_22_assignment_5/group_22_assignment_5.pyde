from classes import *
import random

def setup():
    size (700, 700, P3D)
    frameRate(45)

    Master_cube(150, -300, -100, 4, 50)
    #Master_cube(-500, -500, -500, 4, 100)
    
    speed(.7)
    tic()

def draw():
    # Record time elapsed since last frame
    dt = toc()
    
    # Reset master timer for next frame.
    tic()
    
    # Check for collisions and respond accordingly.
    checkCollisions()

    background(10)
    lights()

    #camera movement with mouse click
    if (mousePressed == True):
        camera(5 * pmouseX, 5 * pmouseY, (pmouseX + pmouseY) /2, 0, 0, 0, 0, 1, 0)
    else:
        camera(-1000, -1000, -0, 0, 0, 0, 0, 1, 0)       


    # Draw the grid of the "arena"
    strokeWeight(10)
    stroke(80, 80, 159)
    line(-500, -500, -500, -500, -500, 500)
    line(-500, -500, -500, -500, 500, -500)
    line(-500, -500, -500, 500, -500, -500)

    stroke(80, 200, 159)
    line(500, 500, -500, -500, 500, -500)
    line(500, 500, -500, 500, 500, 500)
    line(500, 500, -500, 500, -500, -500)

    stroke(200, 80, 159)
    line(500, -500, 500, -500, -500, 500)
    line(500, -500, 500, 500, -500, -500)
    line(500, -500, 500, 500, 500, 500)

    stroke(255)
    line(-500, 500, 500, -500, 500, -500)
    line(-500, 500, 500, 500, 500, 500)
    line(-500, 500, 500, -500, -500, 500)
    noStroke()

    # Update and display the figures
    for figure in figureList:
        if not figure.paused:
            figure.update()
        if figure.visible:
            figure.display()

    # for i in range(len(figureList)):
    #     for j in range(len(figureList)):
    #         if (j == i):
    #             continue
    #         else:
    #             if (figureList[i] is Cube):
    #                 if figureList[i].collides_sphere(figureList[j]):
    #                     figureList[i].kill()

# Listen for key press and respond accordingly
global paused
paused = False
def keyPressed():
    # If P is pressed, pause or resume animation.
    global paused
    if key == "p":
        if paused:
            tic()  # reset frame rate timer
            loop() # resume looping
        else:
            noLoop()  # Stop looping the draw() routine
        paused = not(paused)
        
    # if a number 0 through 9 is entered, the simulation spawns a sphere with a mass that scales with the number.
    if ((key >= '0') and (key <= '9')):
        ball_1 = Ball(-200,100,300).velocity(50,-150,-150).radius(40).loss(.85).gravity(10).mass(int(key) + 1) 
        
    # if r is entered, restart the simulation.
    if (key == 'r') or (key == 'R'):
        while (len(figureList) > 0):
            figureList.pop(0)
        while (len(cube_list) > 0):
            cube_list.pop(0)
        while (len(sphere_list) > 0):
            sphere_list.pop(0)
            
        setup()
        
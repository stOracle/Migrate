from classes import *
import random

def setup():
    size (500, 500, P3D)
    frameRate(45)
    
    ball_1 = Ball(-200,100,300)
    ball_1.velocity(30,-30,-30)    
    ball_1.radius(50)
    ball_1.loss(.95)
    ball_1.gravity(1)
    
    ball_2 = Ball(-400,-300,-100)
    ball_2.velocity(-20,40,25)
    ball_2.radius(30)
    ball_2.loss(.95)
    ball_2.gravity(1)
    ball_2.col('#00F0DE')
    
    ball_3 = Ball(100,100,-300)
    ball_3.velocity(-30,20,24)
    ball_3.radius(20)
    ball_3.loss(.95)
    ball_3.gravity(1)
    ball_3.col('#EAE41A')
    
    ball_4 = Ball(400,200,0)
    ball_4.velocity(-8,19,30)
    ball_4.radius(80)
    ball_4.loss(.95)
    ball_4.gravity(1)
    ball_4.col('#1B1271')
    
    ball_t = Ball(50, -350, 0)    
    ball_t.velocity(20,-20,30)
    ball_t.radius(50)
    ball_t.loss(.95)
    ball_t.gravity(1)
    ball_t.col('#12E005')
    
    Master_cube(150, -300, -100, 3, 100)
    #Master_cube(-500, -500, -500, 4, 100)
    #print(str(len(cube_list)))
    #print(str(len(sphere_list)))
    
    
    
def draw():
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
    
    # Update the figures
    for figure in cube_list:
        if figure.visible:
            figure.update()
            
    for figure in sphere_list:
       if figure.visible:
           figure.update()
                
    for figure in cube_list:
        if figure.visible:
            figure.display()
                
    for figure in sphere_list:
        if figure.visible:
            figure.display()
            
    # Check for collisions and assign new velocities and rotations
    
    for cube in cube_list:
       for ball in sphere_list:
           if (cube.collides_sphere(ball)):
               cube.omegaX = random.uniform(0,.2)
               cube.omegaY = random.uniform(0,.2)
               cube.omegaZ = random.uniform(0,.2)
               cube.x += ball.vx
               cube.y += ball.vy
               cube.z += ball.vz
               cube.vx = ball.vx               
               cube.vy = ball.vy
               cube.vz = ball.vz
               ball.y += -ball.vy
               ball.z += -ball.vz
               ball.x += -ball.vx
               ball.vx = -ball.vx
               ball.vy = -ball.vy
               ball.vz = -ball.vz
                
    # for i in range(len(figureList)):
    #     for j in range(len(figureList)):
    #         if (j == i):
    #             continue
    #         else:
    #             if (figureList[i] is Cube):
    #                 if figureList[i].collides_sphere(figureList[j]):
    #                     figureList[i].kill()
        
    
    
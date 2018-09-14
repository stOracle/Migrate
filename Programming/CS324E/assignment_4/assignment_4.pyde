from classes import *
import random

def setup():
    size (500, 500, P3D)
    frameRate(45)
    
    ball_1 = Ball(200,100,300)
    #ball_1.velocity(5,-5,-5)
    ball_1.velocity(5,-15,-5)
    ball_1.radius(50)
    ball_1.loss(.9)
    ball_1.gravity(1)
    
    ball_2 = Ball(-400,-300,-100)
    ball_2.velocity(-5,5,5)
    ball_2.radius(30)
    ball_2.loss(.95)
    ball_2.gravity(1)
    ball_2.col('#00F0DE')
    
    ball_3 = Ball(100,100,-300)
    ball_3.velocity(-5,10,7)
    ball_3.radius(20)
    ball_3.loss(.95)
    ball_3.gravity(1)
    ball_3.col('#EAE41A')
    
    ball_4 = Ball(400,200,0)
    ball_4.velocity(-2,5,10)
    ball_4.radius(80)
    ball_4.loss(.95)
    ball_4.gravity(1)
    ball_4.col('#1B1271')
    
    ball_t = Ball(50, -450, 0)
    #ball_1.velocity(5,-5,-5)
    ball_t.velocity(0,-20,0)
    ball_t.radius(50)
    ball_t.loss(.9)
    ball_t.gravity(1)
    
    Master_cube(0, 0, 0, 4, 100)
    #Master_cube(-500, -500, -500, 4, 100)
    print(str(len(cube_list)))
    print(str(len(sphere_list)))
    
    
    
def draw():
    background(0)
    lights()
    
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
            
    # Check for collisions
    
    # for i in range(len(cube_list)):
    #     for j in range(len(sphere_list)):
    #         if (cube_list[i].collides_sphere(sphere_list[j])):
    #             cube_list[i].col = "#6FFF5D"
                #sphere_list[j].update(cube_list[i])
                # if strike > 2:
                #     cube_list[i].visible = False
                
    # for i in range(len(figureList)):
    #     for j in range(len(figureList)):
    #         if (j == i):
    #             continue
    #         else:
    #             if (figureList[i] is Cube):
    #                 if figureList[i].collides_sphere(figureList[j]):
    #                     figureList[i].kill()
        
    
    
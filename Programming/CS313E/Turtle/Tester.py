#draws coordinate axes with dividers. 100 pixels = big tick, 50 = medium tick, 25 = small tick   
import turtle

def drawLine (ttl, x1, y1, x2, y2):

    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.penup()

def drawAxes(ttl, screenX, screenY):
    ttl.speed(0)
    
    #draws axes lines
    drawLine(ttl,0,screenY,0,-screenY)
    drawLine(ttl,screenX,0,-screenX,0)
    
    #draws x dividers
    for i in range (int((-screenX/2)/25+1),int((screenX/2)/25)):        
        if (i%4 == 0):
            j = i/4            
            drawLine(ttl, 100*j,30,100*j,-30)
        elif(i%2 == 0):
            j = i/2
            drawLine(ttl, 50*j,15,50*j,-15)
        else:
            drawLine(ttl, 25*i,5,25*i,-5)
    
    #draw y dividers        
    for i in range (int((-screenY/2)/25+1),int((screenY/2)/25)):
        if (i%4 == 0):
            j = i/4
            drawLine(ttl, 30,100*j,-30,100*j)
        elif(i%2 == 0):
            j = i/2
            drawLine(ttl, 15,50*j,-15,50*j)
        else:
            drawLine(ttl, 5,25*i,-5,25*i)

def main():
    turtle.setup(800, 800, 0, 0)
    ttl = turtle.Turtle()
    drawAxes(ttl, 400, 400)
    turtle.done()

main()
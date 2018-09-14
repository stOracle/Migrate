import time
from gui import *

actorList = []
inventory = []
up = False
down = False
right = False
left = False
Paused = False
startTime = time.time()
direction = 'up'

pauseText = None
timer = None
timerTime = 50
pauseStart = 0

playerAnimationR = [['Roy3.png', .1], ['Roy4.png', .1]]
playerAnimationL = [['Roy1.png', .1], ['Roy2.png', .1]]


def displayInventory(inv):
    global Paused    
    if (not Paused):
        for i in range(len(inv)):
            if (inv[i] != None):
                image(inv[i].sprite, i*36 + 210, 442)     

def pauseAll():
    global Paused
    global pauseStart
    global timerTime
    global pauseText
    if (Paused == False):
        pauseStart = time.time()
        pauseText = GUItext().text('PAUSED') \
                         .textSize(100) \
                         .position(120, 250) \
                         .textAlign(LEFT) \
                         .textColor('#0EE361')
    else:
        timerTime += int(time.time() - pauseStart)
        pauseText.kill()
        pauseText = None
    Paused = not Paused
    for actor in actorList:
        actor.paused = not actor.paused

def runClock(startTime):
    global timer
    global timerTime       
    if (Paused):
        pass
    elif (timer != None):
        currentTime = str(int(startTime - time.time()) + timerTime)
        timer.kill()        
        timer = GUItext().text(currentTime) \
                         .textSize(30) \
                         .position(305, 30) \
                         .textAlign(LEFT) \
                         .textColor('#050D9B')
    else:
        currentTime = str(int(startTime - time.time()) + timerTime)
        timer = GUItext().text(currentTime) \
                         .textSize(30) \
                         .position(305, 30) \
                         .textAlign(LEFT) \
                         .textColor('#050D9B')
    
    if (int(startTime - time.time()) + timerTime <= 0):
        endGame(False)

# Brings up the final scoreboard when called and ends the game                                                   
def endGame(win):    
    pauseAll()
    score = (len(inventory)*20 + int(startTime - time.time() + timerTime))
    for i in range(len(actorList)):
        actorList.pop(0)    
    for i in range(len(inventory)):
        inventory.pop(0)
    if (win):
        endText = "You've found the finish!"
        score += 100
    else:
        score = 0
        endText = "You've run out of time!"
    finishWindow = Window()
    finishWindow.size(640, 480)
    finishWindow.position(0,0)
    finishWindow.strokeWeight(3)
    
    GUItext(finishWindow).text(endText) \
                    .textSize(20) \
                    .position(315,30) \
                    .textAlign(CENTER) \
                    .textColor('#000000')
                    
    GUItext(finishWindow).text('Score: ' + str(score)) \
                    .textSize(20) \
                    .position(50,100) \
                    .textAlign(LEFT) \
                    .textColor('#000000')
                    


class Actor (object):
    
    # Allows you to set position and default sprite of an actor at creation.
    # If no sprite is given, will use a default image.    
    def __init__(self, x = 0, y = 0, sprite = "default_sprite.png"):
        self.x = x
        self.y = y               
        self.vx = 0.0
        self.vy = 0.0
        self.sprite = loadImage(sprite)
        self.paused = False        
        self.xcollider = self.sprite.width/2 #Dimensions for collision boundaries
        self.ycollider = self.sprite.height/2 #Set to size of the sprite by default
        self.xcenter = self.x + self.sprite.width/2
        self.ycenter = self.y + self.sprite.width/2
        self.hasCollision = True
        
        actorList.append(self)
    
    # Use to set the velocity of an actor    
    def Velocity(self, vx, vy):
        self.vx = vx
        self.vy = vy

    # Use to set the Position of an actor      
    def Position(self, x, y):
        self.x = x
        self.y = y

    # Use to change or set the default sprite of a actor        
    def Sprite(self, sprite):
        self.sprite = sprite

    # Takes a list of pairs of images and frame times and plays each frame in
    # the list for the amount of time given by its paired frame time (seconds)    
    #def Animation(self, frames):        
        
    
    # Flips the boolean value of whether or not the actor is paused        
    def Pause(self):
        self.paused = not self.paused   
    
    # Returns boolean based on if actor is colliding with another actor    
    def collideActor(self, other):        
        return ((abs(self.xcenter - other.xcenter) <= self.xcollider + other.xcollider and abs(self.ycenter - other.ycenter) <= self.ycollider + other.ycollider) and other.hasCollision)        
        
    def Update(self):
        
        # Update position based on velocities
        self.x += self.vx
        self.y += self.vy
        self.xcenter = self.x + self.sprite.width/2
        self.ycenter = self.y + self.sprite.height/2

    def Display(self):
        
        # Displays actor sprite
        image(self.sprite, self.x, self.y)
                 
class Player(Actor):
    
    def __init__(self, x = 0, y = 0, sprite = "default_sprite.png"):
       
       Actor.__init__(self, x, y, sprite)
       
       self.xcamera = width/2
       self.ycamera = height/2
       self.onEdge = False
    
     # this function is reponsible for player movement as well as world movement when the player reaches the edge of the screen 
    def Moveable(self):
        global direction
        if (self.paused == True):
            return
        if (keyPressed and (self.xcenter < 80 or self.xcenter > 560 or self.ycenter < 60 or self.ycenter > 420)):
            self.vy = 0
            self.vx = 0
            if ((keyCode == UP) and self.ycenter <= 60):
                for i in range (1, len(actorList)):
                    actorList[i].vy = 5
                    direction = 'up'                                                      
            if ((keyCode == LEFT) and self.xcenter <= 80):
                for i in range (1, len(actorList)):
                    actorList[i].vx = 5
                    direction = 'left'                                   
            if ((keyCode == RIGHT) and self.xcenter >= 560):
                for i in range (1, len(actorList)):
                    actorList[i].vx = -5
                    direction = 'right'  
            if ((keyCode == DOWN) and self.ycenter >= 420):
                for i in range (1, len(actorList)):
                    actorList[i].vy = -5
                    direction = 'down'
        else:
            for i in range (1, len(actorList)):
                actorList[i].vx = 0
                actorList[i].vy = 0
            self.vy = 0
            self.vx = 0
        
        if (keyPressed):
            if ((keyCode == UP) and self.ycenter > 60):
                self.vy = -6
                direction = 'up'                    
            if ((keyCode == LEFT) and self.xcenter > 80):
                self.vx = -6
                direction = 'left'
                self.sprite = loadImage('Roy1.png')
            if ((keyCode == RIGHT) and self.xcenter < 560):
                self.vx = 6
                direction = 'right'
                self.sprite = loadImage('Roy3.png')
            if ((keyCode == DOWN) and self.ycenter < 420):
                self.vy = 6
                direction = 'down'                
        else:
            for i in range (1, len(actorList)):
                actorList[i].vx = 0
                actorList[i].vy = 0
            self.vy = 0
            self.vx = 0    
               
class Item (Actor):
    
    def __init__(self, x = 0, y = 0, sprite = 'default_sprite.png', name = 'default_name'):
        
        Actor.__init__(self, x, y, sprite)
        self.name = name
        self.description = 'default_item_description'               
        
    def addInventory(self):
        if (len(inventory) >= 9):
            displayMessage = 'Inventory is full'
            print (displayMessage) #for debugging, can be added to UI later        
        else:
            inventory.append(self)                        
            print ('Item added to inventory') #for debugging            
            
def useItem(buttonPressed, player):
    global timerTime
    global direction
    buttonPressed = int(buttonPressed) - 1
    if (len(inventory) == 0 or buttonPressed >= len(inventory) or Paused == True):
        return
    if (direction == 'up'):
        xtranslation = 0
        ytranslation = -55
    elif (direction == 'left'):
        xtranslation = -55
        ytranslation = 0
    elif (direction == 'right'):
        xtranslation = 95
        ytranslation = 0
    elif (direction == 'down'):
        xtranslation = 0
        ytranslation = 95
    if (inventory[buttonPressed].name == 'Clock'):
        timerTime += 10
        inventory.pop(buttonPressed)
    else:
        inventory[buttonPressed].x = player.x + xtranslation
        inventory[buttonPressed].y = player.y + ytranslation
        if (inventory[buttonPressed].name != 'Bomb'):
            inventory[buttonPressed].hasCollision = False        
        actorList.append(inventory[buttonPressed])        
        inventory.pop(buttonPressed)
            
class Wall (Actor):
    
    def __init__(self, x = 0, y = 0, sprite = 'longvertwall.png'):
        
        Actor.__init__(self, x, y, sprite)
        
    def blockPlayer(self, player):
        
        if (player.xcenter < self.xcenter - self.sprite.width/2):
            player.x -= player.sprite.width/8
        elif (player.xcenter > self.xcenter + self.sprite.width/2):
            player.x += player.sprite.width/8
        if (player.ycenter < self.ycenter - self.sprite.height/2):
            player.y -= player.sprite.height/8
        elif (player.ycenter > self.ycenter + self.sprite.height/2):
            player.y += player.sprite.height/8
            
class Finish (Actor):
    
    def __init__(self, x = 0, y = 0, sprite = 'Finish.png'):
        
        Actor.__init__(self, x, y, sprite)
        

def make_lvl(diff):
    
    # stores all the walls
    wall_list = []
    
    
    
    # sets up different courses based on difficulty - easy, med, and hard
    if diff == 1:
        
        testItem = Item(215, 120, 'Bomb.png', 'Bomb')
        testItem2 = Item(315, 400, 'Clock.png', 'Clock')
        
        # these two set up the edges - or else the person could go around
        for i in range(7):
            wall_list.append(Wall(-30 + 100*i, -10, "shorthorzwall.png"))
            wall_list.append(Wall(-30 + 100*i, 455, "shorthorzwall.png"))

        for i in range(5):
            wall_list.append(Wall(-30, -10 + 100*i, "shortvertwall.png"))
            wall_list.append(Wall(635,-10 + 100*i, "shortvertwall.png"))
        
        wall_list.append(Wall(350, -10))
        wall_list.append(Wall(350, 355, "shortvertwall.png"))
        wall_list.append(Wall(250, 355, "shorthorzwall.png"))
        wall_list.append(Wall(150, 355, "shorthorzwall.png"))
        wall_list.append(Wall(5, 120, "shorthorzwall.png"))
        
        wall_list.append(Wall(100, 120, "shorthorzwall.png"))
        wall_list.append(Wall(260, 120, "shorthorzwall.png"))
        wall_list.append(Wall(260, 155, "shortvertwall.png"))
        wall_list.append(Wall(160, 219, "shorthorzwall.png"))
        wall_list.append(Wall(6, 219, "shorthorzwall.png"))
        
        wall_list.append(Wall(70, 219, "shortvertwall.png"))
        wall_list.append(Wall(335, 355, "longhorzwall.png"))
        
    if diff == 2:
                
        testItem = Item(215, 120, 'Bomb.png', 'Bomb')
        testItem2 = Item(590, 40, 'Clock.png', 'Clock')
        
        wall_list.append(Wall(350, -10))
        wall_list.append(Wall(350, 355, "shortvertwall.png"))
        wall_list.append(Wall(250, 355, "shorthorzwall.png"))
        wall_list.append(Wall(150, 355, "shorthorzwall.png"))
        wall_list.append(Wall(5, 120, "shorthorzwall.png"))
        
        wall_list.append(Wall(100, 120, "shorthorzwall.png"))
        wall_list.append(Wall(260, 120, "shorthorzwall.png"))
        wall_list.append(Wall(260, 155, "shortvertwall.png"))
        wall_list.append(Wall(160, 219, "shorthorzwall.png"))
        wall_list.append(Wall(6, 219, "shorthorzwall.png"))
        
        wall_list.append(Wall(70, 219, "shortvertwall.png"))
        wall_list.append(Wall(335, 355, "longhorzwall.png"))
        wall_list.append(Wall(440, 80))
        wall_list.append(Wall(540, -10))
        
        
         
from gameEngine import *

def setup():
    size (640, 480)
    frameRate(45)    
    
    # Initialize player and inventory NOTE: PLAYER MUST BE FIRST         
    playerActor = Player(60, 60, 'Roy1.png')
    playerActor.xcollider = 20
    playerActor.ycollider = 20
    inventory5 = Item(0, 0, 'FiveSprite.png', 'Five')
    inventory4 = Item(0, 0, 'FourSprite.png', 'Four')
    inventory3 = Item(0, 0, 'ThreeSprite.png', 'Three')
    inventory2 = Item(0, 0, 'TwoSprite.png', 'Two')
    inventory1 = Item(0, 0, 'OneSprite.png', 'One')   
    
    # Add items to inventory and remove them from ground
    for i in range(5, 0, -1):
        actorList[i].addInventory()
        actorList.pop(i)        
    
       
    startTime = time.time()
    
    #start with all actors and timer paused
    pauseAll()
        
    #Window for intro screen with instructions
    mainWin = Window()
    mainWin.size(640, 480)
    mainWin.position(0,0)
    mainWin.strokeWeight(3)
    
    GUItext(mainWin).text('Welcome to our maze game!') \
                    .textSize(20) \
                    .position(315,30) \
                    .textAlign(CENTER) \
                    .textColor('#000000')
                        
    GUItext(mainWin).text('The object of this game is to make it to the red finish circle before time runs out. \nYou can find items to assist you along the way. \nUse the arrow keys to move.\nUse 1-9 to use an item from your inventory.\nUse p to pause the game.\n Your score is based on time and items remaining in your inventory.\nClick one of the buttons below to start.') \
                    .textSize(14) \
                    .position(20, 60) \
                    .textAlign(LEFT) \
                    .textColor('#000000')
                    
                     
    # Function used to close out intro window and start game
    def closeMainWindow1():        
        global startTime        
        mainWin.kill()                       
        pauseAll()
        make_lvl(1)        
        inventoryWindow = Window()
        inventoryWindow.size(500, 36)
        inventoryWindow.position(70, 440)
        inventoryWindow.strokeWeight(2)
        GUItext(inventoryWindow).text('Inventory') \
                                .textSize(24) \
                                .position(10, 26) \
                                .textAlign(LEFT) \
                                .textColor('#000000')
        for i in range(9):
            RectButton(inventoryWindow).size(36,36) \
                                       .position(138 + i*36, 0) \
                                       .strokeWeight(2) \
                                       .text(str(i + 1))
    
    def closeMainWindow2():
        global startTime        
        mainWin.kill()               
        pauseAll()
        make_lvl(2)
        inventoryWindow = Window()
        inventoryWindow.size(500, 36)
        inventoryWindow.position(70, 440)
        inventoryWindow.strokeWeight(2)
        GUItext(inventoryWindow).text('Inventory') \
                                .textSize(24) \
                                .position(10, 26) \
                                .textAlign(LEFT) \
                                .textColor('#000000')
        for i in range(9):
            RectButton(inventoryWindow).size(36,36) \
                                       .position(138 + i*36, 0) \
                                       .strokeWeight(2) \
                                       .text(str(i + 1))                                                                    
    
    
            
    # Buttons used to close the intro window
    closeButton = RectButton(mainWin)
    closeButton.size(140,100) \
               .position(170, 350) \
               .strokeWeight(3) \
               .text("Easy") \
               .onClick(closeMainWindow1) \
               
               
    closeButton2 = RectButton(mainWin)
    closeButton2.size(140,100) \
                .position(320, 350) \
                .strokeWeight(3) \
                .text("Hard") \
                .onClick(closeMainWindow2) \                
               
        
        
def draw():
    
    background(255)
    
    runClock(startTime)
    
    if (len(actorList) != 0):
        actorList[0].Moveable()   
    
    # Check for player collisions and take appropriate action
    for i in range(1, len(actorList)):
        if (isinstance(actorList[i], Finish) and actorList[0].collideActor(actorList[i])):
            endGame(True)
            break
        if (isinstance(actorList[i], Item) and actorList[0].collideActor(actorList[i])):
            actorList[i].addInventory()
            actorList.pop(i)
            break
        if (isinstance(actorList[i], Wall) and actorList[0].collideActor(actorList[i])):
            actorList[i].blockPlayer(actorList[0])
                    

    # Check if a bomb is colliding with a wall and destroys both if true
    for i in range (1, len(actorList)):
        if (isinstance(actorList[i], Item)):
            if (actorList[i].name == 'Bomb'):
                for j in range (1, len(actorList)):
                    if (isinstance(actorList[j], Wall) and actorList[i].collideActor(actorList[j])):
                        actorList.pop(i)
                        actorList.pop(j)
                        break                       
    
    for actor in actorList:
        if not actor.paused:
            actor.Update()
        actor.Display() 
        
    displayGUI()
    displayInventory(inventory)
    
def keyPressed():
    if (key == '1' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6' or key == '7' or key == '8' or key == '9'):
        useItem(key, actorList[0])
    if (key == 'p' or key == 'P'):
        pauseAll()
    
def mousePressed():
    global pushed_GUI 
    pushed_GUI = GUIcollision()
    if pushed_GUI != None:
        pushed_GUI.isPushed = True
        pushed_GUI.pushAction()

def mouseReleased():
    global pushed_GUI
    if pushed_GUI == None: return
    pushed_GUI.isPushed = False
    
    # Mouse released while on top of the currently
    # pushed GUI object. That means the user has
    # clicked it! Call the clickAction!
    if pushed_GUI == GUIcollision():
        pushed_GUI.clickAction()
    else:
        pushed_GUI.releaseAction()
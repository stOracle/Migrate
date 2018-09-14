'''
This contains the entire GUI module as a single file.
To use it, append to the top line in a .pyde file:

from gui import *

Within the draw() function, you will need to include
this line of code:

displayGUI()

and also these lines of code:

def mousePressed():
    handleGUImousePress()

def mouseReleased():
    handleGUImouseRelease()

def mouseMoved():
    handleGUImouseMove()

Of course, I could include these as part of this file, but
I'm making it manual in case you need to add your own code
to the draw(), mousePressed(), mouseReleased(), and
mouseMoved() functions.
'''

global hoveredGUI
hoveredGUI = None

def handleGUImousePress():
    global pushed_GUI
    pushed_GUI = GUIcollision()
    if pushed_GUI != None:
        pushed_GUI.pushAction()
    redraw()

def handleGUImouseRelease():
    global pushed_GUI
    if pushed_GUI == None: return

    # Mouse released while on top of the currently
    # pushed GUI object. That means the user has
    # clicked it! Call the clickAction!
    if pushed_GUI == GUIcollision():
        pushed_GUI.clickAction()
    else:
        pushed_GUI.releaseAction()
    redraw()

def handleGUImouseMove():
    global hoveredGUI
    oldGUI = hoveredGUI
    hoveredGUI = GUIcollision()
    # Check if mouse passed over the previous GUI.
    if oldGUI != None and oldGUI != hoveredGUI:
        oldGUI.passAction()

    # Check if mouse is hovering over a new GUI.
    if hoveredGUI != None and hoveredGUI != oldGUI:
        hoveredGUI.hoverAction()

    redraw()

### GUI CLASSES DEFINED BELOW ###

### GUI HEART ###
# Essential GUI classes and functions are defined below.

global GUI_list
GUI_list = []

# Null function used for GUI actions
def doNothing():
    pass

'''
The essential properties of GUI objects are captured here.
In practice, you should never need to worry about the GUI class;
it's job is as a superclass to subclasses like
RectButton, Radio, Checkboxes, Window, etc.
However, you may use the generic GUI class as a parent to other
sub-GUI's to aid in grouping related GUI objects together.

GUI's come in hierarchies. Any GUI object can have "child" GUI's
whose properties are partially dependent on the parent.
For example: position of a child GUI is relative to the position of
the parent. Also, if a parent GUI is killed, so are all its children.
Children are added to a GUI object when the child object is constructed
For example, to add a button to a Window object named window1
type this:

button1 = RectButton(window1)

The assignment is optional. You could have just as well typed

RectButton(window1)

All GUI objects have associated "action" functions that can be called
upon certain events like clicking. For example, you may have a button
that prints "Hello World" to the screen when clicked. You would define
your sayHello() function and then call this method:

button1.onClick(sayHello)

Now whenever button1 is clicked the function sayHello() is called.
SYNTAX NOTE: To give a GUI an action function, you must type

GUI_object.onClick(function)

don't type

GUI_object.onClick(function())

i.e. don't pass in a function CALL to the .onClick() method, pass
the literal function into it!
To run a single line of code, defining a function in unnecessary.
You can use lambdas. Example: Change text of button.

button1.onClick(lambda: button1.text("You clicked me!"))

Also note that by default, child GUI's inherit the event actions
of their parents until you specify otherwise.'''
class GUI(object):
    # Constructor. Takes a parent as an input. The parent gets
    # this new object as a child.
    def __init__(self, parent=None):
        self.Name = ""
        self.x = 0
        self.y = 0
        self.type = "GUI"
        self.visible = True
        #self.style = "standard"
        self.isPushed = False
        self.parent = parent
        self.children = []
        GUI_list.append(self)
        if parent != None:
            parent.children.append(self)
            # Child inherits event actions from parent
            self.onPush(self.parent.pushAction)
            self.onRelease(self.parent.releaseAction)
            self.onClick(self.parent.clickAction)
            self.onHover(self.parent.hoverAction)
            self.onPass(self.parent.passAction)
        else:
            # Default event actions to do nothing.
            self.onPush(doNothing)
            self.onRelease(doNothing)
            self.onClick(doNothing)
            self.onHover(doNothing)
            self.onPass(doNothing)

    # Destructor
    def kill(self):
       # Remove all children of the object
       self.killChildren()
       # Remove self from parent's children list (if it has a parent)
       if self.parent != None:
           self.parent.children.remove(self)
       # Remove self from the GUI_list
       GUI_list.remove(self)
       del self

    # Kills all of the GUI's children
    def killChildren(self):
        for child in self.children[:]:
            child.kill()

    # Change the name of the GUI object.
    # Given no args, returns current name.
    def name(self, Name=None):
        if Name == None: return self.Name
        self.Name = Name
        return self

    # Changes the order of the given GUI to be in the place i
    # Higher i values mean more on top
    def order(self, i):
        global GUI_list
        i = i % len(GUI_list)
        GUI_list.remove(self)
        GUI_list = GUI_list[:i] + [self] + GUI_list[i:]

    # Moves the GUI object to the top of the GUI stack
    def onTop(self):
        self.order(-1)
        return self

    # Moves the GUI object to the bottom of the GUI stack
    def onBottom(self):
        self.order(0)
        return self

    # Makes the GUI object and all children visible (if they are displayable)
    # Passing True as optional arg hides the children too
    def show(self, includeChildren=False):
        self.visible = True
        if includeChildren:
            for child in self.children:
                child.show()
        return self

    # Makes the GUI object and all children invisible
    # Passing True as optional arg hides the children too.
    def hide(self, includeChildren=False):
        self.visible = False
        if includeChildren:
            for child in self.children:
                child.hide()
        return self

    # Returns whether the GUI object is considered visible
    def isVisible(self):
        return self.visible

    # Set position of the GUI object
    # Given no arguments, returns current position
    # Position is always relative to the parent's position
    # If the GUI object has no parent, position wrt screen origin.
    def position(self, x=None, y=None):
       if x==None:
           return self.x, self.y
       self.x = x
       self.y = y
       return self

    # Returns the coords of the object relative to the screen
    # as a tuple (x,y)
    def screenPosition(self):
        if self.parent == None:
            return self.x, self.y
        # Recursively find parent's screen position
        # and add it to self's position
        x,y = self.parent.screenPosition()
        return self.x + x, self.y + y
    '''
    # Change style
    def setStyle(self, style):
        self.style = style
        return self'''

    # Change function to call when object is pushed
    def onPush(self, func):
        self.pushAction = func
        return self

    # Change the function to call when object is released
    def onRelease(self, func):
        self.releaseAction = func
        return self

    # Does the same as onRelease(). Included for convenience.
    def onCancel(self, func):
        self.onRelease(func)
        return self

    # Change the function to call when object is clicked
    def onClick(self, func):
        self.clickAction = func
        return self

    # Change the function to call when mouse hovers over object
    def onHover(self, func):
        self.hoverAction = func
        return self

    # Change the function to call when mouse stops hovering
    def onPass(self, func):
        self.passAction = func
        return self

    def underMouse(self):
        return False

    # Basic GUI has no visual form.
    def display(self):
        pass

# Displays every visible GUI in the GUI_list
def displayGUI():
    for gui in GUI_list:
        if gui.isVisible(): gui.display()

# Checks if the mouse is over any GUI.
# If it is, returns the topmost such GUI.
def GUIcollision():
    for i in range(len(GUI_list)-1, -1, -1):
        if GUI_list[i].underMouse():
            return GUI_list[i]

# Returns the GUI object with the given name.
# If two GUI's have the same name, the one higher on
# the stack is chosen.
def getGUI(name):
    for i in range(len(GUI_list)-1, -1, -1):
        gui = GUI_list[i]
        if gui.name() == name:
            return gui

### BUTTONS ###

# This module contains the classes for buttons

'''
Button superclass is defined here.
You shouldn't use this class either! This class's job
is to be a superclass to specific buttons like
RectButton, RoundButton, etc.

Buttons have two main states: pushed and released.
You can change the fill of the button during each
state with the corresponding methods below.

Text on the button is specified using the
text() method.
Text size is set using the .textSize() method.'''
class Button(GUI):
    # Constructor
    def __init__(self, parent=None):
        GUI.__init__(self, parent)
        self.type = "Button"
        self.stroke = "#000000"
        self.weight = 1
        self.NormalFill = "#FFFFFF"
        self.PushedFill = "#888888"
        self.fill = self.NormalFill
        self.txt = ""
        self.txtSize = 12
        self.txtColor = "#000000"

    # Set text to be read on the button
    # Given no args, returns current text
    def text(self, txt=None):
        if txt==None:
            return self.txt
        self.txt = txt
        return self

    # Set text size
    # Given no args, returns current size
    def textSize(self, Size=None):
        if Size == None:
            return self.txtSize
        self.txtSize = Size
        return self

    # Change the color of the text on the button
    # Given no args, returns current color (as string)
    def textColor(self, col=None):
        if col == None:
            return self.txtColor
        self.txtColor = col
        return self

    # Change the stroke weight
    # Given no args, returns current weight
    def strokeWeight(self, w=None):
        if w == None:
            return self.weight
        self.weight = w
        return self

    # Change the stroke color.
    # col = string of the form "#HEXDEC"
    # Given no args, returns current color (as HEXDEC string)
    def strokeColor(col=None):
        if col == None:
            return self.stroke
        self.stroke = col
        return self

    # Change the ordinary fill of the button
    # Given no args, returns current normal fill (as string)
    def normalFill(self, col=None):
        if col == None:
            return self.NormalFill
        self.NormalFill = col
        self.updateFill()
        return self

    # Does the same thing as normalFill().
    # Included for convenience.
    def color(self, col=None):
        return self.normalFill(col)

    # Change the pushed fill of the button
    # Given no args, returns current pushed fill (as string)
    def pushedFill(self, col=None):
        if col == None:
            return self.PushedFill
        self.PushedFill = col
        self.updateFill()
        return self

    # Updates the current state of fill based on whether
    # the button is pushed or not. Mainly for internal use.
    def updateFill(self):
        if self.isPushed: self.fill = self.PushedFill
        else: self.fill = self.NormalFill
        return self

    ### Event methods need extra commands so that
    ### the fills change according to state.
    def onPush(self, pushAction):
        def action():
            self.isPushed = True
            self.fill = self.PushedFill
            pushAction()
        GUI.onPush(self, action)
        return self

    def onRelease(self, releaseAction):
        def action():
            self.isPushed = False
            self.fill = self.NormalFill
            releaseAction()
        GUI.onRelease(self, action)
        return self

    def onClick(self, clickAction):
        def action():
            self.isPushed = False
            self.fill = self.NormalFill
            clickAction()
        GUI.onClick(self, action)
        return self

    # This is a generic button, still nothing to display
    def display(self):
        pass

# This is the rectangular button class
class RectButton(Button):
    # Constructor
    def __init__(self, parent=None):
        Button.__init__(self, parent)
        self.type = "RectButton"
        self.W = 25
        self.H = 50

    # Change width of button
    # Given no args, returns current width
    def width(self, W=None):
        if W == None:
            return self.W
        self.W = W
        return self

    # Change height of button
    # Given no args, returns current height
    def height(self, H=None):
        if H == None:
            return self.H
        self.H = H
        return self

    # Does width() and height() together at the same time.
    # Input two arguments to set the width and height
    # Given no args, returns width and height as tuple (W,H)
    def size(self, W=None, H=None):
        if W == None:
            return self.W, self.H
        self.W = W
        self.H = H
        return self

    # Display the object
    def display(self):
        fill(self.fill)
        stroke(self.stroke)
        strokeWeight(self.strokeWeight())
        x, y = self.screenPosition()
        rect(x, y, self.width(), self.height())
        textAlign(CENTER, CENTER)
        textSize(self.textSize())
        fill(self.textColor())
        text(self.txt, x+self.width()/2, y+self.height()/2)

    # Detect whether the mouse is over the button or not
    # Note that this doesn't take into account GUI object order!
    def underMouse(self):
        x, y = self.screenPosition()
        return x <= mouseX <= x+self.width() and \
               y <= mouseY <= y+self.height()

# Round button class defined here
class RoundButton(Button):
    # Constructor
    def __init__(self, parent=None):
        Button.__init__(self, parent)
        self.type = "RoundButton"
        self.R = 20

    # Change radius of button
    # Given no args, returns current radius
    def radius(self, R=None):
        if R == None:
            return self.R
        self.R = R
        return self

    # Display the object
    def display(self):
        fill(self.fill)
        stroke(self.stroke)
        strokeWeight(self.strokeWeight())
        x, y = self.screenPosition()
        ellipse(x, y, 2*self.R, 2*self.R)
        textAlign(CENTER, CENTER)
        textSize(self.textSize())
        fill(self.textColor())
        text(self.txt, x, y)

    # Detect whether the mouse is over the button or not
    # Note that this doesn't take into account GUI object order!
    def underMouse(self):
        x, y = self.screenPosition()
        return dist(x,y, mouseX, mouseY) <= self.radius()

### WINDOW ###

# Window class defined

'''
This is the Window class. It's basically a big
Rectangular Button.'''
class Window(RectButton):
    # Constructor
    def __init__(self, parent=None):
        RectButton.__init__(self, parent)
        self.type = "Window"
        self.Title = ""
        self.width(200)
        self.height(100)
        self.normalFill("#8dceff")
        self.pushedFill("#8dceff")

    def color(self, col=None):
        if col == None: return self.normalFill()
        RectButton.pushedFill(self, col)
        RectButton.normalFill(self, col)
        self.updateFill()
        return self

### STATIC ###

# Static GUI classes defined here
# i.e. GUI objects that aren't very interactive
# e.g. GUItext and GUIimage.

'''
This is the class for adding text to GUI objects.
Note that buttons don't need this, as they have text
built-in.'''
class GUItext(GUI):
    # Constructor
    def __init__(self, parent=None):
        GUI.__init__(self, parent)
        self.type = "GUItext"
        self.txt = "Text"
        self.txtsize = 12
        self.W = 0
        self.H = 0
        self.col = "#000000"
        self.align = LEFT

    # What text will be shown?
    # If given no args, returns current text.
    def text(self, txt=None):
        if txt == None:
            return self.txt
        self.txt = txt
        return self

   # Change text size.
   # Given no args, returns current size.
    def textSize(self, size=None):
        if size == None:
            return self.txtsize
        self.txtsize = size
        return self

    # Change text color.
    # Given no args, returns current text color.
    def textColor(self, col=None):
        if col == None:
            return self.col
        self.col = col
        return self

    # Set the alignment of the text. Valid inputs are:
    # LEFT, CENTER, RIGHT, or any other valid argument
    # for the Processing textAlign() function.
    def textAlign(self, align=None):
        if align == None:
            return self.align
        self.align = align
        return self

    # Set width of the text box
    def width(self, W=None):
        if W == None: return self.W
        self.W = W
        return self

    # Set height of the text box
    def height(self, H=None):
        if H == None: return self.H
        self.H = H
        return self

    # Set width and height of the text box
    def size(self, W=None, H=None):
        if W == None: return self.W, self.H
        if H == None: H = W
        self.W = W
        self.H = H
        return self

    # Display text on the screen
    def display(self):
        x,y = self.screenPosition()
        textSize(self.txtsize)
        fill(self.col)
        textAlign(self.align, TOP)
        if self.width() == 0 or self.height() == 0:
            text(self.txt, x, y)
        else:
            text(self.txt, x, y, self.W, self.H)
'''
This is the class for rendering PImages on a GUI object.'''
class GUIimage(GUI):
    # Constructor
    def __init__(self, parent=None):
        GUI.__init__(self, parent)
        self.type = "GUIimg"
        self.img = None

    def image(self, img=None):
        if img==None: return self.img
        self.img = img
        return self

    def display(self):
        if self.img == None: return
        x,y = self.screenPosition()
        image(self.img, x, y)

### RADIO ###

# Radio Button classes defined here.

# RadioGroup class allows radio buttons to be grouped together.
# Children of RadioGroup are the associated radio buttons.
# Note that ONLY radio buttons can be children of a radio group!
class RadioGroup(GUI):
    # Constructor
    def __init__(self, parent=None):
        GUI.__init__(self, parent)
        self.activeChild = None

    # Activates the radio button radio in the radio group
    # Either radio button object can be given, or the index
    # of the radio button within the radio group's children list.
    # It's preferable to activate radio buttons from the .activate()
    # method within the radio BUTTON class, not the radio GROUP.
    # Mainly useful for activating based on index.
    def activate(self, radio):
        if type(radio) == type(0): radio = self.children[radio]
        if radio not in self.children:
            print("ERROR! Tried to activate radio button that is not part of radio group!")
            1/0
        radio.activate()
        self.activeChild = radio
        return self

    # Deactivates all the radio buttons in this radio group.
    def clear(self):
        for child in self.children: child.clear()

# RadioButton class allows for the creation of radio buttons
# in GUI's. RadioButton objects should almost always be
# children of a RadioGroup object (otherwise the RadioButton
# just degenerates into a checkbox, which might be what you
# want).
class RadioButton(RoundButton):
    # Constructor
    def __init__(self, parent=None):
        self.active = False
        self.zone = None
        RoundButton.__init__(self, parent)

    # RadioButtons require extra book keeping before destruction
    def kill(self):
        # Clear self in case it's active, so that the radio group
        # it's part of doesn't retain it as an active child.
        self.clear()
        RoundButton.kill(self)

    # Returns whether self is active or not.
    def isActive(self):
        return self.active

    # Quick method mainly for internal use. Returns whether this
    # radio button has a parent.
    def hasParent(self):
        return (self.parent != None)

    # Setting the radius scales the text size accordingly.
    # If you don't want radius changes to affect text, give
    # boolean False as the optional second argument.
    def radius(self, R=None, scaleText=True):
        if scaleText and R != None: self.textSize(1.5*R)
        return RoundButton.radius(self, R)

    # Change the width of the click zone that extends to the
    # right of the radio button. By default there is none.
    # Given 0 as input, zoneWidth() will kill the current
    # click zone. Given no args, returns current width
    # (returns 0 if there is no click zone)
    def clickZone(self, W=None):
        # If no argument given, return current width
        if W == None:
            if self.zone == None: return 0
            else: return self.zone.width()

        if self.zone == None:
            if W == 0: return self
            self.zone = RectButton(self)
            self.zone.position(-self.radius(), -self.radius()) \
                          .size(W, 2*self.radius()) \
                          .onPush(self.pushAction) \
                          .onRelease(self.releaseAction) \
                          .onClick(self.clickAction) \
                          .onHover(self.hoverAction) \
                          .onPass(self.passAction) \
                          .hide()
        elif W == 0: self.zone.kill()
        else: self.zone.width(W)
        return self

    ### Special book keeping needed for the event methods
    ### since a click zone might exist and need to be updated.
    def onPush(self, pushAction):
        RoundButton.onPush(self, pushAction)
        if self.zone != None: self.zone.onPush(self.pushAction)
        return self

    def onRelease(self, releaseAction):
        RoundButton.onRelease(self, releaseAction)
        if self.zone != None: self.zone.onRelease(self.releaseAction)
        return self

    # RadioButton requires special onClick() method to ensure
    # that radio button is activated when the click occurs.
    # Note that the button is activated BEFORE the clickAction
    # is called (in case that matters to your clickAction)
    def onClick(self, clickAction):
        def action():
            self.activate()
            clickAction()
        RoundButton.onClick(self, action)
        if self.zone != None: self.zone.onClick(self.clickAction)
        return self

    def onHover(self, hoverAction):
        RoundButton.onHover(self, hoverAction)
        if self.zone != None: self.zone.onHover(self.hoverAction)
        return self

    def onPass(self, passAction):
        RoundButton.onPass(self, passAction)
        if self.zone != None: self.zone.onPass(self.passAction)
        return self

    # Activates the radio button
    # Note: This won't call the clickAction!
    def activate(self):
        # Clear all radio buttons
        if self.hasParent():
            self.parent.clear()
            self.parent.activeChild = self
        # Activate THIS radio button.
        self.active = True
        return self

    # Deactivates the radio button
    def clear(self):
        if self.active and self.hasParent():
            self.parent.activeChild = None
        self.active = False
        return self

    # Does what .clear() does. Included for convenience.
    def deactivate(self):
        self.clear()
        return self

    # Reverses the radio button's active status.
    # active -> cleared; cleared -> active
    def toggle(self):
        if self.active: self.deactivate()
        else: self.activate()
        return self
    '''
    # Set on which side of the radio button the text will
    # appear. Given no args, returns current side.
    def textAlign(self, align=None):
        if align == None: return self.align
        self.align = align
        return self
    '''

    # Display the object
    def display(self):
        if self.isPushed: fill(self.PushedFill)
        else: fill(self.NormalFill)

        stroke(self.stroke)
        strokeWeight(self.strokeWeight())
        x, y = self.screenPosition()
        ellipse(x, y, 2*self.R, 2*self.R)

        if self.active:
            strokeWeight(0)
            fill("#000000")
            ellipse(x, y, self.R, self.R)

        textAlign(LEFT, CENTER)
        textSize(self.textSize())
        fill(self.textColor())
        trans = 2*self.radius()
        text(self.txt, x+trans, y)

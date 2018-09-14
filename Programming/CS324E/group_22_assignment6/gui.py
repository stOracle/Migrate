# GUI classes are defined below.

global GUI_list
GUI_list = []

# Null function used for GUI actions
def doNothing():
    pass

# Changes the order of the given GUI to be in the place i
# Higher i values mean more on top
def orderGUI(gui, i):
    global GUI_list
    if gui not in GUI_list:
        print("Object is not a GUI!")
        1/0
    i = i % len(GUI_list)
    GUI_list.remove(gui)
    GUI_list = GUI_list[:i] + [gui] + GUI_list[i:]

'''
The essential properties of GUI objects are captured here.
In practice, you should never need to worry about the GUI class;
it's job is as a superclass to subclasses like
RectButton, Radio, Checkboxes, Window, etc.

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
the literal function into it!'''
class GUI(object):
    # Constructor. Takes a parent as an input. The parent gets
    # this new object as a child.
    def __init__(self, parent=None):
        self.x = 0
        self.y = 0
        self.type = "GUI"
        #self.style = "standard"
        self.isPushed = False
        self.parent = parent
        self.children = []
        self.pushAction = doNothing  # Function to call when object is clicked
        self.releaseAction = doNothing  # Function to call when object is released
        self.clickAction = doNothing  # Function to call when object is fully clicked
        GUI_list.append(self)
        if parent != None:
            parent.children.append(self)
   
    # Destructor
    def kill(self):
       # Remove all children of the object
       for child in self.children:
           child.kill()
       # Remove self from the GUI_list
       GUI_list.remove(self)

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
    '''
    # Calls the action associated with object being pushed
    # Optionally provide a single argument to pass to the
    # action function
    def push(self, argument=None):
        self.isPushed = True
        if argument == None:
            return self.pushAction()
        return self.pushAction(argument)'''
    
    # Change the function to call when object is released
    def onRelease(self, func):
        self.releaseAction = func
        return self
    '''
    # Calls the action associated with the object being released
    # Optionally provide a single argument to pass to the
    # action function
    def release(self, argument=None):
        self.isPushed = False
        if argument == None:
            return self.releaseAction()
        return self.releaseAction(argument)'''
    
    # Change the function to call when object is clicked
    def onClick(self, func):
        self.clickAction = func
        return self
    '''
    # Calls the action associated with the object being clicked
    # Optionally provide a single argument to pass to the
    # action function
    def click(self, argument=None):
        if argument == None:
            return self.clickAction()
        return self.clickAction(argument)'''
    
    # Generic GUI is not clickable. Therefore when checking if mouse
    # is over, assume False, unless a method is given whereby to check
    def underMouse(self):
        return False
    
    # Basic GUI has no visual form.
    def display(self):
        pass

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
        self.txtCol = col
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
        return self
    
    # Change the pushed fill of the button
    # Given no args, returns current pushed fill (as string)
    def pushedFill(self, col=None):
        if col == None:
            return self.PushedFill
        self.PushedFill = col
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
    def width(self, W=None):
        if W == None:
            return self.W
        self.W = W
        return self
    
    # Change height of button
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
        if self.isPushed:
            fill(self.PushedFill)
        else:
            fill(self.NormalFill)
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

'''
This is the Window class. It's basically a big
Rectangular Button.'''
class Window(RectButton):
    # Constructor
    def __init__(self, parent=None):
        RectButton.__init__(self, parent)
        self.type = "Window"
        self.width(200)
        self.height(100)
        self.normalFill("#8dceff")
        self.pushedFill("#8dceff")

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
        self.size = 12
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
            return self.size
        self.size = size
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
    
    # Display text on the screen
    def display(self):
        x,y = self.screenPosition()
        textSize(self.size)
        fill(self.col)
        textAlign(self.align)
        text(self.txt, x, y)

def displayGUI():
    for gui in GUI_list:
        gui.display()

def GUIcollision():
    for i in range(len(GUI_list)-1, -1, -1):
        if GUI_list[i].underMouse():
            return GUI_list[i]
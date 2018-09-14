'''
GUI MANUAL

To use the GUI classes, append the following to the top line
in your .pyde file:

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

Of course, I could include these as part of gui.py, but
I'm making it manual in case you need to add your own code
to the draw(), mousePressed(), mouseReleased(), and
mouseMoved() functions.

### SYNTAX ###

These are the main GUI classes you should be needing:

GUI
RectButton
RoundButton
Window
GUItext
GUIimage
RadioGroup
Radio

To create an instance of one of the objects, type:

yourWindow = Window()

The assignment is optional, but you probably want to
so you can modify the object after creation.

Once a GUI object is created you can modify its attributes
with various methods. Usually you'll want to set attributes
like position and size at least. If you've named your GUI
object like I did above, you can set the attributes like this:

yourWindow.position(25, 50)
yourWindow.size(400, 300)
yourWindow.color("#FFFF88")  # Makes a light yellow fill
yourWindow.strokeWeight(3)  # How thick is the window border?

It can be repetitive to keep retyping yourWindow over and over.
Since most of the methods used to change attributes return the
modified object, you can string such commands together like so:

yourWindow.position(25, 50).size(400, 300).color("#FFFF88")

or even more cleanly using python's line continuation symbol \

yourWindow.position(25, 50) \
          .size(400, 300) \
          .color("#FFFF88") \
          .strokeWeight(3)

Most attribute-changing methods can also be called without inputs
to return the current attribute. Like if you want to store the
current color of your window as a string, type:

winColor = yourWindow.color()

Finally, GUI objects are meant to come in hierarchies, and so a
single GUI object can have multiple children whose properties are
partially dependent on their parent. For example, a child object's
position is always with respect to the position of its parent.
That way, if you change the position of the parent, all of its
children move accordingly. To make a GUI object a child of another
GUI object, define it so during construction like so:

yourButton = RectButton(yourWindow)

The rectangular button called yourButton now has its position
with respect to the origin of yourWindow. Existence of a child
is also dependent on the parent. If you delete a GUI object, all
of its children are deleted also.

### EVENTS ###

The point of GUI's is to be interactive of course, so here I'll
talk about how to make the various GUI's do things when certain
events happen.

There are five events that GUI objects can handle:

Mouse Push -- User clicks mouse down, but does not release yet.
Mouse Release -- User clicks mouse down, but cancels by releasing
                 somewhere else.
Mouse Click -- User clicks mouse down, and completes the click
               by releasing while over the same object.
Mouse Hover -- Mouse hovers over object
Mouse Pass -- Mouse stops hovering over object

When any of these events happen, you can tell the GUI object to
run a function you specify which I'll call an "action". The most
common event to respond to is the complete "click" for buttons.

Suppose you want a button that changes some text and then destroys
itself. You would define a function in-line like so:

def destroy():
  text1.text("You clicked the kill button!")
  button1.kill()

And then set button1 to call this destroy() function when clicked:

button1.onClick(destroy)

CAUTION! Be sure you pass in the function NAME to the onClick() method
and not the function CALL. I.e. DON'T type:

button1.onClick(destroy())

Often times, the action you want a button to take only requires a single
line of code. In that case, you do not need to define a whole function
like we did above with destroy(). Suppose you have a button that should
close the main window. That requires only a single line of code. In that
case, you can use python lambdas and type:

closeButton.onClick(lambda: mainWindow.kill())

In general, if you only have ONE line of code to execute as an action,
then you may type:

object1.onClick(lambda: [line of code you want to run])

The other "on" methods work similarly.

A few things to note:
* Often times you don't want an object to do ANYTHING on one of these
  events (like when mouse is released). In that case, I provide the
  built-in function doNothing() for those cases. If you want nothing
  to happen when the user cancels a click, you'd type:

  button1.onRelease(doNothing)

* By default, GUI objects inherit the event actions of their
  parents. So if you place a button inside a button, the child button
  will, by default, do what the parent button does until you specify
  otherwise.
* If a GUI has no parent, then by default all of its event actions are
  set to doNothing.
* Some GUI objects (like the static objects GUItext and GUIimage) are
  not made to be interactable. You can still assign event actions to
  them, but they'll never be called. However, sometimes you want
  something to happen when the user clicks, say, an image. In that case,
  I'd make the GUIimage in question a child of a button object, give
  the button object the event action you want, and then make the button
  invisible with the .hide() method.

### GUI HEART ###

-=GUI class=-
This is the generic GUI object. Every other GUI object inherits
from this class. It defines the most fundamental methods that
virtually all the other GUI objects need. It is mainly for internal
use, and as a user, you should probably have little need to actually
define your own generic GUI object (as it is not even displayable).
However, it may be useful to you as a parent to children.
E.g. if you want to have a bunch of GUI images all grouped together
so you can delete them all at once when need comes.

Methods:

kill()
Deletes the GUI object and all of its children if it has any

order(i)
Changes the position of the object on the GUI stack. Like if you
want to move one window to be on top of another. In practice, I've
never used this method since GUI object order is established by the
order of GUI construction. It also doesn't have inheritance properties
(i.e. reordering an object won't reorder its children too).
You probably won't need to use this method.

onTop()
Moves the GUI object to the top of the stack

onBottom()
Moves the GUI object to the bottom of the stack

name(Name)
Optionally give a name to your GUI object. Calling the method
without any arguments returns the current name. You can grab a
GUI object by name by using the getGUI() function.
By default, GUI's have the empty string "" as their name.

getGUI(Name)
This is not a method in the GUI class, but it is a function you
can call. getGUI(Name) returns the GUI object with the given Name.
If no GUI has that Name, None is returned.
If multiple GUI's have that Name, the top-most GUI is returned.

show([includeChildren])
Makes the GUI object visible. Optionally pass in boolean True to make
children visible too.

hide([includeChildren])
Makes the GUI object invisible. Optionally pass in boolean True to
make children invisible too.

isVisible()
Returns boolean on whether the object is currently visible or not.

position(x,y)
Set position of the GUI object with respect to the parent (or the screen
origin if it has no parent). Given no args, returns current position as
tuple (x,y). Optionally you can grab x- or y-components by reading in
X = myObject.x
Y = myObject.y

screenPosition()
Returns position of object with respect to the screen origin as a tuple
(x,y). Mainly for internal use, but maybe you'll need it.

onPush(func)
Set the function to call when the GUI object is pushed. "Pushed" means
the mouse has clicked the object, but not released yet.

onRelease(func)
Set the function to call when the GUI object is released. "Released"
means the mouse has clicked the object, but then released AWAY from
the object. This is like "canceling" a click.

onCancel(func)
Same as onRelease(). Provided for coding convenience.

onClick(func)
Set the function to call when the GUI object is clicked. "Clicked"
means the mouse has clicked the object, but then release WHILE STILL
OVER the object.

onHover(func)
Set the function to call when the mouse hovers over the object.
Note that this function only gets called ONCE when the mouse comes over
the object FOR THE FIRST TIME. It is NOT called every frame that the
mouse happens to be over the object.

onPass(func)
Set the function to call when the mouse stops hovering over the object.

underMouse()
Mainly for internal use. Returns boolean on whether or not the mouse
is currently over the object i.e. the object is UNDER the mouse.

display()
Mainly for internal use.
Displays the GUI object. This method will display the object REGARDLESS
of whether or not the GUI object is considered "visible" or not. You'll
need to check yourself with isVisible() before you call this function.

.children
Mainly for internal use.
This is not a method but a field. It consists of a list of the children
of the GUI object. Access it by typing: myObject.children

.parent
Mainly for internal use.
This is not a method but a field. It contains the parent of the object.
If it has no parent it is set to the python object None.
Access it by typing: myObject.parent

.isPushed
Mainly for internal use.
This is not a method, but a field. It is a boolean indicating whether
the current object is currently in the "pushed" state by the mouse.

### BUTTONS ###

-=Button class=-
You probably won't need to use this class, as its main purpose is to be
a superclass to the RectButton and RoundButton class. So it's mainly for
internal use again. However, I'll go over its methods since both
RectButton and RoundButton have them.

text(txt)
Sets the text that will appear on the button.
Given no inputs, returns current text (as string).

textSize(Size)
Set the size of the text.
Given no inputs, returns current text size (as num).

textColor(col)
Set the color of the text. Pass in string of the form "#HEXDEC"
Given no inputs, returns current color (as string).

strokeWeight(w)
Set the border thickness.
Given no inputs, returns current thickness (as num).

strokeColor(col)
Set the border color. Pass in string of form "#HEXDEC"
Given no inputs, returns current border color (as string).

normalFill(col)
Set the unpushed fill color of the button.
Pass in string of form "#HEXDEC".

color(col)
Same as normalFill(). Included for coding convenience.

pushedFill(col)
Set the pushed fill color of the button.
Pass in string of form "#HEXDEC".

updateFill()
Mainly for internal use.
Updates the current state of fill based on whether
the button is currently pushed or not.

-=RectButton class=-
Define rectangular buttons here.
Unique methods defined below:

width(W)
Set the width of the button.

height(H)
Set the height of the button.

size(W, H)
Set the width AND height of the button at the same time.

-=RoundButton class=-
Define round buttons here.
Unique methods defined below:

radius(R)
Set radius for the button.

### WINDOWS ###

=-Window class=-
Windows are defined here. They are essentially big
rectangular buttons and share the methods that they have.
Unique methods defined below:

color(col)
Set the interior fill of the window.

### STATIC GUIs ###

Static GUIs consist of GUItext and GUIimage. They are called
"static" since they are not very interactable (for example:
event actions are never called for static GUIs, even though
you can set them.) If you want to make a static GUI interactable,
I suggest making them a child of an invisible, interactive GUI
like a button.

-=GUItext class=-
Put text on the screen (or another GUI object)
Unique methods defined below:

text(txt)
Set what the text is.

textSize(size)
Set the size of the text.

textColor(col)
Set the color of the text.

textAlign(align)
Set position of origin for the GUItext object.
By default, this is set to LEFT which means the position of a
GUItext object is with respect to the upper-left corner.
Changing it to CENTER or RIGHT will make the object's position
relative to the upper-center and upper-right respectively.
CENTER is especially useful for if you want to, say, put a title
on a Window object.
Syntax: yourText.textAlign(CENTER)

width(), height(), and size()
Optional. Setting a non-zero width AND height defines an invisible
box around the GUItext object whereby the text will word wrap as
required.

-=GUIimage class=-
Allows you to put Processing PImages on the screen or other GUIs
Unique methods defined below:

image(img)
Set the image to display. img needs to be a Processing PImage type.

### RADIO BUTTONS ###

-=RadioGroup class=-
Radio buttons need to be children of a RadioGroup object so that only
one radio button at a time in the group may be active.
IMPORTANT: The only children allowed for a RadioGroup object are
RadioButton objects!! DON'T GIVE IT ANY OTHER CHILDREN!!!
Unique methods defined below:

activate(radio)
Activates the radio button specified. This can either be the actual
radio button OBJECT, or can be an index into the RadioGroup's
children list.
Note that calling this method WON'T call any click action associated
with the radio button specified.

clear()
Deactivates all of the radio buttons in the group.

-=RadioButton class=-
Radio buttons are defined here. Note that they really should be
the children of some radio group. Making them the children of some
other class could cause the GUI module to crash! And anyway, it'd
probably be useless.
One other minor note: if you decide to assign a click action to
a radio button, that click action will be called BEFORE the state
of the button is changed to being activated.
Unique methods defined below:

isActive()
Returns boolean on whether the radio button is currently active.

hasParent()
Mainly for internal use. Returns boolean on whether this button
has a parent. (Again, it really always should!)

radius(R, [scaleText])
Set the radius for the radio button.
By default, changing the radius will change the text size
to match, but this can be prevented by providing an additional
optional argument False to the radius() method.

clickZone(W)
Creates a "click zone" extending over the text of the radio button.
W denotes the width of this "click zone". If you don't specify a
click zone width, then the only way to activate a radio button is
to actually click the round button itself. With an appropriately chosen
click zone width, you can click the text and activate the button too.
Note that click zone applies to more than just clicking. It is also a
"hover zone".

activate()
Activates the radio button.
Note that this WON'T call the click action.

clear()
Deactivates the radio button.

deactivate()
Same as clear(). Included for coding convenience.

toggle()
Reverses the radio button's active status.
Deactivates an active button, and activates a deactivated one.
'''

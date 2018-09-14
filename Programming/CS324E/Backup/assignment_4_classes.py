figureList = []

'''
The universal class. All figures will inherit the basic fields of this class:
Position, Orientation, Velocity, Angular speed, Axis of rotation, Gravity.
Position can be set from the constructor, but the others are set from their
corresponding methods.
The class also includes methods for rudimentary control of the figure:
Showing, Hiding, Pausing, Removal'''

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        
    # create a string representation of a Point (x, y, z)
    def __str__ (self):
        s = "({}, {}, {})".format(str(self.x), str(self.y), str(self.z))
        return s

    # get distance to another Point object
    def distance (self, other):
        core_x = (self.x - other.x) ** 2
        core_y = (self.y - other.y) ** 2
        core_z = (self.z - other.z) ** 2 
        d = (core_x + core_y + core_z) ** .5
        return d

    # test for equality between two points
    def __eq__ (self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)


class Figure(object):
    '''
    Constructor.
    (x,y,z) = Position in world space. Defaults to the origin.
    Other parameters are set using the methods found below'''
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
        # Default values given for the other fields
        self.thX = 0.0
        self.thY = 0.0
        self.thZ = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0
        self.omega = 0.0
        self.axisX = 0.0
        self.axisY = 0.0
        self.axisZ = 1.0
        self.g = 0.0
        self.L = 1.0
        self.visible = True
        self.paused = False

        figureList.append(self)

    # Set position of figure. Given no arguments, returns current position (as triplet).
    # To change individual components, assign values to the fields .x .y and .z
    def position(self, x=None, y=None, z=None):
        if x==None:
            return self.x, self.y, self.z
        self.x = x
        self.y = y
        self.z = z
    
    # Set orientation of figure. Given no arguments, returns current orientation (as triplet).
    # To change individual components, assign values to the fields .thX .thY and .thZ
    def orient(self, thX=None, thY=None, thZ=None):
        if thX==None:
            return self.thX, self.thY, self.thZ
        self.thX = thX
        self.thY = thY
        self.thZ = thZ
    
    # Set velocity of the figure. Given no arguments, returns the current velocity (as triplet)
    # To change individual components, assign values to the fields .vx .vy and .vz
    def velocity(self, vx=None, vy=None, vz=None):
        if vx==None:
            return self.vx, self.vy, self.vz
        self.vx = vx
        self.vy = vy
        self.vz = vz
    
    # Set rotation speed. Given no arguments, returns the current rotation speed.
    def angSpeed(self, omega=None):
        if omega==None:
            return self.omega
        self.omega = omega
    
    # Set rotation axis. Given no arguments, returns the current axis (as triplet).
    # To change individual components, assign values to the fields .axisX .axisY and .axisZ
    def axis(self, axisX=None, axisY=None, axisZ=None):
        if axisX==None:
            return self.axisX, self.axisY, self.axisZ
        self.axisX = axisX
        self.axisY = axisY
        self.axisZ = axisZ
    
    # Set gravity. Given no arguments, returns the current gravity.
    def gravity(self, g=None):
        if g==None:
            return self.g
        self.g = g
    
    # Set loss factor. Y-velocity will be multiplied by this factor after each bounce.
    def loss(self, L=None):
        if L==None:
            return self.L
        self.L = L 

    # Destructor. Removes the figure from the scene.
    def kill(self):
        figureList.remove(self)

    # Makes the figure visible
    def show(self):
        self.visible = True

    # Makes the figure invisible
    def hide(self):
        self.visible = False

    # Prevents the figure from being updated
    def pause(self):
        self.paused = True

    # Allows the figure to be updated
    def resume(self):
        self.paused = False

# Master_cube is the initial giant cube that is able to be broken
# it is a ixjxk grid of cubes, where when one of the cubes is collided with,
# it chips off and gains gravity, thus falling.
# class Master_cube(Figure):

#     def __init__ (self, x = 0, y = 0, z = 0, dim = 0, sidelength = 0):
#         # (x, y, z) will represent the corner of the front-left corner of the cube
#         # sidelength represents the length of the MasterCube's side.
#         # the dim is how many cubes in the x direction.
#         # if dim is 5, there are 125 cubes making mastercube.

#         Figure.__init__(self, x, y, z)

#         self.L = 0
#         self.dim = dim
#         self.g = 0

#         start = [self.x, self.y, self.z]

#         for i in range(dim):
#             for j in range(dim):
#                 for k in range(dim):
#                     cube = Cube(start[0] + (i * sidelength), 
#                         start[1] + (j * sidelength), start[2] + (k * sidelength))

                    


# # The Cube class. Inherits from Figure.
# class Cube(Figure):
#     # Constructor. Takes all parameters that Figure does, as well as other parameters
#     # specific to the Cube class.
#     def __init__(self, x = 0, y = 0, z = 0):

#         # Use Figure's constructor to initialize the universal fields
#         Figure.__init__(self, x, y, z)

#         # orig is the front left point on the cube (origin)
#         self.orig = Point(x, y, z)

#         self.S = 20
#         self.col = ("#C1BBBB")
#         self.L = 0

#         # Assign other fields specific to the Cube class (e.g. color?)
#         #self.etc = etc

#     # Set sidelength of bcube. Given no arguments, returns the current sidelength.
#     def side(self, S = None):
#         if (S == None):
#             return self.S
#         self.S = S

#     def col(self, C=None):
#         if (C ==None):
#             return self.C
#         self.C = C

#     # determines if a point is inside the cube
#     def is_inside_point (self, p):

#         x_in = (p.x > self.orig.x) and (p.x < self.orig.x + self.S)
#         y_in = (p.y > self.orig.y) and (p.y < self.orig.y + self.S)
#         z_in = (p.z > self.orig.z) and (p.z < self.orig.z + self.S)
    
#         return (x_in and y_in and z_in)



#     # Given a sphere, returns boolean on whether self is colliding with it
#     # def collides(self, other):

#     #     x = other.center.x
#     #     y = other.center.y
#     #     z = other.center.z

#     #     x_in = True
#     #     y_in = True
#     #     z_in = True

#     #     if (x < self.center.x) or (x > self.center.x + self.side):
#     #     if (y < self.center.y) or (y > self.center.y + self.side):
#     #     if (z < self.center.z) or (z > self.center.z + self.side):






#         return None
        

#         # Etc

#     def chip(self, other):
#         pass

#     # Return list of all figures this object is colliding with in this frame
#     def collisions(self):
#         pass
#         # Perhaps collisions can be detected by for-looping thru the figureList?

#     # Code that updates this cube's fields for the next frame
#     def update(self):
#         #if self.collides(other)

#         # Increment position by velocity
#         self.x += self.vx
#         self.y += self.vy

#         # Increment vertical velocity
#         self.vy += self.g
        

#         # Check for collisions and respond accordingly
#         # Check if self is near the ground and whether to explode
#         # If self explodes, kill it: self.kill()
#         # Etc

#     # Code that displays the cube based on the current fields
#     def display(self):
#         noStroke()
#         pushMatrix()
#         translate(self.x, self.y, self.z)
#         fill(self.C)
#         cube(self.S)
#         popMatrix()

# Example ball class
class Ball(Figure):
    # Constructor. Takes same arguments as Figure
    def __init__(self, x=0.0, y=0.0, z=0.0):
        # Use Figure's constructor to initialize the universal fields
        Figure.__init__(self, x, y, z)

        # Default radius to 10, color to red, loss factor to 1
        self.center = Point(x, y, z)
        self.R = 10.0
        self.C = "#FF0000"
        self.L = 1.0
    
    # Set radius of ball. Given no arguments, returns the current radius.
    def radius(self, R=None):
        if R==None:
            return self.R
        self.R = R
    
    # Set color of ball (as string). Given no arguments, returns the current color (as string). 
    def col(self, C=None):
        if (C ==None):
            return self.C
        self.C = C

    # Updates the fields of the ball depending on its current state in the scene
    def update(self):
        # If ball is out-of-bounds, reverse relevant velocities
        if not(self.R < self.x < width-self.R):
            self.x -= self.vx  # Move to within boundary
            self.vx = -self.vx
        if not (self.R < self.y < height-self.R):
            self.y -= self.vy  # Move to within boundary
            self.vy = -self.vy*self.L
        if not(-400 < self.z < 200-self.R):
            self.z -= self.vz
            self.vz = -self.vz

        # Increment position by velocity
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

        # Increment vertical velocity
        self.vy += self.g

    # Displays the ball on the screen
    def display(self):
        noStroke()
        pushMatrix()
        translate(self.x, self.y, self.z)
        fill(self.C)
        #ellipse(self.x, self.y, self.R*2, self.R*2)
        sphere(self.R)
        popMatrix()
figureList = []
sphere_list = []
cube_list = []

'''
The universal class. All figures will inherit the basic fields of this class:
Position, Orientation, Velocity, Angular speed, Axis of rotation, Gravity.
Position can be set from the constructor, but the others are set from their
corresponding methods.
The class also includes methods for rudimentary control of the figure:
Showing, Hiding, Pausing, Removal'''

def Master_cube(x, y, z, dim, sideL):
    # (x, y, z) will represent the corner of the front-left corner of the cube
    # sidelength represents the length of the MasterCube's side.
    # the dim is how many cubes in the x direction.
    # if dim is 5, there are 125 cubes making mastercube.
        start = [x, y, z]

        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    cube = Cube(start[0] + (i * sideL), 
                        start[1] + (j * sideL), start[2] + (k * sideL), sideL)
                    
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
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
        # Default values given for the other fields
        self.thX = 0
        self.thY = 0
        self.thZ = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.omega = 0
        self.axisX = 0
        self.axisY = 0
        self.axisZ = 1
        self.g = 0
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

    # Destructor. Removes the figure from the scene.
    def kill(self):
        cube_list.remove(self)
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

# The Cube class. Inherits from Figure.
class Cube(Figure):
    # Constructor. Takes all parameters that Figure does, as well as other parameters
    # specific to the Cube class.
    def __init__(self, x = 0, y = 0, z = 0, sideL = 0):

        # Use Figure's constructor to initialize the universal fields
        Figure.__init__(self, x, y, z)
        
        # orig is the front left point on the cube (origin)
        self.orig = Point(x, y, z)
        if (sideL == None):
            self.sideL = 0
        else:
            self.sideL = sideL    
        self.col = ("#C1BBBB")
        self.L = 0
        # touch counts how many times the cube has been touched
        #self.touch = 0        
        cube_list.append(self)

    # Set sidelength of cube. Given no arguments, returns the current sidelength.
    # def side(self, S = None):
    #     if (S == None):
    #         return self.S
    #     self.S = S

    def col(self, C=None):
       if (C ==None):
           return self.C
       self.C = C

    # determines if a point is inside the cube
    def is_inside_point (self, p):

        x_in = (p.x >= self.orig.x - .5 * self.sideL) and (p.x <= self.orig.x + .5 * self.sideL)
        y_in = (p.y >= self.orig.y - .5 * self.sideL) and (p.y <= self.orig.y + .5 * self.sideL)
        z_in = (p.z >= self.orig.z - .5 * self.sideL) and (p.z <= self.orig.z + .5 * self.sideL)
    
        return (x_in and y_in and z_in)

    # Given a sphere, returns boolean on whether self is colliding with it
    def collides_sphere(self, other):
        
        # if self.visible == False:
        #     return False
        if self.is_inside_point(other.center):
            return True
        else:
            return False
        
        # distance = self.orig.distance(other.center)
        # if (distance <= other.R + 10):
        #    return True
        # else:
        #    return False
        
        # x = other.center.x
        # y = other.center.y
        # z = other.center.z
        # r = other.R
        # index = [-1, 1]
            
        # for i in range (3):
        #    for j in range (2):
        #        if (i == 0):
        #            place = Point(x + r * index[j], 0, 0)
        #        elif (i == 1):
        #            place = Point(0, y + r * index[j], 0)
        #        else:
        #            place = Point(0, 0, z + r * index[j])
        #        if self.is_inside_point(place):
        #            return True
        # return False
    
      # if (x < self.center.x) or (x > self.center.x + self.side):
      # if (y < self.center.y) or (y > self.center.y + self.side):
      # if (z < self.center.z) or (z > self.center.z + self.side):
          
    def is_hit (self):
        self.touch = 0
        self.cols = []
        count = 0
        for ball in sphere_list:
            if self.collides_sphere(ball):
                count += 1
                self.cols.append(ball)
        
        return count
        #return False
        # return self.cols
 
    def update(self):
        
        count = self.is_hit()
        if (count > 0):
            self.C = ("#86FFB7")
        elif (count == 0):
            self.C = ("#FF8686")
        print(str(count))
            
            
        
        #self.C = ("#86FFB7")
        
        # if self.is_hit:
        #     self.C = ("#86FFB7")
        # else:
        #     self.C = ("#FF8686")
        # for said cube, makes a list of all spheres touching it
        # if (len(cols) > 0):
        #     for i in range(len(cols)):
        #         self.touch += 1
        # if (self.touch > 0):
        #     self.C = ("#6FFF5D")
        
            #self.C = (100 + self.touch*2, 150 + self.touch*2, 200 - self.touch)
            
        # Increment position by velocity
        # self.x += self.vx
        # self.y += self.vy

        # # Increment vertical velocity
        # self.vy += self.g
        
    def display(self):
        stroke(0)
        #noStroke()
        strokeWeight(2)
        pushMatrix()
        translate(self.x, self.y, self.z)
        fill(self.C)
        box(self.sideL, self.sideL, self.sideL)
        popMatrix()

# Example ball class
class Ball(Figure):
    # Constructor. Takes same arguments as Figure
    def __init__(self, x=0, y=0, z=0):
        # Use Figure's constructor to initialize the universal fields
        Figure.__init__(self, x, y, z)
        
        self.center = Point(self.x, self.y, self.z)
        
        # Default radius to 10 and color to red
        self.R = 10
        self.C = "#FF0000"
        self.L = 1
        
        sphere_list.append(self)
    
    # Set radius of ball. Given no arguments, returns the current radius.
    def radius(self, R=None):
        if R==None:
            return self.R
        self.R = R
    
    # Set color of ball (as string). Given no arguments, returns the current color (as string). 
    def col(self, C=None):
        if C==None:
            return self.C
        self.C = C
    
    def loss(self, L=None):
        if L==None:
            return self.L
        self.L = L

    # Updates the fields of the ball depending on its current state in the scene
    def update(self):
        # If ball is out-of-bounds, reverse relevant velocities
        if (self.x + self.R >= 500) or (self.x - self.R <= -500):
            self.x -= self.vx
            self.vx = -self.vx
        if (self.y + self.R >= 500) or (self.y - self.R <= -500):
             self.y -= self.vy             
             self.vy = -self.vy*self.L           
        if (self.z + self.R >= 500) or (self.z - self.R <= -500):
            self.z -= self.vz
            self.vz = -self.vz
        # if other != None:
        #     if (other.collides_sphere(self)):
        #         self.pause()
                # self.x -= self.vx
                # self.vx = -self.vx
                # self.y -= self.vy
                # self.vy = -self.vy*self.L
                # self.z -= self.vz
                # self.vz = -self.vz
            

        # Increment position by velocity
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        
        #gravity
        self.vy += self.g
        
        # if ((other != None) and (other.collides_sphere(self))):
        #     #self.pause()
        #     other.visible = False
        #     other.kill()

    # Displays the ball on the screen
    def display(self):
        noStroke()
        pushMatrix()
        translate(self.x, self.y, self.z)
        fill(self.C)
        #ellipse(self.x, self.y, self.R*2, self.R*2)
        sphere(self.R)
        popMatrix()
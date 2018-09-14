from timer import *
from vector import *

#////////////////////////////////////////////////////////////////////////////////////////////////

figureList = []
sphere_list = []
cube_list = []

#////////////////////////////////////////////////////////////////////////////////////////////////

def Master_cube(x, y, z, dim, sideL):
    # (x, y, z) will represent the corner of the front-left corner of the cube
    # sidelength represents the length of the MasterCube's side.
    # the dim is how many cubes in the x direction.
    # if dim is 5, there are 125 cubes making mastercube.
        start = [x, y, z]

        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    cube = Cube(start[0] + (i * sideL), start[1] + (j * sideL), start[2] + (k * sideL), sideL)
                    cube.gravity(0)

#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////

class Point (object):
    
#////////////////////////////////////////////////////////////////////////////////////////////////

    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

#////////////////////////////////////////////////////////////////////////////////////////////////

    # create a string representation of a Point (x, y, z)
    def __str__ (self):
        s = "({}, {}, {})".format(str(self.x), str(self.y), str(self.z))
        return s

#////////////////////////////////////////////////////////////////////////////////////////////////

    # get distance to another Point object
    def distance (self, other):
        core_x = (self.x - other.x) ** 2
        core_y = (self.y - other.y) ** 2
        core_z = (self.z - other.z) ** 2
        d = (core_x + core_y + core_z) ** .5
        return d

#////////////////////////////////////////////////////////////////////////////////////////////////

    # test for equality between two points
    def __eq__ (self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
    
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////

'''
The universal class. All figures will inherit the basic fields of this class:
Position, Orientation, Velocity, Angular speed, Axis of rotation, Gravity.
Position can be set from the constructor, but the others are set from their
corresponding methods. Methods used to set attributes return the updated object
(unless the methods are used to RETURN attribute values). Therefore it is
possible to concatenate attribute-changing methods this way:
Figure(10,20,30).velocity(5,3).gravity(1).hide().pause()
The class also includes methods for rudimentary control of the figure:
Showing, Hiding, Pausing, Removal'''
class Figure(object):
    '''
    Constructor.
    (x,y,z) = Position in world space. Defaults to the origin.
    Other parameters are set using the methods found below'''

#////////////////////////////////////////////////////////////////////////////////////////////////

    def __init__(self, x=0, y=0, z=0):
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
        self.omegaX = 0.0
        self.omegaY = 0.0
        self.omegaZ = 0.0
        self.axisX = 0.0
        self.axisY = 0.0
        self.axisZ = 1.0
        self.m = 1.0
        self.g = 0.0
        self.visible = True
        self.paused = False

        figureList.append(self)
        
#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set position of figure. Given no arguments, returns current position (as triplet).
    # To change individual components, assign values to the fields .x .y and .z
    def position(self, x=None, y=None, z=None):
       if x==None:
           return self.x, self.y, self.z
       self.x = float(x)
       self.y = float(y)
       self.z = float(z)
       return self
    
#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set orientation of figure. Given no arguments, returns current orientation (as triplet).
    # To change individual components, assign values to the fields .thX .thY and .thZ
    def orient(self, thX=None, thY=None, thZ=None):
        if thX==None:
            return self.thX, self.thY, self.thZ
        self.thX = float(thX)
        self.thY = float(thY)
        self.thZ = float(thZ)
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set velocity of the figure. Given no arguments, returns the current velocity (as triplet)
    # To change individual components, assign values to the fields .vx .vy and .vz
    def velocity(self, vx=None, vy=None, vz=None):
        if vx==None:
            return self.vx, self.vy, self.vz
        self.vx = float(vx)
        self.vy = float(vy)
        self.vz = float(vz)
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set rotation speed. Given no arguments, returns the current rotation speed.
    def angSpeed(self, omega=None):
       if omega==None:
           return self.omega
       self.omega = float(omega)

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set rotation axis. Given no arguments, returns the current axis (as triplet).
    # To change individual components, assign values to the fields .axisX .axisY and .axisZ
    def axis(self, axisX=None, axisY=None, axisZ=None):
        if axisX==None:
            return self.axisX, self.axisY, self.axisZ
        self.axisX = float(axisX)
        self.axisY = float(axisY)
        self.axisZ = float(axisZ)
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set gravity. Given no arguments, returns the current gravity.
    def gravity(self, g=None):
        if g==None:
            return self.g
        self.g = float(g)
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////
    
    # Set mass. Given no arguments, returns the current mass.
    def mass(self, m=None):
        if m==None:
            return self.m
        self.m = float(m)
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Destructor. Removes the figure from the scene.
    def kill(self):
        if self in cube_list:
            cube_list.remove(self)
        if self in figureList:
            figureList.remove(self)
        if self in sphere_list:
            sphere_list.remove(self)

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Makes the figure visible
    def show(self):
        self.visible = True
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Makes the figure invisible
    def hide(self):
        self.visible = False
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Returns boolean on whether the object is visible or not
    def is_visible(self):
        return self.visible

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Prevents the figure from being updated
    def pause(self):
        self.paused = True
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Allows the figure to be updated
    def resume(self):
        self.paused = False
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Returns boolean on whether the object is paused or not
    def is_paused(self):
        return self.paused

#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////

# The Cube class. Inherits from Figure.
class Cube(Figure):
    
#////////////////////////////////////////////////////////////////////////////////////////////////

    # Constructor. Takes all parameters that Figure does, as well as other parameters
    # specific to the Cube class.
    def __init__(self, x = 0, y = 0, z = 0, sideL = 0):

        self.C = "#FA5103"
        self.L = .85

        # Use Figure's constructor to initialize the universal fields
        Figure.__init__(self, x, y, z)

        if (sideL == None):
            self.sideL = 0
        else:
            self.sideL = sideL
        self.col = ("#C1BBBB")        
        # orig is the center
        self.orig = Point(x+self.sideL/2, y+self.sideL/2, z+self.sideL/2)
        # touch counts how many times the cube has been touched
        #self.touch = 0
        cube_list.append(self)
        
#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set sidelength of cube. Given no arguments, returns the current sidelength.
    # def side(self, S = None):
    #     if (S == None):
    #         return self.S
    #     self.S = S

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set position of figure. Given no arguments, returns current position (as triplet).
    # To change individual components, assign values to the fields .x .y and .z
    def position(self, x=None, y=None, z=None):
        if x==None:
            return self.x+self.sideL/2, self.y+self.sideL/2, self.z+self.sideL/2
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    def col(self, C=None):
       if (C ==None):
           return self.C
       self.C = C
       self.L = .95
       return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # determines if a point is inside the cube
    def is_inside_point (self, p):

        x_in = (p.x >= self.orig.x - .5 * self.sideL) and (p.x <= self.orig.x + .5 * self.sideL)
        y_in = (p.y >= self.orig.y - .5 * self.sideL) and (p.y <= self.orig.y + .5 * self.sideL)
        z_in = (p.z >= self.orig.z - .5 * self.sideL) and (p.z <= self.orig.z + .5 * self.sideL)

        return (x_in and y_in and z_in)

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Given a sphere, returns boolean on whether self is colliding with it
    def collides_sphere(self, other):
        return (self.orig.distance(other.center) < other.R + self.sideL/2)

#////////////////////////////////////////////////////////////////////////////////////////////////
        
    def collides_cube(self, other):
       #return (abs(self.orig.x - other.orig.x) < other.sideL/2 + self.sideL/2 or abs(self.orig.y - other.orig.y) < other.sideL/2 + self.sideL/2 or abs(self.orig.z - other.orig.z) < other.sideL/2 + self.sideL/2)
       return (self.orig.distance(other.orig) < other.sideL/2 + self.sideL/2)

#////////////////////////////////////////////////////////////////////////////////////////////////
   
    def collide(self, other): 
        
        # if (isinstance(other, Ball)):
        #     measure = other.R
        # else:
        #     measure = other.sideL/2                
        
        # Move objects away from each other, so that
        # they are no longer colliding and won't "stick"
        r1 = Vector(self.position())
        r2 = Vector(other.position())
        N = r1 - r2  # Normal vector between object centers
        n = unit(N)  # Unit vector version of N        
        # if(isinstance(other, Ball)):
        #     move = 0.5*(self.sideL/2 + other.R - Norm(N))
        #     r1 += n.times(move)
        #     r2 -= n.times(move)
        #     # Update fields
        #     self.x, self.y, self.z = r1.vect
        #     other.x, other.y, other.z = r2.vect
        #     self.orig = Point(self.x, self.y, self.z)
        #     other.center = Point(other.x, other.y, other.z)        

        # Begin bounce algorithm
        # Setup
        v1 = Vector(self.velocity())
        v2 = Vector(other.velocity())
        m1 = self.mass()
        m2 = other.mass()
        Sum = m1+m2
        Diff = m1-m2
        v_cm = (v1.times(m1) + v2.times(m2)).times(1.0/Sum)
        
        # Translate velocities into center-of-momentum frame
        v1 = v1 - v_cm
        v2 = v2 - v_cm
        
        # Compute parallel and perp components wrt normal N
        v1_para = v1.proj(N)
        v1_perp = v1 - v1_para
        v2_para = v2.proj(N)
        v2_perp = v2 - v2_para
                       
        # angular momentum transfer        
        v_perp = (v1_perp + v2_perp).times(.02)
        if (Norm(v_perp) != 0):
            self.omegaX = v_perp.vect[0]
            self.omegaY = v_perp.vect[1]  
            self.omegaZ = v_perp.vect[2]          
        
        # Momentum transfer only occurs in the para direction.
        # Translate v1_para into the frame where v2_para = 0
        # so we can apply elastic collision formulas.
        v1_para2 = v1_para - v2_para
        
        # Compute new velocites
        w1_para2 = v1_para2.times(Diff/Sum)
        w2_para2 = v1_para2.times(2*m1/Sum)
        
        # Translate back into center-of-momentum frame
        w1_para = w1_para2 + v2_para
        w2_para = w2_para2 + v2_para
        
        # Add in the perp components which are unchanged.
        w1 = w1_para + v1_perp
        w2 = w2_para + v2_perp
        
        # # Calculate bounced versions of v1 and v2
        # w1 = v1_perp - v1_para
        # w2 = v2_perp - v2_para
        
        # Translate final velocities back into scene frame
        w1 = w1 + v_cm
        w2 = w2 + v_cm
        
        # Set velocities to bounce values
        self.vx, self.vy, self.vz = w1.vect
        other.vx, other.vy, other.vz = w2.vect

#////////////////////////////////////////////////////////////////////////////////////////////////
    
    def update(self, dt=None):
        if dt == None:
            dt = toc()*45*speed()
        else:
            # Get elapsed time since last frame was drawn.
            dt *= 45*speed()

        # # Record positions BEFORE update
        # xOld = self.x
        # yOld = self.y
        # zOld = self.z
        # vxOld = self.vx
        # vyOld = self.vy
        # vzOld = self.vz

        # Update position
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt

        # Update vertical (y) velocity due to gravity
        self.vy += self.g * dt

        # Check for collision with boundary
        if self.y < -500 + self.sideL/2:
            # h = yOld + 500 - self.R
            # self.vy = -sgn(self.vy)*sqrt(abs(vyOld**2 + 2*self.g*h)*self.L)
            self.vy = -self.vy * self.L
            self.y = -500 + self.sideL/2
        elif self.y > 500 - self.sideL/2:
            # h = 500 - self.R - yOld
            # self.vy = -sgn(self.vy)*sqrt(abs(vyOld**2 + 2*self.g*h)*self.L)
            self.vy = -self.vy * self.L
            self.y = 500 - self.sideL

        if self.x < -500 + self.sideL:
            self.x = -500 + self.sideL
            self.vx = -self.vx * self.L
        elif self.x > 500 - self.sideL:
            self.x = 500 - self.sideL
            self.vx = -self.vx * self.L

        if self.z < -500 + self.sideL:
            self.z = -500 + self.sideL
            self.vz = -self.vz * self.L
        elif self.z > 500 - self.sideL:
            self.z = 500 - self.sideL
            self.vz = -self.vz * self.L

        #increment rotation by rotational speed; can only have value between 0 and 2PI
        self.thX = (self.thX + self.omegaX*dt)%(2*PI)
        self.thY = (self.thY + self.omegaY*dt)%(2*PI)
        self.thZ = (self.thZ + self.omegaZ*dt)%(2*PI)

        self.orig = Point(self.x+self.sideL/2, self.y+self.sideL/2, self.z+self.sideL/2)

        # # Increment vertical velocity
        #self.vy += self.g * dt

#////////////////////////////////////////////////////////////////////////////////////////////////

    def display(self):
        stroke(0)
        #noStroke()
        strokeWeight(2)
        pushMatrix()
        translate(self.x, self.y, self.z)
        rotateX(self.thX)
        rotateY(self.thY)
        rotateZ(self.thZ)
        fill(self.C)
        box(self.sideL, self.sideL, self.sideL)
        popMatrix()

#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////

# Ball class
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

#////////////////////////////////////////////////////////////////////////////////////////////////
    
    # Set radius of ball. Given no arguments, returns the current radius.
    def radius(self, R=None):
        if R==None:
            return self.R
        self.R = R
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set color of ball (as string). Given no arguments, returns the current color (as string).
    def col(self, C=None):
        if C==None:
            return self.C
        self.C = C
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Set bounce loss factor. Given no arguments, returns the current loss factor.
    def loss(self, L=None):
        if L==None:
            return self.L
        self.L = L
        return self

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Return boolean on whether self overlaps other
    def collides(self, other):
        return dist(self.x, self.y, self.z, other.x, other.y, other.z) <= self.R + other.R

#////////////////////////////////////////////////////////////////////////////////////////////////
    
    # Return list of all spheres colliding with self
    def collisions(self):
        hitList = []
        for sph in sphere_list:
            if self != sph and self.collides(sph):
                hitList.append(sph)
        return hitList

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Updates the fields of self AND other using bounce physics
    def bounce(self, other):
        # Move balls away from each other, so that
        # they are no longer colliding and won't "stick"
        r1 = Vector(self.position())
        r2 = Vector(other.position())
        N = r1 - r2  # Normal vector between ball centers
        n = unit(N)  # Unit vector version of N
        # Amount to move balls so they no longer collide
        move = 0.5*(self.R + other.R - Norm(N))
        r1 += n.times(move)
        r2 -= n.times(move)
        # Update fields
        self.x, self.y, self.z = r1.vect
        other.x, other.y, other.z = r2.vect
        self.center = Point(self.x, self.y, self.z)
        other.center = Point(other.x, other.y, other.z)

        # Begin bounce algorithm
        # Setup
        v1 = Vector(self.velocity())
        v2 = Vector(other.velocity())
        m1 = self.mass()
        m2 = other.mass()
        Sum = m1+m2
        Diff = m1-m2
        v_cm = (v1.times(m1) + v2.times(m2)).times(1.0/Sum)
        
        # Translate velocities into center-of-momentum frame
        v1 = v1 - v_cm
        v2 = v2 - v_cm
        
        # Compute parallel and perp components wrt normal N
        v1_para = v1.proj(N)
        v1_perp = v1 - v1_para
        v2_para = v2.proj(N)
        v2_perp = v2 - v2_para
        
        # Momentum transfer only occurs in the para direction.
        # Translate v1_para into the frame where v2_para = 0
        # so we can apply elastic collision formulas.
        v1_para2 = v1_para - v2_para
        
        # Compute new velocites
        w1_para2 = v1_para2.times(Diff/Sum)
        w2_para2 = v1_para2.times(2*m1/Sum)
        
        # Translate back into center-of-momentum frame
        w1_para = w1_para2 + v2_para
        w2_para = w2_para2 + v2_para
        
        # Add in the perp components which are unchanged.
        w1 = w1_para + v1_perp
        w2 = w2_para + v2_perp
        
        # # Calculate bounced versions of v1 and v2
        # w1 = v1_perp - v1_para
        # w2 = v2_perp - v2_para
        
        # Translate final velocities back into scene frame
        w1 = w1 + v_cm
        w2 = w2 + v_cm
        
        # Set velocities to bounce values
        self.vx, self.vy, self.vz = w1.vect
        other.vx, other.vy, other.vz = w2.vect

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Updates the fields of the ball depending on its current state in the scene
    def update(self, dt=None):
        if dt == None:
            dt = toc()*45*speed()
        else:
            # Get elapsed time since last frame was drawn.
            dt *= 45*speed()

        # # Record positions BEFORE update
        # xOld = self.x
        # yOld = self.y
        # zOld = self.z
        # vxOld = self.vx
        # vyOld = self.vy
        # vzOld = self.vz

        # Update position
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt

        # Update vertical (y) velocity due to gravity
        self.vy += self.g * dt

        # Check for collision with boundary
        if self.y < -500 + self.R:
            # h = yOld + 500 - self.R
            # self.vy = -sgn(self.vy)*sqrt(abs(vyOld**2 + 2*self.g*h)*self.L)
            self.vy = -self.vy * self.L
            self.y = -500 + self.R
        elif self.y > 500 - self.R:
            # h = 500 - self.R - yOld
            # self.vy = -sgn(self.vy)*sqrt(abs(vyOld**2 + 2*self.g*h)*self.L)
            self.vy = -self.vy * self.L
            self.y = 500 - self.R

        if self.x < -500 + self.R:
            self.x = -500 + self.R
            self.vx = -self.vx * self.L
        elif self.x > 500 - self.R:
            self.x = 500 - self.R
            self.vx = -self.vx * self.L

        if self.z < -500 + self.R:
            self.z = -500 + self.R
            self.vz = -self.vz * self.L
        elif self.z > 500 - self.R:
            self.z = 500 - self.R
            self.vz = -self.vz * self.L

        self.center = Point(self.x, self.y, self.z)

#////////////////////////////////////////////////////////////////////////////////////////////////

    # Displays the ball on the screen
    def display(self):
        noStroke()
        pushMatrix()
        translate(self.x, self.y, self.z)
        fill(self.C)
        #ellipse(self.x, self.y, self.R*2, self.R*2)
        sphere(self.R)
        popMatrix()

#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////

# Checks for collisions between all spheres.
# If any are detected, it will call the .bounce() method
# to update the fields accordingly.
def checkCollisions():
    for i in range(len(sphere_list)):
        for j in range(i+1, len(sphere_list)):
            ball1 = sphere_list[i]
            ball2 = sphere_list[j]
            if ball1.collides(ball2):
                ball1.bounce(ball2)
                
    for i in range(len(cube_list)):
        for j in range(len(sphere_list)):
            cube1 = cube_list[i]
            ball1 = sphere_list[j]
            if cube1.collides_sphere(ball1):
                if cube1.gravity() == 0:
                    cube1.gravity(1)
                cube1.collide(ball1)
                
    for i in range(len(cube_list)):
        for j in range(len(cube_list)):
            if (j == i):
                continue
            cube1 = cube_list[i]
            cube2 = cube_list[j]
            if cube1.collides_cube(cube2):
                if cube1.gravity() == 0:
                    cube1.gravity(1)
                cube1.collide(cube2)
        
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////

# Sets the speed of the simulation.
# speed(1) is normal, speed(0.5) is half speed, etc.
# Call speed() without arguments to return current speed.
global sp
sp = 1
def speed(s=None):
    global sp
    if s==None:
        return sp
    sp = s

# HELPER FUNCTIONS

# Signum function. Returns x/abs(x) unless x = 0, in which case: 0 returned
def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0
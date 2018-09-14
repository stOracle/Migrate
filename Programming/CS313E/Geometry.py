#  File: Geometry.py

#  Description: A geometry simulator

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 2/19/2016

#  Date Last Modified: 2/21/2016

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

import math
import random

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

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

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

class Sphere (object):

	# constructor with default values
	def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
		self.center = Point(x, y, z)
		self.radius = radius

	# string representation of a Sphere: Center: (x, y, z), Radius: value
	def __str__ (self):
		s = "Center: {}, Radius: {}".format(str(self.center), str(self.radius))
		return s

	# compute surface area of Sphere
	def area (self):
		S = 4 * math.pi * (self.radius ** 2)
		return S

	# compute volume of a Sphere
	def volume (self):
		V = (4 / 3) * math.pi * (self.radius ** 3)
		return V

	# determines if a Point is strictly inside the Sphere
	def is_inside_point (self, p):
		diff = self.center.distance(p)
		return (diff < self.radius)

	# determine if another Sphere is strictly inside this Sphere
	def is_inside_sphere (self, other):
		diff = self.center.distance(other.center)
		return (self.radius > (diff + other.radius))

	# determine if a Cube is strictly inside this Sphere
	def is_inside_cube (self, a_cube):

		diff = self.center.distance(a_cube.center)
		index = [-.5, .5]

		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [a_cube.center.x + a_cube.side * index[i],
						a_cube.center.y + a_cube.side * index[j],
							a_cube.center.z + a_cube.side * index[k]]
					vert = Point(point[0], point[1], point[2])

					if (self.radius <= diff + vert.distance(a_cube.center)):
						return False
		return True

	# determine if a Cylinder is strictly inside this Sphere
	def is_inside_cylinder (self, a_cyl):

		diff = self.center.distance(a_cyl.center)
		index = [-1, 1]

		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [a_cyl.center.x + a_cyl.radius * index[i],
						a_cyl.center.y + a_cyl.radius * index[j],
							a_cyl.center.z + a_cyl.height * (.5 * index[k])]
					vert = Point(point[0], point[1], point[2])

					if (self.radius <= diff + vert.distance(a_cyl.center)):
						return False
		return True


	# determine if another Sphere intersects this Sphere
	# there is a non-zero volume of intersection
	def does_intersect_sphere (self, other):
		diff = self.center.distance(other.center)
		if (diff >= self.radius + other.radius):
			return False
		else:
			return True

	# determine if a Cube intersects this Sphere
	# there is a non-zero volume of intersection
	def does_intersect_cube (self, a_cube):
		diff = self.center.distance(a_cube.center)
		index = [-.5, 0, .5]

		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [a_cube.center.x + a_cube.side * index[i],
						a_cube.center.y + a_cube.side * index[j],
							a_cube.center.z + a_cube.side * index[k]]
					vert = Point(point[0], point[1], point[2])

					if (self.is_inside_point(vert)):
						return True
		return False


	# return the largest Cube object that is circumscribed
	# by this Sphere
	def circumscribe_cube (self):
		cube_x = self.center.x
		cube_y = self.center.y
		cube_z = self.center.z
		side = round(2 * self.radius / (3 ** .5), 3)
		cube = Cube (cube_x, cube_y, cube_z, side)

		return cube

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

class Cube (object):

	# Cube is defined by its center (which is a Point object)
	# and side. The faces of the Cube are parallel to x-y, y-z,
	# and x-z planes.
	def __init__ (self, x = 0, y = 0, z = 0, side = 1):
		self.center = Point(x, y, z)
		self.side = side

	# string representation of a Cube: Center: (x, y, z), Side: value
	def __str__ (self):
		s = "Center: {}, Side: {}".format(str(self.center), str(self.side))
		return s

	# compute surface area of Cube
	def area (self):
		A = 6 * (self.side ** 2)
		return A

	# compute volume of a Cube
	def volume (self):
		V = self.side ** 3
		return V

	# determines if a Point is strictly inside this Cube
	def is_inside_point (self, p):
		diff = self.center.distance(p)
		x_in = (.5 * self.side  > abs(self.center.x - p.x))
		y_in = (.5 * self.side  > abs(self.center.y - p.y))
		z_in = (.5 * self.side  > abs(self.center.z - p.z))
		return (x_in and y_in and z_in)


	# determine if a Sphere is strictly inside this Cube
	def is_inside_sphere (self, a_sphere):
		
		index = [-1, 1]
		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [a_sphere.center.x + a_sphere.radius * index[i],
						a_sphere.center.y + a_sphere.radius * index[j],
							a_sphere.center.z + a_sphere.radius * index[k]]
					vert = Point(point[0], point[1], point[2])

					if not (self.is_inside_point(vert)):
						return False
		return True

	# determine if another Cube is strictly inside this Cube
	def is_inside_cube (self, other):

		index = [-.5, .5]
		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [other.center.x + other.side * index[i],
						other.center.y + other.side * index[j],
							other.center.z + other.side * index[k]]
					vert = Point(point[0], point[1], point[2])

					if not (self.is_inside_point(vert)):
						return False
		return True

	# determine if a Cylinder is strictly inside this Cube
	def is_inside_cylinder (self, a_cyl):

		index = [-1, 1]

		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [a_cyl.center.x + a_cyl.radius * index[i],
						a_cyl.center.y + a_cyl.radius * index[j],
							a_cyl.center.z + a_cyl.height * (.5 * index[k])]
					vert = Point(point[0], point[1], point[2])

					if not (self.is_inside_point(vert)):
						return False
		return True

	# determine if another Cube intersects this Cube
	# there is a non-zero volume of intersection
	def does_intersect_cube (self, other):

		index = [-.5, .5]
		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [other.center.x + other.side * index[i],
						other.center.y + other.side * index[j],
							other.center.z + other.side * index[k]]
					vert = Point(point[0], point[1], point[2])

					if (self.is_inside_point(vert)):
						return True
		return False

	# determine the volume of intersection if this Cube 
	# intersects with another Cube
	def intersection_volume (self, other):
		
		if not self.does_intersect_cube:
			return 0
		elif (self.is_inside_cube(other)):
			return other.volume
		else:
			return None
			#x_len = abs(self.)

	# return the largest Sphere object that is inscribed
	# by this Cube
	def inscribe_sphere (self):
		sphere_x = self.center.x
		sphere_y = self.center.y
		sphere_z = self.center.z
		radius = .5 * self.side
		sphere = Sphere(sphere_x, sphere_y, sphere_z, radius)
		return sphere

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

class Cylinder (object):

	# Cylinder is defined by its center (which is a Point object),
	# radius and height. The main axis of the Cylinder is along the
	# z-axis and height is measured along this axis
	def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
		self.center = Point(x, y, z)
		self.radius = radius
		self.height = height

	# string representation of a Cylinder: Center: (x, y, z), Radius: value, Height: value
	def __str__ (self):
		s = "Center: {}, Radius, {}, Height: {}".format(
			str(self.center), str(self.radius), str(self.height))
		return s

	# compute surface area of Cylinder
	def area (self):
		S = 2 * math.pi * self.radius * (self.height + self.radius)
		return S

	# compute volume of a Cylinder
	def volume (self):
		V = math.pi * self.height * self.radius ** 2
		return V

	# determine if a Point is strictly inside this Cylinder
	def is_inside_point (self, p):
		p_x = p.x
		p_y = p.y
		p_z = p.z

		x_in = ((p_x > self.center.x - self.radius) and 
			(p_x < self.center.x + self.radius))
		y_in = ((p_y > self.center.y - self.radius) and 
			(p_y < self.center.y + self.radius))
		z_in = ((p_z > self.center.z - (.5 * self.height)) and 
			(p_z < self.center.z + (.5 * self.height)))

		return (x_in and y_in and z_in)

	# determine if a Sphere is strictly inside this Cylinder
	def is_inside_sphere (self, a_sphere):

		index = [-1, 1]
		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [a_sphere.center.x + a_sphere.radius * index[i],
						a_sphere.center.y + a_sphere.radius * index[j],
							a_sphere.center.z + a_sphere.radius * index[k]]
					vert = Point(point[0], point[1], point[2])

					if not (self.is_inside_point(vert)):
						return False
		return True

	# determine if a Cube is strictly inside this Cylinder
	def is_inside_cube (self, a_cube):
		
		index = [-.5, .5]
		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [a_cube.center.x + a_cube.side * index[i],
						a_cube.center.y + a_cube.side * index[j],
							a_cube.center.z + a_cube.side * index[k]]
					vert = Point(point[0], point[1], point[2])

					if not (self.is_inside_point(vert)):
						return False
		return True

	# determine if another Cylinder is strictly inside this Cylinder
	def is_inside_cylinder (self, other):
		
		index = [-1, 1]

		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [other.center.x + other.radius * index[i],
						other.center.y + other.radius * index[j],
							other.center.z + other.height * (.5 * index[k])]
					vert = Point(point[0], point[1], point[2])

					if not (self.is_inside_point(vert)):
						return False
		return True

	# determine if another Cylinder intersects this Cylinder
	# there is a non-zero volume of intersection
	def does_intersect_cylinder (self, other):
		
		index = [-1, 1]
		for i in range (len(index)):
			for j in range (len(index)):
				for k in range (len(index)):

					point = [other.center.x + other.radius * index[i],
						other.center.y + other.radius * index[j],
							other.center.z + other.height * (.5 * index[k])]
					vert = Point(point[0], point[1], point[2])

					if (self.is_inside_point(vert)):
						return True
		return False

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

def main():

	# open file "geometry.txt" for reading
	in_file = open(".\geometry.txt", "r")
	data = []

	for line in in_file:
		spot = line.find("#")
		line = line[:spot]
		line = line.split()
		data.append(line)

	in_file.close()

	for i in range(len(data)):

		for j in range(len(data[i])):
			data[i][j] = float(data[i][j])

	# read the coordinates of the first Point p
	

	# create a Point object and print its coordinates
	object_list = []

	p = Point(data[0][0], data[0][1], data[0][2])
	object_list.append(p)

	q = Point(data[1][0], data[1][1], data[1][2])
	object_list.append(q)

	sphereA = Sphere(data[2][0], data[2][1], data[2][2], data[2][3])
	object_list.append(sphereA)

	sphereB = Sphere(data[3][0], data[3][1], data[3][2], data[3][3])
	object_list.append(sphereB)

	cubeA = Cube(data[4][0], data[4][1], data[4][2], data[4][3])
	object_list.append(cubeA)

	cubeB = Cube(data[5][0], data[5][1], data[5][2], data[5][3])
	object_list.append(cubeB)

	cylA = Cylinder(data[6][0], data[6][1], data[6][2], data[6][3], data[6][4])
	object_list.append(cylA)

	cylB = Cylinder(data[7][0], data[7][1], data[7][2], data[7][3], data[7][4])
	object_list.append(cylB)
	title_list = ["Point p", "Point q", "sphereA", "sphereB", 
		"cubeA", "cubeB", "cylA", "cylB"]

	print()
	for i in range (len(title_list)):
		print("{:^10}: {}".format(title_list[i], str(object_list[i])))

	print()
	print ("Distance between p and q: {}".format(str(p.distance(q))))

	print()
	print("Area of sphereA: {}".format(str(sphereA.area())))
	print("Volume of sphereA: {}".format(str(sphereA.volume())))

	# print if Point p is inside sphereA
	if (sphereA.is_inside_point(p)):
		print("Point p is inside sphereA")
	else:
		print("Point p is not inside sphereA")

	# print if sphereB is inside sphereA
	if (sphereA.is_inside_sphere(sphereB)):
		print("sphereB is inside sphereA")
	else:
		print("sphereB is not inside sphereA")

	# print if cubeA is inside sphereA
	if (sphereA.is_inside_cube(cubeA)):
		print("cubeA is inside sphereA")
	else:
		print("cubeA is not inside sphereA")

	# print if cylA is inside sphereA
	if (sphereA.is_inside_cylinder(cylA)):
		print("cylA is inside sphereA")
	else:
		print("cylA is not inside sphereA")

	# print if sphereA intersects with sphereB
	if (sphereA.does_intersect_sphere(sphereB)):
		print("sphereA does intersect sphereB")
	else:
		print("sphereA does not intersect sphereB")

	# print if cubeB intersects with sphereB
	if (sphereB.does_intersect_cube(cubeB)):
		print("cubeB does intersect sphereB")
	else:
		print("cubeB does not intersect sphereB")

	# print the largest Cube that is circumscribed by sphereA
	print("Largest Cube circumscribed by sphereA: {}".format(str(sphereA.circumscribe_cube())))
	print()

	# print area of cubeA
	print("Area of cubeA: {}".format(cubeA.area()))

	# print volume of cubeA
	print("Volume of cubeA: {}".format(cubeA.volume()))

	# print if Point p is inside cubeA
	if (cubeA.is_inside_point(p)):
		print("Point p is inside cubeA")
	else:
		print("Point p is not inside cubeA")

	# print if sphereA is inside cubeA
	if (cubeA.is_inside_sphere(sphereA)):
		print("sphereA is inside cubeA")
	else:
		print("sphereA is not inside cubeA")

	# print if cubeB is inside cubeA
	if (cubeA.is_inside_cube(cubeB)):
		print("cubeB is inside cubeA")
	else:
		print("cubeB is not inside cubeA")

	# print if cylA is inside cubeA
	if (cubeA.is_inside_cylinder(cylA)):
		print("cylA is inside cubeA")
	else:
		print("cylA is not inside cubeA")

	# print if cubeA intersects with cubeB
	if (cubeA.does_intersect_cube(cubeB)):
		print("cubeA does intersect cubeB")
	else:
		print("cubeA does not intersect cubeB")

	# print the intersection volume of cubeA and cubeB
	print("Intersection volume of cubeA and cubeB: {}".format(cubeA.intersection_volume(cubeB)))

	# print the largest Sphere object inscribed by cubeA
	print("Largest Sphere inscribed by cubeA: {}".format(str(cubeA.inscribe_sphere())))

	# print area of cylA
	print()
	print("Area of cylA: {}".format(cylA.area()))

	# print volume of cylA
	print("Volume of cylA: {}".format(cylA.volume()))

	# print if Point p is inside cylA
	if (cylA.is_inside_point(p)):
		print("Point p is inside cylA")
	else:
		print("Point p is not inside cylA")

	# print if sphereA is inside cylA
	if (cylA.is_inside_sphere(sphereA)):
		print("sphereA is inside cylA")
	else:
		print("sphereA is not inside cylA")

	# print if cubeA is inside cylA
	if (cylA.is_inside_cube(cubeA)):
		print("cubeA is inside cylA")
	else:
		print("cubeA is not inside cylA")

	# print if cylB is inside cylA
	if (cylA.is_inside_cylinder(cylB)):
		print("cylB is inside cylA")
	else:
		print("cylB is not inside cylA")

	# print if cylB intersects with cylA
	if (cylA.does_intersect_cylinder(cylB)):
		print("cylA does intersect cylB")
	else:
		print("cylA does not intersect cylB")

main()
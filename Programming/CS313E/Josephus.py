#  File: Josephus.py

#  Description: A fun and quirky russian-roulette simulator!

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 4/9/16

#  Date Last Modified: 4/9/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

global dead
dead = []

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Link (object):

# /////////////////////////////////////////////////////////////////////////////////

	def __init__ (self, data, next = None):
		self.data = data
		self.next = None

# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):
		return str(self.data)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////p
# /////////////////////////////////////////////////////////////////////////////////

class CircularList(object):

# /////////////////////////////////////////////////////////////////////////////////

	def __init__ (self):

		self.first = None
		self.last = None
		self.links = 0

# /////////////////////////////////////////////////////////////////////////////////

	# insert an element into the list
	def insert (self, data):

		newLink = Link(data)
		first = self.first
		last = self.last

		# if list is empty
		if (first == None):
			self.first = newLink

		# if only one item in list
		elif (last == None):
			first.next = newLink
			self.last = newLink
			newLink.next = self.first

		else:
			last.next = newLink
			self.last = newLink
			newLink.next = first

		self.links += 1

# /////////////////////////////////////////////////////////////////////////////////

	# find the link with the given key
	# I modified find to reorient the last and first values - 
	#   now, self.first points to the value you wanted to find
	def find(self, data):

		current = self.first
		if (current == None):
			return None

		count = 1
		while (count <= self.links):
			if (current.next.data == data):
				self.last = current
				self.first = current.next
				return current.next.data

			current = current.next

			count += 1

# /////////////////////////////////////////////////////////////////////////////////

	# delete a link with a given key
	def delete (self, data):

		current = self.first
		previous = self.last
		start = self.first.data

		if (current == None):
			return None

		count = 1

		while (count <= self.links):

			if (current.data == data):
				if (current == self.first):
					self.last.next = current.next
					self.first = current.next
					self.links -= 1
					dead.append(current.data)
					break
				elif (current == self.last):
					self.last = previous
					previous.next = self.first
					self.links -= 1
					dead.append(current.data)
					break
				else:
					previous.next = current.next
					self.links -= 1
					dead.append(current.data)
					break

			elif (current.data != data):
				previous = current
				current = current.next

			count += 1		

# /////////////////////////////////////////////////////////////////////////////////

	# delete the nth link starting from the Link start
	# return the next link from the deleted link
	def deleteAfter(self, start, n):

		self.find(start)
		current = self.first	
		count = 1

		while (count < n):
			current = current.next
			count += 1

		self.delete(current.data)
		follow = current.next.data
		return follow

# /////////////////////////////////////////////////////////////////////////////////

	# return a string representation of a Circular List
	def __str__ (self):
		
		current = self.first
		st = ""
		count = 0

		if (current == None):
			return None

		while (current.next != self.first):

			if (count % 10 == 9):
				st += "{}\n".format(str(current.data))

			else:
				st += "{:<4}".format(current.data)

			current = current.next
			count += 1

		if (count % 10 == 9):
				st += "{}\n".format(str(current.data))

		else:
				st += "{:<4}".format(current.data)

		return st

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():

	# open file and pull from file
	in_file = open("./josephus.txt", "r")
	num_soldiers = int(in_file.readline())
	start_pos = int(in_file.readline())
	jump = int(in_file.readline())

	in_file.close()

	# create circular list and populate
	Sol_circle = CircularList()
	for i in range (num_soldiers):
		Sol_circle.insert(i + 1)

	# loop to kill people until there is one left
	spot = start_pos
	while (Sol_circle.links > 1):
		Sol_circle.find(spot)
		spot = Sol_circle.deleteAfter(Sol_circle.first, jump)
	
	# print loop for all dead people
	st = ""
	for i in dead:
		st += str(i) + " "
	print (st)

	# The list should only have one person at this point
	print (Sol_circle)

	




main()
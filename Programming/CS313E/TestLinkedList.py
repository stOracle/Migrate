#  File: TestLinkedList.py

#  Description: A program to utilize the data structure linked list in various situations

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 4/3/2016

#  Date Last Modified: 4/4/2016

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Link(object):
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class LinkedList(object):
	def __init__(self):
		self.first = None

# /////////////////////////////////////////////////////////////////////////////////

	# get number of links
	def getNumLinks(self):
		count = 1
		current = self.first

		if (current == None):
			return 0

		while (current.next != None):
			count += 1
			current = current.next

		return count

# /////////////////////////////////////////////////////////////////////////////////

	# add data at the front of a list
	def addFirst(self, data):

		newLink = Link(data)
		newLink.next = self.first
		self.first = newLink

# /////////////////////////////////////////////////////////////////////////////////

	# add data at the end of a list
	def addLast(self, data):

		newLink = Link(data)
		current = self.first

		if (current == None):
			self.first = newLink
			return

		while (current.next != None):
			current = current.next

		current.next = newLink

# /////////////////////////////////////////////////////////////////////////////////

	# add data in an ordered list in ascending order
	def addInOrder(self, data):

		newLink = Link(data)
		previous = self.first
		current = self.first

		if (current == None):
			newLink.next = None
			self.first = newLink

		while (newLink.data > current.data):
			previous = current
			if (current.next == None):
				break
			else:
				current = current.next

		if (current == self.first):
			self.first = newLink
			newLink.next = current
		elif (current.next == None):
			previous.next = newLink
			newLink.next = None
		else:
			previous.next = newLink
			newLink.next = current

# /////////////////////////////////////////////////////////////////////////////////

	# search in an unordered list, return None if not found
	def findUnordered(self, data):

		current = self.first

		if (current == None):
			return None

		while (current.data != data):
			if (current.next == None):
				return None
			else:
				current = current.next

		return current
		

# /////////////////////////////////////////////////////////////////////////////////

	# search in an ordered list, return None if not found
	def findOrdered(self, data):

		current = self.first

		if (current == None):
			return None

		while (current.data < data):
			if (current.next == None):
				return None
			else:
				current = current.next
		return current

# /////////////////////////////////////////////////////////////////////////////////

	# delete and return link from an unordered list or None if not found
	def delete(self, data):

		current = self.first
		previous = self.first

		if (current == None):
			return None

		while (current.data != data):
			if (current.next == None):
				return None

			else:
				previous = current
				current = current.next

		if (current == self.first):
			self.first = self.first.next

		else:
			previous.next = current.next
		
		return current

# /////////////////////////////////////////////////////////////////////////////////

	# string representation of data 10 items to a line, 2 spaces between data
	def __str__(self):
		length = self.getNumLinks()
		current = self.first
		count = 0

		if (current == None):
			return "List is Empty."

		st = ""

		while (current != None):

			if (count % 10 == 9):
				st += "{}\n".format(str(current.data))

			else:
				st += "{:<4}".format(current.data)

			current = current.next
			count += 1

		return st

# /////////////////////////////////////////////////////////////////////////////////

	# copy the contents of a list and return new list
	def copyList(self):

		new_list = LinkedList()
		current = self.first
		if (current == None):
			return None

		while (current != None):
			data = current.data
			new_list.addLast(data)
			current = current.next

		return new_list

# /////////////////////////////////////////////////////////////////////////////////

	# reverse the contents of a list and return new list
	def reverseList(self):
		current = self.first
		new = LinkedList()
		if (current == None):
			return None

		while (current != None):
			data = current.data
			new.addFirst(data)
			current = current.next

		return new

# /////////////////////////////////////////////////////////////////////////////////

	# sort the contents of a list in ascending order and return new list
	def sortList(self):

		current = self.first
		if (current == None):
			return None

		new = LinkedList()
		new.addFirst(current.data)
		current = current.next
		while (current != None):
			new.addInOrder(current.data)
			current = current.next

		return new

# /////////////////////////////////////////////////////////////////////////////////

	# return True if a list is sorted in ascending order or False otherwise
	def isSorted(self):

		isSorted = True
		current = self.first
		if (current == None):
			return None

		while (current.next != None):
			isSorted = isSorted and (current.data <= current.next.data)
			current = current.next
		return isSorted

# /////////////////////////////////////////////////////////////////////////////////

	# return True if a list is empty or False otherwise
	def isEmpty(self):

		return (self.first == None)
			
# /////////////////////////////////////////////////////////////////////////////////

	# Merge two sorted lists and return new list in ascending order
	def mergeList(self, b):

		newList = LinkedList()
		s_current = self.first
		b_current = b.first

		if (s_current == None) and (b_current == None):
			return None
		elif (s_current == None):
			return b
		elif (b_current == None):
			return self

		while (s_current != None) and (b_current != None):
			if (s_current == None):
				return 

		pass

# /////////////////////////////////////////////////////////////////////////////////

	# test if two lists are equal, item by item and return True if so
	def isEqual(self, b):

		if (self.getNumLinks() != b.getNumLinks()):
			return False
		numLinks = self.getNumLinks()
		s_current = self.first
		b_current = b.first
		for i in range (numLinks):
			if (s_current.data != b_current.data):
				return False
			elif (s_current.next == None):
				return True
			else:
				s_current = s_current.next
				b_current = s_current.next

# /////////////////////////////////////////////////////////////////////////////////

	# return a new list, keeping only the first occurence of an element 
	# and removing all duplicates. Do not change the order of the elements.
	def removeDuplicates(self):
		previous = self.first
		current = self.first
		if (current == None):
			return None

		while (current.next != None):
			if (current.data != current.next.data):
				previous = current
				current = current.next
			else:
				c

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():

	data_ordered = [2, 3, 4, 5, 6, 7, 7, 8, 10, 11, 12, 13, 15, 20, 21, 23]
	
	# test methods addFirst() and __str__() by adding more than
	# 10 items to a list and printing it
	data_unordered = [7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 4, 8, 9, 6, 4] 
	lists = []

	list1 = LinkedList()
	lists.append(list1)

	for el in data_ordered:
		list1.addFirst(el)

	print ("\n-----ADDFIRST TEST-------------\n")
	print ("Data used for list: \n", data_ordered)
	print (list1)

	# test method addLast()
	list2 = LinkedList()
	lists.append(list2)

	for el in data_unordered:
		list2.addLast(el)
	print ("\n-----ADDLAST TEST-----------\n")
	print ("Data used for list: \n", data_unordered)
	print (list2)

	# test method addInOrder()
	print ("\n-----ADDINORDER TEST-----------\n")

	list3 = list2.copyList()
	lists.append(list3)


	list3.addInOrder(9)
	list3.addInOrder(1)
	list3.addInOrder(24)

	print (list3)

	# test method getNumLinks()
	print ("-----GETNUMLINKS TEST-----------\n")

	for i in range(len(lists)):
		print ("List {}: {} links".format(i + 1, lists[i].getNumLinks()))


	# test method findUnordered()
	# consider two cases - item is there, item is not there
	print ("-----FINDUNORDERED TEST-----------\n")
	print("Searching for 7 and 1 in list2:")
	print("list2 = ", list2)

	list2.findUnordered(7)
	list2.findUnordered(1)

	print("list3 is sorted:", list3.isSorted())

	# test method findOrdered()
	# consider two cases - item is there, item is not there
	list1.findUnordered(7)
	list1.findUnordered(1)

	# test method delete()
	# consider two cases - item is there, item is not there


	# test method copyList()

	# test method reverseList()

	# test method reverseList()

	# test method sortList()

	# test method isSorted()
	# consider two cases - list is/is not sorted

	# test method isEmpty()

	# test method mergeList()

	# test method isEqual()
	# consider two cases - lists are/aren't equal

	# test removeDuplicates()




main()
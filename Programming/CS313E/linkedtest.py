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
				st += "{:<3}".format(current.data)

			current = current.next
			count += 1
		return st

	def copyList(self):

		new_list = LinkedList()
		current = self.first
		if (current == None):
			return None

		while (current.next != None):
			data = current.data
			new_list.addLast(data)
			current = current.next

		data = current.data
		new_list.addLast(data)

		return new_list

def main():

	data = [2, 3, 4, 5, 6, 8, 10]
	List = LinkedList()
	for el in data:
		List.addLast(el)

	print (List)

	list2 = List.copyList()
	print (list2)


main()
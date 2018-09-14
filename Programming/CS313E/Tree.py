#  File: Tree.py

#  Description: The basic codework for the binary tree database class

#  Date Created: 4/20/16

#  Date Last Modified: 4/20/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Node (object):

# /////////////////////////////////////////////////////////////////////////////////

	def __init__ (self, data):

		self.data = data
		self.lChild = None
		self.Rchild = None

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Tree (object):

# /////////////////////////////////////////////////////////////////////////////////

	def __init__ (self):
		self.root = None

# /////////////////////////////////////////////////////////////////////////////////

	# insert a node into the tree
	def insert (self, data):

		# create the node
		newNode = Node (data)

		# checks if this will be the first node
		if (self.root == None):
			self.root = newNode

		else:
			# set trackers
			current = self.root
			parent = self.root

			# moves down the according path until you have reached a leaf
			while (current != None):
				parent = current
				if (val < current.data):
					current = current.lChild
				else:
					current = current.Rchild

			# once on the according leaf, sets as one of the children
			if (val < parent.data):
				parent.lChild = newNode
			else:
				parent.rChild = newNode

# /////////////////////////////////////////////////////////////////////////////////

	def search (self, key):

		current = self.root

		while ((current != None) and (current.data != key)):
			if (key < current.data):
				current = current.lChild
			else:
				current = current.rChild

		return current

# /////////////////////////////////////////////////////////////////////////////////

	# in order traversal - left, center, right
	# 	uses recursion to divvy the tree into subtrees until you have 
	# 	you have reached the bottom leafs
	def inOrder (self, aNode):

		if (aNode != None):
			inOrder (aNode.lChild)
			print (aNode.data)
			inOrder (aNode.rChild)

# /////////////////////////////////////////////////////////////////////////////////

	# pre order traversal - center, left, right
	def preOrder (self, aNode):

		if (aNode != None):
			print (aNode.data)
			preOrder (aNode.lChild)
			preOrder (aNode.rChild)

# /////////////////////////////////////////////////////////////////////////////////

	# post order traversal - left, right, center
	def postOrder (self, aNode):

		if (aNode != None):
			postOrder (aNode.lChild)
			postOrder (anode.rChild)
			print (aNode.data)

# /////////////////////////////////////////////////////////////////////////////////

	# find the node with the smallest value
	def minimum (self):

		current = self.root
		parent = current

		while (current != None):
			parent = current
			current = current.lChild

		return parent

# /////////////////////////////////////////////////////////////////////////////////

	# find the node with the largest value
	def maximum (self):

		current = self.root
		parent = current

		while (current != None):
			parent = current
			current = current.rChild

		return current

# /////////////////////////////////////////////////////////////////////////////////

	# delete a node with the given key
	def delete (self, key):

		deleteNode = self.root
		parent = self.root
		isLeft = False

		# if empty tree
		if (deleteNode == None):
			return False

		# Find the delete node
		while ((deleteNode != None) and (deleteNode.data != key)):
			parent = deleteNode
			if (key < deleteNode.data):
				deleteNode = deleteNode.lChild
				isLeft = True

			else:
				deleteNode = deleteNode.rChild
				isLeft = False

		# if node not found
		if (deleteNode == None):
			return False

		# delete node is a leaf node
		if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
			if (deleteNode == self.root):
				self.root = None
			elif (isLeft):
				parent.lChild = None
			else:
				paretn.rChild = None

		# delete node is a node with only left child
		elif (deleteNode.rChild == None):
			if (deleteNode == self.root):
				self.root = deleteNode.lChild
			elif (isLeft):
				parent.lChild = deleteNode.lChild
			else:
				parent.rChild = deleteNode.lChild

		# delete node is a node with only right child
		elif (deleteNode.lChild == None):
			if (deleteNode == self.root):
				self.root = deleteNode.rChild
			elif (isLeft):
				parent.lChild = deleteNode.rChild
			else:
				parent.rChild = deleteNode.rChild

		# delete node is a node with both right and left children
		else:
			# find delete node's successor and successor's parent nodes
			successor = deleteNode.rChild
			successorParent = deleteNode

			while (successor.lChild != None):
				successorParent = successor
				successor = successor.lChild

			# successor node right child of delete node
			if (deleteNode == self.root):
				self.root = successor
			elif (isLeft):
				parent.lChild = successor
			else:
				parent.rChild = successor

			# connect delete node's left child to the successor's left child
			successor.lChild = deleteNode.lChild

			# successor node left descendant of delete node
			if (successor != deleteNode.rChild):
				successorParent.lChild = successor.rChild
				successor.rChild = deleteNode.rChild

		return True

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////



#  File: TestBinaryTree.py

#  Description: Adding to the Tree data structure

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 4/27/16

#  Date Last Modified: 4/29/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Node (object):
	def __init__ (self, data):

		self.data = data
		self.lChild = None
		self.rChild = None

# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):

		if (self.lChild == None) and (self.rChild == None):
			return "\nData:   {}".format(self.data)

		return "\nData:   {}\nlChild: {}\nrChild: {}".format(
			self.data, self.lChild, self.rChild)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Tree (object):
	def __init__ (self):

		self.root = None

# /////////////////////////////////////////////////////////////////////////////////

	# I've added this (in Progress) String function. It works well for full graphs
	# but doesn't handle gaps well.
	def __str__ (self):

		s = ""
		height = self.getHeight()
		space = 4 * 2**(height - 1)
		for i in range (height):
			row = self.printLevel(i + 1, "")
			row = row.strip().split()
			unitSpace = space // 2**i
			for el in row:
				s += "{:^{}}".format(el, unitSpace)
			s += "\n"

		return s

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
				if (data < current.data):
					current = current.lChild
				else:
					current = current.rChild

			# once on the according leaf, sets as one of the children
			if (data < parent.data):
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
	def preOrder (self):

		aNode = self.root
		if (aNode.lChild == None) and (aNode.rChild == None):
			return aNode.data

		lTree = Tree()
		lTree.root = aNode.lChild
		rTree = Tree()
		rTree.root = aNode.rChild

		return aNode.data + " " + lTree.preOrder() + " " + rTree.preOrder()

# /////////////////////////////////////////////////////////////////////////////////

	# post order traversal - left, right, center
	def postOrder (self):

		aNode = self.root
		if (aNode.lChild == None) and (aNode.rChild == None):
			return aNode.data

		lTree = Tree()
		lTree.root = aNode.lChild
		rTree = Tree()
		rTree.root = aNode.rChild

		return "{:>3} {:>3} {:>3}".format(
			lTree.postOrder() + " " + rTree.postOrder() + " " + aNode.data)

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

	# in isSimilar, instead of using nodes, I used an entire Tree input
	def isSimilar (self, other):

		# essentially, this whole function is a bunch of logic strings
		#	to make sure the trees are constucted the same way and they 
		#	have the same data values.
		# For all of isSimilar, srTree represents the right subtree of sCurrent,
		#	slCurrent represents the left subtree of sCurrent, etc.
		sCurrent = self.root
		oCurrent = other.root
		if (sCurrent == None) and (oCurrent != None):
			return False
		if (sCurrent != None) and (oCurrent == None):
			return False

		# first, when confronted with a leaf on sCurrent,
		if (sCurrent.lChild == None) and (sCurrent.rChild == None):
			# make sure oCurrent has no children,
			if (oCurrent.lChild != None) or (oCurrent.rChild != None):
				return False
			# then compares the data - this is the base case.
			else:
				return True and (sCurrent.data == oCurrent.data)

		# second, if sCurrent only has a rChild
		elif (sCurrent.lChild == None):
			# make sure oCurrent has only a rChild
			if (oCurrent.lChild != None) or (oCurrent.rChild == None):
				return False
			# then compares the rChild subtree for both
			else:
				srTree = Tree()
				srTree.root = sCurrent.rChild
				orTree = Tree()
				orTree.root = oCurrent.rChild
				return srTree.isSimilar(orTree)

		# same as above but reversed
		elif (sCurrent.rChild == None):
			if (oCurrent.rChild != None):
				return False
			else:
				slTree = Tree()
				slTree.root = sCurrent.lChild
				olTree = Tree()
				olTree.root = oCurrent.lChild
				return srTree.isSimilar(orTree)

		# lastly, when sCurrent has rChild and lChild
		else:
			# make sure oCurrent has both
			if (oCurrent.lChild == None) or (oCurrent.rChild == None):
				return False
			# now compare the right and left subtrees
			else:
				srTree = Tree()
				srTree.root = sCurrent.rChild
				slTree = Tree()
				slTree.root = sCurrent.lChild
				orTree = Tree()
				orTree.root = oCurrent.rChild
				olTree = Tree()
				olTree.root = oCurrent.lChild
				return (srTree.isSimilar(orTree)) and (slTree.isSimilar(olTree))

# /////////////////////////////////////////////////////////////////////////////////

	# s is the string constructed in the process. Typically is just ""
	def printLevel (self, level, s):

		current = self.root
		if (current == None):
			return ""

		# base case, when we have arrived at the right level, add to s
		if (level == 1):
			return "{:<3} ".format(current.data)

		# if we've hit a leaf in this case, we aren't at the right level - return
		if (current.lChild == None) and (current.rChild == None):
			return ""

		# go down rTree
		elif (current.lChild == None):
			rTree = Tree()
			rTree.root = current.rChild
			s += rTree.printLevel(level - 1, s)

		# go down lTree
		elif (current.rChild == None):
			lTree = Tree()
			lTree.root = current.lChild
			s += lTree.printLevel(level - 1, s)

		# go down both Trees
		else:
			lTree = Tree()
			lTree.root = current.lChild
			rTree = Tree()
			rTree.root = current.rChild
			s += lTree.printLevel(level - 1, s) + rTree.printLevel(level - 1, s)

		return s

# /////////////////////////////////////////////////////////////////////////////////

	def getHeight (self):

		current = self.root
		if (current == None):
			return 0

		# the function counts up, so when it hits the bottom, it starts with 1
		#	and adds as it returns up.

		# in this case, we have hit a leaf, and start counting
		if (current.lChild == None) and (current.rChild == None):			
			return 1

		# in these cases, we go down the one route and keep adding
		elif (current.lChild == None):
			rTree = Tree()
			rTree.root = current.rChild
			return 1 + rTree.getHeight()			
		elif (current.rChild == None):
			lTree = Tree()
			lTree.root = current.lChild
			return 1 + lTree.getHeight()
		
		# in this case, we go down both trees and compare the values.
		#	whichever is larger we keep and continue.
		else:
			lTree = Tree()
			rTree = Tree()
			lTree.root = current.lChild
			rTree.root = current.rChild
			# lHi and rHi are the heights of the subtrees
			lHi = lTree.getHeight()
			rHi = rTree.getHeight()
			# compare to see which has gotten larger
			if (lHi >= rHi):
				hi = 1 + lHi
			elif (lHi < rHi):
				hi = 1 + rHi
			return hi

# /////////////////////////////////////////////////////////////////////////////////

	def numNodes (self):

		current = self.root
		if (current == None):
			return 0

		# base case - we have hit a leaf; returns 1 to be summed above
		elif (current.lChild == None) and (current.rChild == None):
			return 1

		# for the next two, we add 1 for the node to the number of nodes
		#	in the respective subtree
		elif (current.lChild == None):
			rTree = Tree()
			rTree.root = current.rChild
			return 1 + rTree.numNodes()
		elif (current.rChild == None):
			lTree = Tree()
			lTree.root = current.lChild
			return 1 + lTree.numNodes()

		# in case of two children, add 1 for node to both numNode 
		#	for both subtrees
		else:
			lTree = Tree()
			lTree.root = current.lChild
			rTree = Tree()
			rTree.root = current.rChild
			return 1 + lTree.numNodes() + rTree.numNodes()

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():

	# create three trees - two are the same and one is different

	data1 = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
	data2 = [50, 30, 70, 10, 40, 60, 80, 7, 25]

	Tree1 = Tree()
	Tree2 = Tree()
	Tree3 = Tree()

	# construct Tree1 and Tree2 using same dataset
	for i in range (len(data1)):
		Tree1.insert(data1[i])
		Tree2.insert(data1[i])
	# construct Tree3 from differnt data set
	for i in range (len(data2)):
		Tree3.insert(data2[i])

	# test isSimilar()
	# Tree1 and Tree2 are exact, Tree3 is different
	print ("\nTest Tree1.isSimilar(Tree2): {}".format(Tree1.isSimilar(Tree2)))
	print ("Test Tree1.isSimilar(Tree3): {}".format(Tree1.isSimilar(Tree3)))

	# print the various levels of two of the trees that are different
	# I'm going to print all levels of both Tree1 and Tree3
	print ("\nTree1: ")
	for i in range (Tree1.getHeight()):
		print ("Level {}: {}".format(i + 1, Tree1.printLevel(i + 1, "")))
	print ("\nTree3: ")
	for i in range (Tree3.getHeight()):
		print ("Level {}: {}".format(i + 1, Tree3.printLevel(i + 1, "")))

	# get the height of the two trees that are different
	print ("\nHeight of Tree1: {}".format(Tree1.getHeight()))
	print ("Height of Tree3: {}".format(Tree3.getHeight()))

	# get the number of nodes in the left and right subtree
	# I'm using Tree1 and going to make lTree and rTree off of it. 
	# I'll print total nodes for Tree 1, which should equal
	#	1 + numNodes(lTree) + numNodes(rTree)
	lTree = Tree()
	rTree = Tree()
	lTree.root = Tree1.root.lChild
	rTree.root = Tree1.root.rChild
	print("\nTree1.numNodes(): {}".format(Tree1.numNodes()))
	print("lTree.numNodes(): {}".format(lTree.numNodes()))
	print("rTree.numNodes(): {}".format(rTree.numNodes()))



main()

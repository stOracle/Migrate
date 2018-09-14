#  File: ExpresssionTree.py

#  Description: An algorithm to do math using a tree

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 4/24/16

#  Date Last Modified: 4/25/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Stack (object):
	def __init__ (self):
		self.stack = []

# /////////////////////////////////////////////////////////////////////////////////

	def push (self, item):
		self.stack.append(item)

# /////////////////////////////////////////////////////////////////////////////////

	def pop (self):
		return self.stack.pop()

# /////////////////////////////////////////////////////////////////////////////////

	def peek (self):
		return self.stack[-1]

# /////////////////////////////////////////////////////////////////////////////////

	def isEmpty (self):
		return (len(self.stack) == 0)

# /////////////////////////////////////////////////////////////////////////////////

	def size (self):
		return (len(self.stack))

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.rChild = None
		self.lChild = None

# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):
		if (self.lChild == None) and (self.rChild == None):
			return "Data:   {}".format(self.data)

		return "Data:   {}\nlChild: {}\nrChild: {}".format(
			self.data, self.lChild, self.rChild)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Tree (object):
	def __init__(self):
		self.root = None

# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):
		return str(self.root)

# /////////////////////////////////////////////////////////////////////////////////

	def createTree (self, s):

		# start the tree with 'empty' node, set it to current
		self.root = Node(" ")
		current = self.root

		# start the stack
		stack = Stack()

		Tokens = ["+", "-", "*", "/"]

		for el in s:	

			# for the following, I just followed Mitra's algorithm	
			if (el == "("):
				newNode = Node(" ")
				current.lChild = newNode
				stack.push(current)
				current = newNode
				
			elif (el == ")"):				
				if (stack.isEmpty()):
					break
				else:
					current = stack.pop()

			# if el is an operator
			elif (el in Tokens):
				newNode = Node(" ")
				current.data = el
				current.rChild = newNode
				
				stack.push(current)
				current = newNode

			# if el is a number
			else:
				current.data = el
				current = stack.pop()

# /////////////////////////////////////////////////////////////////////////////////

	def evaluate (self):

		# I changed evaluate so it doesn't need an imput parameter. 
		# 	it becomes a recursive method of the tree Class which
		#	breaks the trees into subtrees to run the method on

		aNode = self.root

		# once you hit the bottom of the tree, return the data
		if (aNode.lChild == None) and (aNode.rChild == None):
			return int(aNode.data)

		# create two trees for the left sub-tree and the right sub-tree
		lTree = Tree()
		lTree.root = aNode.lChild
		rTree = Tree()
		rTree.root = aNode.rChild

		if (aNode.data == "+"):
			return lTree.evaluate() + rTree.evaluate()
		elif (aNode.data == "-"):
			return lTree.evaluate() - rTree.evaluate()
		elif (aNode.data == "*"):
			return lTree.evaluate() * rTree.evaluate()
		elif (aNode.data == "/"):
			return lTree.evaluate() / rTree.evaluate()

# /////////////////////////////////////////////////////////////////////////////////

	def evaluate2 (self, s):

		# I included a second evaluate function which uses the stack
		#	rather than recursion because I didn't know which you wanted.

		s = s.split()

		theStack = Stack()
		Tokens = ["+", "-", "*", "/"]

		total = 0
		for el in s:
			if (el in Tokens):
				oper2 = int(theStack.pop())
				oper1 = int(theStack.pop())
				if (el == "+"):
					val = oper1 + oper2
				elif (el == "-"):
					val = oper1 - oper2
				elif (el == "*"):
					val = oper1 * oper2
				else:
					val = int(oper1 / oper2)

				theStack.push(val)

			else:
				theStack.push(el)

		return theStack.pop()


# /////////////////////////////////////////////////////////////////////////////////
	
	# recursive function which creates a left and right sub-tree to run the 
	#	method on. Same for postOrder. 
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

	def postOrder (self):

		aNode = self.root
		if (aNode.lChild == None) and (aNode.rChild == None):
			return aNode.data

		lTree = Tree()
		lTree.root = aNode.lChild
		rTree = Tree()
		rTree.root = aNode.rChild

		return lTree.postOrder() + " " + rTree.postOrder() + " " + aNode.data

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():

	inFile = open("expression.txt", "r")

	for line in inFile:

		st = line.strip()
		exp = line.strip().split()
		ExpTree = Tree()
		ExpTree.createTree(exp)

		print("\n{} = {}".format(st, int(ExpTree.evaluate())))
		print("Prefix Expression: {}".format(ExpTree.preOrder()))
		print("Postfix Expression: {}".format(ExpTree.postOrder()))

	inFile.close()

main()
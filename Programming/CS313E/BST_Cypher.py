#  File: BST_Cipher.py

#  Description: An encryption algorithm using a binary searchtree

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 5/1/16

#  Date Last Modified: 5/2/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Queue (object):
	def __init__ (self):
		self.queue = []

# /////////////////////////////////////////////////////////////////////////////////

	def enqueue (self, item):
		self.queue.append(item)

# /////////////////////////////////////////////////////////////////////////////////

	def dequeue (self):
		return self.queue.pop(0)

# /////////////////////////////////////////////////////////////////////////////////

	def isEmpty (self):
		return (len(self.queue) == 0)

# /////////////////////////////////////////////////////////////////////////////////

	def size (self):
		return (len(self.queue))

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.rChild = None
		self.lChild = None

# /////////////////////////////////////////////////////////////////////////////////

	# returns True a node is a leaf
	def isLeaf(self):
		return (self.lChild == None) and (self.rChild == None)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Tree (object):
	def __init__(self, encrypt_str):

		# for the init function, estabish the key, set the root,
		#	and for the rest of the characters, use the insert() 
		#	method to construct
		st = encrypt_str.lower().strip()
		self.root = Node(st[0])

		# char_used makes sure we don't make multiple entries for
		#	the same character
		char_used = [st[0]]
		for i in range (1, len(st)):
			if (st[i] not in char_used):
				self.insert(st[i])
				char_used.append(st[i])

# /////////////////////////////////////////////////////////////////////////////////

	def insert(self, ch):

		# set current as the root
		current = self.root

		# run loop until it breaks
		while True:

			# either go left or right
			#	because of char_used, no value will be exactly equal	
			if (ord(ch) < ord(current.data)):
				# if it wants to go left and can't, set the value to a child
				if current.lChild == None:
					current.lChild = Node(ch)
					return
				# if not, keep going
				current = current.lChild

			# same as above
			elif (ord(ch) > ord(current.data)):
				if current.rChild == None:
					current.rChild = Node(ch)
					return
				current = current.rChild

# /////////////////////////////////////////////////////////////////////////////////

	def search(self, ch):

		# establish current and start the s string
		current = self.root
		s = ""

		# if you don't have a key-tree, return nothing
		if (current == None):
			return ""
		# if it's the root, immediately get out
		if (ch == self.root.data):
			return "*"

		# if you get out of the loop, it's not in the tree
		while (current != None):

			# base case: when they math, return the path so far
			if (ch == current.data):
				return s

			# for the other two, either you keep track of left or right
			if (ord(ch) < ord(current.data)):
				s += "<"
				current = current.lChild
			elif (ord(ch) > ord(current.data)):
				s += ">"
				current = current.rChild

		return ""

# /////////////////////////////////////////////////////////////////////////////////

	def traverse(self, st):

		# establish current and check if it exists
		current = self.root
		if (current == None):
			return ""
		# if the root matches, get out
		if (st == "*"):
			return current.data

		# for this part, I break the input into a queue and 
		#	go until it's empty
		queue = Queue()
		for el in st:			
			queue.enqueue(el)

		# current equalling None means the path pointed somewhere 
		#	that doesn't exist.
		#	if queue ends, you have found the right spot
		while (current != None) and (not queue.isEmpty()):
			# pull from the queue
			move = queue.dequeue()
			if (move != "<") and (move != ">") and (move != "*"):
				continue
			if (move == "<"):
				current = current.lChild
			elif (move == ">"):
				current = current.rChild

		if (current == None):
			return ""

		# error checking
		if (current == self.root):
			return ""

		return current.data

# /////////////////////////////////////////////////////////////////////////////////

	def encrypt(self, st):

		# lowercase the st and start the return string
		st = st.lower()
		code = ""

		# for every character,
		for i in range(len(st)):
			char = st[i]

			# if it's not a lowercase letter or space, skip
			if not (((ord(char) >= 97) and (ord(char) <= 122)) or (ord(char) == 32)):
				continue

			# else, add the character and end with an exclamation point
			code += self.search(char) + "!"

		# return everything except the last char, because we don't need
		#	the last "!"
		return code[0:-1]

# /////////////////////////////////////////////////////////////////////////////////

	def decrypt (self, st):

		# split the string by "!" and feed them individually to add to code
		code = ""
		moves = st.split("!")
		for el in moves:
			code += self.traverse(el)

		return code

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():

	# hard code the key
	key = "the quick brown fox jumps over the lazy dog"
	eTree = Tree(key)

	# test the encryption method
	pre_encrypt_str = str(input("\nEnter string to be encrypted: "))
	encrypt_str = eTree.encrypt(pre_encrypt_str)
	print ("Encrypted string: " + encrypt_str)

	# test the decryption method
	pre_decrypt_str = str(input("\nEnter string to be decrypted: "))	
	decrypt_str = eTree.decrypt(pre_decrypt_str)
	print ("Decrypted String: " + decrypt_str)

main()
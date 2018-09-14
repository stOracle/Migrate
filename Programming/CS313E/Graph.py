#  File: Graph.py

#  Description: program to make use of the graph data structure

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 5/9/16

#  Date Last Modified: 5/9/16

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
		return len(self.stack)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Queue (object):
	def __init__ (self):
		self.Q = []

# /////////////////////////////////////////////////////////////////////////////////

	def enqueue (self, item):
		self.Q.append (item)

# /////////////////////////////////////////////////////////////////////////////////

	def dequeue (self):
		return (self.Q.pop(0))

# /////////////////////////////////////////////////////////////////////////////////

	def isEmpty (self):
		return (len(self.Q) == 0)

# /////////////////////////////////////////////////////////////////////////////////

	def size (self):
		return len(self.Q)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Vertex (object):
	def __init__ (self, label):
		self.label = label
		self.visited = False

# /////////////////////////////////////////////////////////////////////////////////

	# determine if vertex was visited
	def wasVisited (self):
		return self.visited

# /////////////////////////////////////////////////////////////////////////////////

	# determine the label of the vertex
	def getLabel (self):
		return self.label

# /////////////////////////////////////////////////////////////////////////////////

	# string representation of the label
	def __str__ (self):
		return str(self.label)

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Edge (object):
	def __init__ (self, fromVertex, toVertex, weight):
		self.u = fromVertex
		self.v = toVertex
		self.weigh = weight

# /////////////////////////////////////////////////////////////////////////////////

	# comparison operators
	def __lt__ (self, other):
		return 

	def __le__ (self, other):
		return

	def __gt__ (self, other):
		return

	def __ge__ (self, other):
		return

	def __eq__ (self, other):
		return 

	def __ne__ (self, other):
		return

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Graph (object):
	def __init__ (self):
		self.Vertices = []
		self.adjMat = []

# /////////////////////////////////////////////////////////////////////////////////

	# checks if a vertex label already exists
	def hasVertex (self, label):
		nVert = len(self.Vertices)
		for i in range (nVert):
			if (label == self.Vertices[i].label):
				return True

		return False

# /////////////////////////////////////////////////////////////////////////////////

	# adds a vertex with given label
	def addVertex (self, label):
		if not self.hasVertex (label):
			self.Vertices.append(Vertex(label))

			# add a new column in the adj Matrix for new Vertex
			nVert = len(self.Vertices)
			for i in range (nVert - 1):
				self.adjMat[i].append(0)

			# add a new row for the new Vertex in the adj Matrix
			newRow = []
			for i in range (nVert):
				newRow.append(0)
			self.adjMat.append(newRow)

# /////////////////////////////////////////////////////////////////////////////////

	# add weighted directed edge to graph
	def addDirectedEdge (self, start, finish, weight = 1):
		self.adjMat[start][finish] = weight

# /////////////////////////////////////////////////////////////////////////////////

	# add weighted undirected edge to graph
	def addUndirectedEdge (self, start, finish, weight = 1):
		self.adjMat[start][finish] = weight
		self.adjMat[finish][start] = weight

# /////////////////////////////////////////////////////////////////////////////////

	# return an unvisited vertex adjacent to V
	def getAdjUnvisitedVertex (self, v):
		nVert = len (self.Vertices)
		for i in range (nVert):
			if (self.adjMat[v][i] > 0) and (not self.Vertices[i].wasVisited()):
				return i

		return -1

# /////////////////////////////////////////////////////////////////////////////////

	# does a depth first search in a graph
	def dfs (self, v):

		theStack = Stack()
		self.Vertices[v].visited = True
		print (self.Vertices[v])
		theStack.push(v)

		while (not theStack.isEmpty()):
			# get an adjacent unvisited vertex
			u = self.getAdjUnvisitedVertex (theStack.peek())
			if (u == -1):
				u = theStack.pop()
			else:
				self.Vertices[u].visited = True
				print (self.Vertices[u])
				theStack.push(u)

		# stack is empty reset the flags
		nVert = len(self.Vertices)
		for i in range (nVert):
			self.Vertices[i].visited = False

# /////////////////////////////////////////////////////////////////////////////////

	def bfs (self, v):
		theQ = Queue()
		self.Vertices[v].visited = True
		print (self.Vertices[v])
		theQ.enqueue(v)

		while (not theQ.isEmpty()):
			# gaet hte vertex at the front
			v1 = theQ.dequeue()
			# get an adjacent unvistited vertex
			v2 = self.getAdjUnvisitedVertex(v1)
			while (v2 != -1):
				self.Vertices[v2].visited = True
				print (self.Vertices[v2])
				theQ.enqueue (v2)
				v2 = self.getAdjUnvisitedVertex (v1)

		# queue is empty reset the flags
		nVert = len(self.Vertices)
		for i in range (nVert):
			self.Vertices[i].visited = False

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():
	cities = Graph()
	inFile = open("graph.txt", "r")

	numVertices = int(inFile.readline().strip())
	print (numVertices)

	for i in range (numVertices):
		city = inFile.readline().strip()
		print (city)
		cities.addVertex(city)

	numEdges = int((inFile.readline().strip()))
	print (numEdges)

	for i in range (numEdges):
		edge = inFile.readline().strip()
		print(edge)
		edge = edge.split()
		start = int(edge[0])
		finish = int(edge[1])
		weight = int(edge[2])
		cities.addDirectedEdge (start, finish, weight)

	startVertex = inFile.readline().strip()
	print(startVertex)

	inFile.close()

	nVert = len(cities.Vertices)
	for i in range (nVert):
		for j in range (nVert):
			print (cities.adjMat[i][j], end = " ")
		print()
	print()

	# dfs from Houston
	print ("Depth First Search from Houston")
	cities.dfs(11)
	print()

	# bfs from Houston
	print ("Breadth First Search from Houston")
	cities.bfs(11)

main()

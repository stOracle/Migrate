#  File: Music.py

#  Description: Class definition of music theory elements

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Date Created: 4/25/16

#  Date Last Modified: 5/2/16

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Link (object):
	def __init__ (self, data):
		self.data = data
		self.next = None

# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):
		return self.data

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
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

	def interval (self, note1, space):

		self.find(note1)
		current = self.first

		intervals = {"d2":0, "m2":1, "M2":2, "A2":3, "d3":2, "m3":3, "M3":4, "A3":5, 
						"d4":4, "P4":5, "A4":6, "d5":6, "P5":7, "d6":7, "m6":8, 
						"M6":9, "A6":10, "d7":9, "m7":10, "M7":11, "A7":12, "P8":12}

		idx = intervals[space]

		count = 0
		while (count != idx):
			current = current.next
			count += 1

		return current.data

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

	# return a string representation of a Circular List
	def __str__ (self):
		
		current = self.first
		st = ""
		count = 0

		if (current == None):
			return None

		while (current.next != self.first):
			st += "{:^6}".format(str(current.data))

			current = current.next
			count += 1

		return st

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Note (object):
	def __init__ (self, name):

		hz_dict = {"C":262, "C#":277, "Db": 277, "D":294, "D#":311, "Eb":311
					"E":330, "F":349, "F#":370, "Gb": 370, "G":392, "G#":415, 
						"Ab":415, "A":440, "A#":466, "Bb":466, "B":494}
		self.name = name
		self.pitch = pitch
		self.octave = 4

# /////////////////////////////////////////////////////////////////////////////////

	#def play(self):


# /////////////////////////////////////////////////////////////////////////////////

	def __str__ (self):
		return self.pitch

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Chord (object):
	def __init__ (self, root):
		self.root = Note(root)
		self.third = None
		self.fifth = None
		self.seventh = None

# /////////////////////////////////////////////////////////////////////////////////

	def major(self):
		self.third = "M3"
		self.fifth = "P5"

# /////////////////////////////////////////////////////////////////////////////////

	def minor(self):
		self.third = "m3"
		self.fifth = "P5"

# /////////////////////////////////////////////////////////////////////////////////

	def dim (self):
		self.third = "m3"
		self.fifth = "d5"

# /////////////////////////////////////////////////////////////////////////////////

	def aug (self):
		self.third = "M3"
		self.fifth = "A5"

# /////////////////////////////////////////////////////////////////////////////////

	def maj7 (self):
		self.third = "M3"
		self.fifth = "P5"
		self.seventh = "M7"

# /////////////////////////////////////////////////////////////////////////////////

	def dom (self):
		self.third = "M3"
		self.fifth = "P5"
		self.seventh = "m7"

# /////////////////////////////////////////////////////////////////////////////////

	def Min7 (self):
		self.third = "m3"
		self.fifth = "P5"
		self.seventh = "m7"

# /////////////////////////////////////////////////////////////////////////////////

	def halfDim (self):
		self.third = "m3"
		self.fifth = "d5"
		self.seventh = "m7"

# /////////////////////////////////////////////////////////////////////////////////

	def fullDim (self):
		self.third = "m3"
		self.fifth = "d5"
		self.seventh = "d7"

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Progression (object):
	# when first constructing a Progression, you will need 
	#	to establish Key and Mode - e.g. C Major, F Dorian, G minor
	#	This will dictate what the notation I, II, ... will mean
	def __init__ (self, key = None, mode = None):
		self.key = key
		self.mode = mode

# /////////////////////////////////////////////////////////////////////////////////

	# pulls from CSV file to make the n amount of chords
	def make(self):
		pass

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Song (object):
	def __init__ (self, key, file_name):

		notes_sharps = ["C", "C#", "D", "D#", "E", "F", 
				"F#", "G", "G#", "A", "A#", "B"]
		notes_flats = ["C", "Db", "D", "Eb", "E", "F", 
				"Gb", "G", "Ab", "A", "Bb", "B"]

		self.notes = CircularList()
		if (key in ["C", "D", "E", "F", "G", "A", "B"]):
			for i in notes_sharps:
				self.notes.insert(Note(i))
				self.notes.find(key)
		else:
			for i in notes_flats:
				self.notes.insert(Note(i))
				self.notes.find(key)

		in_file = open(file_name, "r")
		self.chords = []
		for line in in_file:
			line = line.strip().split()
			if (len(line) == 3):
				chord = Chord(Note(line[0]))
				chord.third = Note(line[1])
				chord.fifth = Note(line[2])
				chords.append()
			if (len(line) == 4):
				chord = Chord(Note(line[0]))
				chord.third = Note(line[1])
				chord.fifth = Note(line[2])
				chord.seventh = line[3]

		in_file.close()

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

def main():
	# notes = ["C", "C#/Db", "D", "D#/Eb", "E", "F", 
	# 			"F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

	notes = ["C", "C#", "D", "D#", "E", "F", 
				"F#", "G", "G#", "A", "A#", "B"]

	global chromatic
	chromatic = CircularList()
	for el in notes:
		chromatic.insert(el)

	print (chromatic)
	chromatic.find("A")
	print (chromatic)
	print()
	for note in notes:
		root = note
		print ("{:^5} Maj = {}, {}, {}".format(root, root, chromatic.interval(root, "M3"), 
			chromatic.interval(root, "P5")))

main()
# Define the vector object
class Vector(object):
  # Constructor
  def __init__(self, x):
    if type(x) == type(0):
      self.n = x
      self.vect = [0]*x
    else:
      self.n = len(x)
      self.vect = list(x)

  # Return a copy of the vector
  def copy(self):
    clone = Vector(self.size())
    clone.vect = self.vect[:]
    return clone

  # Define vector addition
  def __add__(self, y):
    Sum = self.copy()
    n = Sum.size()
    for i in range(n):
      Sum.vect[i] += y.vect[i]
    return Sum

  # Define vector subtraction
  def __sub__(self, y):
    Sum = self.copy()
    n = Sum.size()
    for i in range(n):
      Sum.vect[i] -= y.vect[i]
    return Sum

  # Define scalar multiplication
  def times(self, c):
    scaled = self.copy()
    n = scaled.size()
    for i in range(n):
      scaled.vect[i] *= c
    return scaled

  # Define vector dot product
  def __mul__(self, other):
    if self.size() != other.size():
      print("ERROR: Can't dot vectors of different length!")
      exit()
    prod = 0
    for i in range(self.size()):
      prod += self.item(i) * other.item(i)
    return prod

  # Define scalar division
  def __truediv__(self, c):
    return self.times(1.0/c)

  # Returns the projection of self onto other
  def proj(self, other):
    other2 = other*other
    # Handle special case: norm = 0
    if other2 == 0:
        other2 = 0.0001
    return other.times((other*self)/other2)

  # Return the size of the vector
  def size(self):
    return self.n

  # Define how to display a vector
  def __str__(self):
    return str(self.vect)

  # Return the i-th item of the vector
  def item(self, i):
    return self.vect[i]

# Returns the Euclidean norm of a vector.
def Norm(v):
  n = v.size()
  N = 0
  for i in range(n):
    N += v.vect[i]**2
  return N**0.5

# Returns unit vector representing the direction of v
# i.e. returns v / norm(v)
def unit(v):
  N = Norm(v)
  # Handle special case norm = 0
  if N==0:
    N = 0.0001
  return v.times(1.0/N)
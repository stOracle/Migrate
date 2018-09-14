def gcd(num_1, num_2):
  div = 1
  g_div = 0
  for div in range (1, num_1 + 1):
    if (num_1 % div != 0):
      div += 1
      continue
    else:
      if (num_2 % div == 0) and (div > g_div):
        g_div = div
        div += 1
  return (g_div)
      

def dio_eq(coef_x, coef_y, sol):
  if (sol % gcd(coef_x, coef_y) == 0):
    for x in range (-10000, 10000):
      for y in range (-10000, 10000):
        if (coef_x * x + coef_y * y == sol):
          return (x, y)
          break
        else:
          continue
      
  else:
    return ("There are no integer solutions to this equation")
def main():
  print ("ax + by = c")
  a = int(input("Enter value of a:"))
  b = int(input("Enter value of b:"))
  c = int(input("Enter value of c:"))
  d = gcd(a, b)

  x,y = dio_eq(a, b, c)
  if (a > b):
    while (x < 0):
      x += b // d
      y -= a // d
  else:
    while (y > 0):
      x += b // d
      y -= a // d
    
  print ("x =", x)
  print ("y =", y)
  


main()
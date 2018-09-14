def sum_divisors (n):
  if (n == 1):
    return 0
  sum_d = 0
  limit = n // 2 + 1
  for div in range (1, limit):
    if (n % div == 0):
      sum_d += div
  return sum_d

def main():
  x = 1
  y = 1
  while (x, y <= 10,000):
    for x in range (1, 10001):
      if  == x
    if (x == sum_divisors(y)) and (y == sum_divisors(x)) and (x < y):
      print (x, "and", y, "are amicable numbers", end = ".")
  x, y += 1

main()
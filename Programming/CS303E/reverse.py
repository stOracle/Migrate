def rev(x):
  r = 0
  while(x > 0):
    r = 10 * r + x % 10
    x = x // 10
  return r

def main():
  n = int(input("Enter an integer:"))
  print("The reversed number is", rev(n))

main()
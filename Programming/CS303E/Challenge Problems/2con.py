def main():
  n = 0
  while (n < 56406 ** .5):
    if (n * (n + 1) != 56406):
      n += 1
    elif (n * (n + 1) == 56406):
      print("The numbers", n, "and", (n+1), "multiply to 56406", end = ".")
      break

main()
      
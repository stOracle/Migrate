def main():
  n = 1
  while ((n < (357627 ** 1/3) + 1)):
    n += 2
    if ((n * (n+2) * (n+4)) == 357627):
      print("The numbers", n, (n + 2), "and", (n + 4), "multiply to make 357627", end = ".")
      break
main()
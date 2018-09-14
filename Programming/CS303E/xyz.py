def xyz_there(str):
  
  if (len(str) < 3):
    return False
  for i in range (len(str) -3):
    s = str[i:i + 4]
    print (s)
    if (s[1:] == "xyz") and (str[0] != "."):
      return True
    else:
      continue
  return False
      
def main():

  string = str(input("enter"))
  print (xyz_there(string))

main()
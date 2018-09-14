# Removes punctuation marks from a string
def stripPunct(st):
  st = st.strip()
  newSt = ""

  # loop thru each character in the string and decide what characters
  # to keep, and which to throw out.
  for i in range(len(st)):
    ch = st[i]
    if ch.isalpha() or ch.isspace():  # if it is a letter or a space, keep it
      newSt += ch
    elif i==len(st)-1:  # elif it's the last character, skip it
      break
    # elif there is an ('s) at the end of the line, skip it
    elif i==len(st)-2 and ch=="'" and st[i+1]=="s":
      break
    elif ch=="'":  # elif it's an apostrophe, skip it
      continue
    else:  # otherwise, replace the character with a space
      newSt += " "
  newSt = newSt.strip()
  return newSt

def main():
  book = open("Sherlock.txt", "r")  # open file for reading
  wordList = []
  wordFreq = {}  # define empty dictionary

  print("Finding all words.")
  # for each line in the book, grab its words and add it to the list
  for line in book:
    line = line.strip().lower()
    line = stripPunct(line)
    wordList += line.split()
  book.close()

  print("Writing all words to file.")
  allWords = open("allwords.txt", "w")
  for word in wordList:
    allWords.write(word+"\n")
  allWords.close()

  print("Computing raw word frequencies.")
  # Count up the number of occurences for each word.
  for word in wordList:
    if word in wordFreq:
      wordFreq[word] += 1
    else:
        wordFreq[word] = 1

  # Remove repeated words and sort
  wordList = set(wordList)
  wordList = list(wordList)
  wordList.sort()

  print("Writing raw word frequencies to file.")
  file = open("rawFreqs.txt", "w")
  for word in wordList:
    file.write(word)
    file.write(":")
    file.write(str(wordFreq[word]))
    file.write("\n")
  file.close()

  print("Finding unique words.")
  uniques = []
  for word in wordFreq:
    if wordFreq[word] == 1:
      uniques.append(word)
  uniques.sort()

  print("Writing unique words to file.")
  file = open("uniquewords.txt", "w")
  for word in uniques:
    file.write(word+"\n")
  file.close()

  # Compute the word distribution in the format
  # (number of occurences : number of unique words that occur that many times)
  print("Computing final frequency distribution.")
  # Grab all possible word frequencies and list them in ascending order
  freqs = set(wordFreq.values())
  freqs = list(freqs)
  freqs.sort()
  distr = {}  # Initialize the distribution dictionary
  # For each frequency: count up the number of words that have that frequency.
  # Record the result in the distr dictionary.
  for f in freqs:
    count = 0
    for word in wordFreq:
      if wordFreq[word] == f:
        count += 1
    distr[f] = count

  print("Writing frequency distribution to file.")
  file = open("wordfrequency.txt", "w")
  for f in freqs:
    file.write(str(f))
    file.write(":")
    file.write(str(distr[f]))
    file.write("\n")
  file.close()

  print("Done!")

main()

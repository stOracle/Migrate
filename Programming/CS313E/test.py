def mergeSort (a, left, right):
  if (left < right):
    print("*STACK* ms(a, {}, {})\n   a = {}".format(left, right, a))
    center = (left + right) // 2
    mergeSort (a, left, center)
    mergeSort (a, center + 1, right)
    merge_sort (a, left, center, right)
    print("*POP* ms(a, {}, {})\n   a = {}".format(left, right, a))

def merge_sort (a, left, center, right):
  print("*STACK* m_s(a, {}, {}, {})\n   a = {}\n".format(left, center, right, a))
  first1 = left
  last1 = center
  first2 = center + 1
  last2 = right
  b = []

  while ((first1 <= last1) and (first2 <= last2)):
    if (a[first1] < a[first2]):
      b.append(a[first1])
      first1 = first1 + 1
    else:
      b.append(a[first2])
      first2 = first2 + 1

  while (first1 <= last1):
    b.append(a[first1])
    first1 = first1 + 1

  while (first2 <= last2):
    b.append(a[first2])
    first2 = first2 + 1

  idxA = left
  for i in range (len(b)):
    a[idxA] = b[i]
    idxA = idxA + 1

  print("*POP* m_s(a, {}, {}, {})\n   a = {}".format(left, center, right, a))


def main():
  a = [3, 8, 10, 15, 2, 7, 1, 9]
  mergeSort(a, 0, len(a) - 1)

main()
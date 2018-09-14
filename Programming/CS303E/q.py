sum_n = 0
idx = 1
while (idx < 23):
	print("sum =", sum_n, "idx =", idx)
	if (idx == 9 ):
		break
	if (idx % 5 != 0):
		sum_n += idx
	idx += 2
print(sum_n)

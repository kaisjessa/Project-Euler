num = 2
total_sum = 0
for x in range(10**6):
	total = 0
	arr = [int(i) for i in list(str(num))]
	for a in arr:
		total += a**5
	if(total == num):
		total_sum += num
	num += 1
print(total_sum)
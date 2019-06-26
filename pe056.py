
def sum_of_digits(n):
	total = 0
	for i in str(n):
		total += int(i)
	return(total)

max_sum = 0
for a in range(1, 101):
	for b in range(1, 101):
		max_sum = max(sum_of_digits(a**b), max_sum)
print(max_sum)

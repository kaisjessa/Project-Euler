arr = list(range(1, 10000))
count = 0

def sum_factors(x):
	total = 0
	for i in range(1, x):
		if(x % i == 0):
			total += i
	return(total)

for i in arr:
	si = sum_factors(i)
	sii = sum_factors(si)
	if(i == sii and si in arr and i != si):
		print(i, si)
		count += i
		count += si
		arr.remove(i)
print(count)
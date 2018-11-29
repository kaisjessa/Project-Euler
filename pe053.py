import math

def combinatorics(n ,r):
	return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

million_count = 0
for n in range(23, 101):
	for r in range(n):
		if(combinatorics(n,r) > 1000000):
			million_count += (n-r)-r+1
			break
print(million_count)
count = 0
arr = []
n = 0
for n in range(1, 1000):
	base = 1
	sol = 0
	while(len(str(sol)) <= n):
		sol = base**n
		if(len(str(sol)) == n): #if the number has n digits
			count += 1
			arr.append([sol, base, n])
		base += 1
print(count)
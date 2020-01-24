import math

def prime_factors(x):
	factors = []
	current = 2
	new_x = x
	while current <= math.ceil(math.sqrt(x)+1):
		if new_x % current == 0:
			factors.append(current)
			new_x = new_x / current
		else:
			current += 1
	if(new_x != 1):
		factors.append(int(new_x))
	return list(set(factors))

def euler(n):
	facts = prime_factors(n)
	prod = 1
	for fact in facts:
		prod *= (1-1/fact)
	return int(n*prod)

nphi = 0
maxn = 0
for n in range(10**6, 0, -1):
	temp = n/euler(n)
	if temp > nphi:
		nphi = temp
		maxn = n
print(maxn)
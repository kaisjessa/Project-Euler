import math

def isPrime(x):
	temp = int(math.sqrt(x)+1)
	if x%2==0:
		return False
	for i in range(3,temp,2):
		if(x%i==0):
			return False
	return True


total = 2
for n in range(3, 2 * 10**5, 2):
	total += n if isPrime(n) else 0
print(total)
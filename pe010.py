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
for n in range(3, 2000000, 2):
	if isPrime(n):
		total += n
print(total)
import math
prime = 600851475143

def checkPrime(n):
	for i in range(int(math.ceil(math.sqrt(n))), 2, -1):
		if(n%i==0):
			return False
	return True

for i in range(int(math.ceil(math.sqrt(prime))), 1, -1):
	if(prime%i==0 and checkPrime(i)):
		print(i)
		quit()


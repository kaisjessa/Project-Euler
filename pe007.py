import math
count = 1

n = 3

def isPrime(x):
	upper = int(math.sqrt(x))+1
	for i in range(2, upper):
		if(x%i == 0):
			return False
	return True



while True:
	if(isPrime(n)):
		count += 1
	if count == 10001:
		print(n)
		quit()
	n += 2

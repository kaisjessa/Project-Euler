import math
prime_list = [2]

def is_prime(x):
	if(x in prime_list):
		return True
	if(x<2):
		return False
	if(x==2):
		return True
	if(x%2==0):
		return False
	for i in range(3, math.ceil(math.sqrt(x))+1, 2):
		if x % i == 0:
			return False
	if(x not in prime_list):
		prime_list.append(x)
	return True

for i in range(10**5):
	is_prime(i)

print(prime_list)
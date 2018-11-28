import math
prime_list = []

def is_prime(x):
	if x in prime_list:
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
	prime_list.append(x)
	return True

def prime_factors(x):
	factors = []
	current = 2
	new_x = x
	while current <= math.ceil(math.sqrt(x)+1):
		if new_x % current == 0:
			factors.append(current)
			new_x = new_x / current
		else:
			if(is_prime(new_x)):
				factors.append(new_x)
				return(len(list(set(factors))))
			current += 1
	return(len(list(set(factors))))

found = False
index = 2*3*5*7
while not found:
	if(index % 1000 == 0):
		print(index)
	if(prime_factors(index)==4):
		index += 1
		if(prime_factors(index)==4):
			index += 1
		if(prime_factors(index)==4):
			index += 1
		if(prime_factors(index)==4):
			print(index-3)
			found = True
	index += 1




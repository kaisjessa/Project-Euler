import math

def is_prime(x):
	if(x<2):
		return False
	if(x==2):
		return True
	if(x%2==0):
		return False
	for i in range(3, math.ceil(math.sqrt(x)), 2):
		if x % i == 0:
			return False
	return True

def prime_factors(x):
	factors = []
	current = x
	n = x
	while current != 1:
		if(is_prime(n) and current%n==0):
			factors.append(n)
			current = current / n
		else:
			n -= 1

	list = []
	temp_list = []
	for e in sorted(factors):
		if e in temp_list or len(temp_list)==0:
			temp_list.append(e)
		else:
			list.append(temp_list)
			temp_list = [e]
	list.append(temp_list)
	return(list)

found = 0
index = 1
while not found:
	index += 1
	f1 = prime_factors(index)
	f2 = prime_factors(index+1)
	f3 = prime_factors(index+2)
	f4 = prime_factors(index+3)
	if(len(f1)==4 and len(f2)==4 and len(f3)==4 and len(f4)==4):
		print(set(f1).intersection(set(f2),set(f3),set(f4)))



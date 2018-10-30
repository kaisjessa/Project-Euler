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

def check_conjecture(x):
	diff = x
	i = 1
	while diff >= 0:
		diff = x - 2*i**2
		if(is_prime(diff)):
			return True
		i += 1
	return False


found = 0
index = 1
while found == 0:
	index += 2
	if not is_prime(index) and not check_conjecture(index):
		found = index
print(index)

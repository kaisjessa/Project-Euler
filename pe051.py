import math

def is_prime(x):
	if(x<2):
		return False
	if(x==2):
		return True
	if(x%2==0):
		return False
	for i in range(3, math.ceil(math.sqrt(x))+1, 2):
		if x % i == 0:
			return False
	return True

def repeated_digits(x):
	if(len(set(list(str(x)))) != len(list(str(x)))):
		return True
	return False

def value_family(prime):
	count = 0
	for i in str(prime):
		if str(prime).count(i) > 1:
			repeat = i
			break
	if(str(prime).index(repeat) == 0):
		start = 1
	else:
		start = 0
	for x in range(start, 10):
		temp = int(str(prime).replace(i,str(x)))
		if(is_prime(temp)):
			count += 1
	return count

def find_prime(target_value_family=8):
	correct_prime = 0
	current_integer = 0
	while correct_prime == 0:
		current_integer += 1
		if(repeated_digits(current_integer) and is_prime(current_integer) and value_family(current_integer) == target_value_family):
			return(current_integer)
print(find_prime())
import math
max_primes_length = 0
max_prime = 0

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
	return True

def generate_primes(lim):
	l = []
	for i in range(lim):
		if is_prime(i):
			l.append(i)
	return l

prime_list = generate_primes(10**4)

for starting_index in range(0, len(prime_list)):
	current_sum = 0
	index = starting_index
	num_primes = 0
	while current_sum < 10**6 and index < len(prime_list):
		current_sum += prime_list[index]
		num_primes += 1
		if(is_prime(current_sum) and num_primes > max_primes_length):
			max_primes_length = num_primes
			max_prime = current_sum
		index += 1
print(max_prime)
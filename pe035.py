import math
def is_prime(x):
	temp = int(math.sqrt(x)+1)
	if(x==2):
		return True
	if x%2==0:
		return False
	for i in range(3,temp,2):
		if(x%i==0):
			return False
	return True

def circular_prime(x):
	arr = [c for c in str(x)]
	for i in range(len(str(x))):
		n_str = "".join(arr)
		if(not is_prime(int(n_str))):
			return False
		new_arr = arr[1:]
		new_arr.append(arr[0])
		arr = new_arr
	return True




num_primes = 1
for i in range(3, 10**6, 2):
	if(is_prime(i)):
		if(circular_prime(i)):
			num_primes += 1
print(num_primes)
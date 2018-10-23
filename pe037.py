import math
def is_prime(x):
	if(x<2):
		return False
	if(x==2):
		return True
	if x%2==0:
		return False
	temp = int(math.sqrt(x)+1)

	for i in range(3,temp,2):
		if(x%i==0):
			return False
	return True

def back_front_prime(x):
	n = x
	while(len(str(n))>1):
		if(not is_prime(n)):
			return False
		n = int(str(n)[1:])

	m = x
	while(len(str(m))>1):
		if(not is_prime(m)):
			return False
		m = int(str(m)[:-1])

	if(is_prime(n) and is_prime(m)):
		return True
	return False

count = 0
total = 0
num = 11
while(count < 11):
	if(is_prime(num) and back_front_prime(num)):
		total += num
		count += 1
	num += 2

print(total)
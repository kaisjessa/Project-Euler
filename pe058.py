import math
'''
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

'''
def spiral(x):
	diagonals = []
	count = 0
	increment = 2
	i=1
	while(i <= x**2):
		diagonals.append(i)
		count += 1
		i += increment
		if count % 4 ==0:
			increment += 2
	return(diagonals)

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

#each entry is ([all numbers on diagonals, all primes on diagonals])
#dynamic_array = [[[0], [0]], [[0], [0]], [[3, 5, 7, 9], [3, 5, 7]]]
ratio = 1
i = 3
count = 5
primes = 3
while ratio >= 0.1:
	i += 2
	arr = spiral(i)[-4:]
	count += 4
	for a in arr:
		if(is_prime(a)):
			primes += 1
	ratio = float(primes)/count

print(i)
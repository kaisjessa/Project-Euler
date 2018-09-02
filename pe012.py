import math
tri_n = 0
i = 1


def factors(x):
	count = 0
	temp = int(math.ceil(math.sqrt(x))+1)
	for j in range(1, temp, 1):
		if(x % j == 0):
			count += 2
		if(j**2 == x):
			count -= 1
	return count

while True:
	tri_n += i
	i += 1

	
	if(factors(tri_n) >= 500):
		print(tri_n)
		quit()
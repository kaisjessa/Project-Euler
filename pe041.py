import math
import itertools
import sys
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

# def is_pandigital(x):
# 	if('0' in str(x)):
# 		return False
# 	arr = [str(n) for n in range(1, 10)]
# 	for i in arr:
# 		if(str(x).count(i) > 1):
# 			return False
# 	return True
digits = [1,2,3,4,5,6,7,8,9]
pandigitals = sorted(list(itertools.permutations(digits)))[::-1]
while(len(pandigitals)>0):
	for i in pandigitals:
		num = int("".join([str(x) for x in list(i)]))
		if(is_prime(num)):
			print(num)
			sys.exit()
	digits = digits[:-1]
	pandigitals = sorted(list(itertools.permutations(digits)))[::-1]
print("none")


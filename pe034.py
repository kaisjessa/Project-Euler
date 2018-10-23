import math
'''
Determine upper bound
x9! = x-digit num
'''

upper_bound = 0
x = 1
while len(str(upper_bound)) <= x:
	upper_bound = x * math.factorial(9)
	x += 1


def factorial_digits(n):
	temp = 0
	arr = [int(c) for c in str(n)]
	for x in arr:
		temp += math.factorial(x)
	return temp

total = 0
for i in range(3, upper_bound):
	if(factorial_digits(i) == i):
		total += i
print(total)


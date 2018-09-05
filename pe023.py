import math
upper = 28123
def is_abundant(x):
	s = 1
	temp = int(math.floor(math.sqrt(x)+1))
	for i in range(2, temp):
		if(x % i == 0):
			s += i
			if(i != int(x/i)):
				s += int(x/i)
	if s > x:
		return True
	return False

abundant_list = []
for i in range(1, upper):
	if(is_abundant(i)):
		abundant_list.append(i)


nums = set(range(upper+1))
sumlist = []
i = 0
for i in range(0, len(abundant_list)):
	for j in range(i, len(abundant_list)):
		temp = abundant_list[i] + abundant_list[j]
		if(temp <= upper):
			sumlist.append(temp)
sumlist = set(sumlist)
print(sum(nums-sumlist))
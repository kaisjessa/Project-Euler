import math
import itertools
import collections

prime_list = []
correct_list = []
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
	prime_list.append(x)
	return True

def difference_list(a):
	temp = []
	for i in a:
		for j in a:
			if j > i and (j+j-i) in a and i != 1487:
				return (i, j, j+j-i)
	return (None, None, None)

def check_valid(arr):
	prime_count = 0
	working_nums = []
	for elem in arr:
		t = int("".join([str(x) for x in elem]))
		if(is_prime(t)):
			prime_count += 1
			working_nums.append(t)
	working_nums.sort()
	return working_nums



'''
arr = [x for x in range(1000, 10000) if is_prime(x)]
print(arr)
arr2 = []
for e in arr:
	if(sorted(list(str(e)))):
		arr2.append(sorted(list(str(e))))
print(arr2)
'''
for x in range(1000, 10000):
	int_perms = []
	if(is_prime(x)):
		all_perms = list(set(list(itertools.permutations([int(i) for i in str(x)]))))
		for y in all_perms:
			if(list(y)[0] != 0):
				int_perms.append(list(y))
		temp_list = check_valid(int_perms)
		answer = difference_list(temp_list)
		if(answer != (None, None, None)):
			print(str(answer[0]) + str(answer[1]) + str(answer[2]))
			break

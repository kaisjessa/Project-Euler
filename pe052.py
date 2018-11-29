import math
def check_lists(a, l):
	a1 = sorted(list(str(a)))
	for i in range(2,l+1):
		if a1 != sorted(list(str(a*i))):
			return False
	return True


x = 0
temp = 0
while x == 0:
	temp += 1
	if(check_lists(temp, 6)):
		x = temp
print(x)

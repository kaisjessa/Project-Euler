max_pan = 0
def is_pandigital(x):
	if(len(str(x)) != 9):
		return False
	arr = [str(c) for c in range(1, 10)]
	for i in arr:
		if(str(x).count(str(i)) != 1):
			return False
	return True
for i in range(1, 10**5):
	s_num = str(i)
	n = 2
	while len(s_num+str(i*n)) < 10:
		s_num += str(i*n)
		n += 1
	if(is_pandigital(int(s_num)) and int(s_num) > max_pan):
		max_pan = int(s_num)

print(max_pan)
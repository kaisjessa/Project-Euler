def check_multiple(n, x):
	if x==1:
		return True
	if n % x == 0:
		return check_multiple(n, x-1)
	else:
		return False

#solution for 1-10
n = 2520
while not check_multiple(n, 20):
	n += 2520

print(n)





from math import sqrt, ceil, floor
#x**2 - D * y**2 = 1
#x**2 = 1 + D * y**2

#for D <- 2 to 1000 (no perfect squares), find integer values for x,y s.t. x in minimized

#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
def determine_period(n):
	period = 0
	m = 0
	d = 1
	a_0 = int(sqrt(n))
	a = int(sqrt(n))
	arr = []
	arr.append(a)
	while a != 2*a_0:
		m = d*a - m
		d = (n-m**2)/d
		a = int((a_0 + m)/d)
		arr.append(a)
		period += 1
	if(period % 2 == 0):
		return arr[0:period]
	return arr[0:period] + arr[1:period]

squares = [n**2 for n in range(int(sqrt(1000))+1)]

def continued_fraction(arr):
	num = 1
	arr2 = arr[::-1]
	dem = arr2[0]
	for i in arr2[1:]:
		#add previous element to fraction
		num += dem*i
		#take reciprocal
		temp = num
		num = dem
		dem = temp
	return dem

max_x = 0
max_D = 0
for D in range(2, 1001):
	if(D not in squares):
		x = continued_fraction(determine_period(D))
		if(x > max_x):
			max_x = x
			max_D = D
print(max_D)


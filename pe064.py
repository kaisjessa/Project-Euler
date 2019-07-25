from math import sqrt
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
def determine_period(n):
	period = 0
	m = 0
	d = 1
	a_0 = int(sqrt(n))
	a = int(sqrt(n))
	while a != 2*a_0:
		m = d*a - m
		d = (n-m**2)/d
		a = int((a_0 + m)/d)
		period += 1
	return(period)

perfect_squares = [n**2 for n in range(1, 101)]

count = 0
for i in range(1+10**4):
	if(i not in perfect_squares and determine_period(i) % 2 != 0):
		count += 1
print(count)

import math
# n^2 + an + b
# |a| < 1000
# |b| <= 1000


'''
(n**2 + an + b) must be prime
when n==0:
b must be prime

when n==1:
(1+a+b) is prime
a+b is even
a%2 == b%2

when n==2:
(4 + 2a + b) is prime
(no information)
'''

nmax = 0
amax = 0
bmax = 0


def is_prime(x):
	if(x<2):
		return False
	if(x==2):
		return True
	for i in range(3, int(math.sqrt(x)) + 1, 2):
		if x % i == 0:
			return False
	return True


for a in range(-1000, 1000, 1):
	for b in range(-1000, 1000, 1):
		n = 0
		if(is_prime(b) and a%2==b%2 and (a+b)>0):
			while(is_prime(n**2 + a*n + b)):
				n += 1
			if(n - 1 > nmax):
				nmax = n - 1
				amax = a
				bmax = b

print(amax*bmax)
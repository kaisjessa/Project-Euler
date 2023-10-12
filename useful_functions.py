import math

"""
Sieve of Eratosthenes

n: upper bound for largest prime
"""
def sieve(n):
    is_prime = [True for i in range(0, n+1)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []

    while(True in is_prime):
        p = is_prime.index(True)
        primes.append(p)
        for i in range(p, len(is_prime), p):
            is_prime[i] = False
    return(primes)

"""
Returns True if x is prime, false otherwise
prime_list: optional argument containing list of known primes
"""
def is_prime(x, prime_list=[]):
	if(x==2 or x in prime_list):
		return True
	if(x<2 or x%2==0):
		return False
	for i in range(3, math.ceil(math.sqrt(x))+1, 2):
		if x % i == 0:
			return False
	return True

"""
given prime p, determine the next prime
"""
def next_prime(p0):
	i = p0+1
	while(True):
		if(is_prime(i)):
			return(i)
		i += 1
		
"""
given prime p, determine the previous prime
"""
def prev_prime(p1):
	i = p1-1
	while(i > 2):
		if(is_prime(i)):
			return(i)
		i -= 1
	return(2)

def prime_factors(n):
	l = []
	m = 2
	while(m <= n):
		while(n % m == 0):
			l.append(m)
			n /= m
		m = next_prime(m)
	return(l)
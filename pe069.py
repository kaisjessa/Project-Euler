import math

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


if(__name__ == "__main__"):
    primes = sieve(10**3)
    n = 1
    i = 0
    while(n*primes[i] <= 10**6):
        n *= primes[i]
        i += 1
    print(n)
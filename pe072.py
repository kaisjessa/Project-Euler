from useful_functions import *

n = 10**6
primes = sieve(n+1)

def factors(n):
    l = [[] for i in range(n+1)]
    for p in primes:
        for i in range(p, n+1, p):
            l[i].append(p)
    return(l)

facts = factors(n)

def unique_prime_factors(n):
    l = []
    i = 0
    while(n>1):
        if(n % primes[i] == 0):
            l.append(primes[i])
            while(n % primes[i] == 0):
                n /= primes[i]
        i += 1
    return(l)

def phi(n):
    if(n <= 1):
        return 1
    r = n
    for p in facts[n]:
        r *= (1 - 1/p)
    return(r)

if __name__ == "__main__":
    print(len(facts))
    total = 0
    for d in range(2, n+1):
        total += phi(d)
    print(int(total))
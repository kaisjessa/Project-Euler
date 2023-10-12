import math
from useful_functions import *

def phi(n):
    if(n <= 1):
        return 1
    if(is_prime(n)):
        return(n-1)
    r = n
    for p in set(prime_factors(n)):
        r *= (1 - 1/p)
    return(int(r))

def is_perm(n,m):
    return(sorted(list(str(n))) == sorted(list(str(m))))

if __name__ == "__main__":
    # best_n = 0
    # min_ratio = 2.0
    # for i in range(10**7, 87000, -1):
    #     p = phi(i)
    #     if(i/p <= min_ratio):
    #         if(sorted(list(str(i))) == sorted(list(str(p)))):
    #             min_ratio = i/p
    #             best_n = i
    #             print(best_n, p, min_ratio)
    # print(best_n)

    n = 0
    min_ratio = 2.0
    primes = sieve(int(10**4))
    for p1 in primes:
        for p2 in primes:
            if(p1*p2 < 10**7 and is_perm(p1*p2, (p1-1)*(p2-1)) and (p1*p2)/((p1-1)*(p2-1)) < min_ratio):
                min_ratio = (p1*p2)/((p1-1)*(p2-1))
                n = p1*p2
    print(n)
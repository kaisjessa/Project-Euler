import math
from useful_functions import sieve, prime_factors

primes = sieve(1_000_000)

def is_perfect_cube(n):
    cube_root = round(n**(1.0/3.0))
    return cube_root**3 == n

if __name__ == "__main__":
    count = 0
    for n in range(1, 600):
        diff = (n+1)**3 - n**3
        if(diff in primes):
            count += 1
    print(count)
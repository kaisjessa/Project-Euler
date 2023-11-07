import math
from useful_functions import *

n = 50 * 10**6
p = 2
primes1 = []
primes2 = []
primes3 = []
while(p <= math.sqrt(n - 2**3 - 2**4)+1):
    primes1.append(p)
    if(p <= math.cbrt(n - 2**2 - 2**4)+1):
        primes2.append(p)
        if(p <= math.sqrt(math.sqrt(n - 2**2 - 2**3))+1):
            primes3.append(p)
    p = next_prime(p)
# print(primes1, primes2, primes3)
nums = []
count = 0

if __name__ == "__main__":
    for p1 in primes1:
        for p2 in primes2:
            for p3 in primes3:
                t = p1**2 + p2**3 + p3**4
                if(t <= n):
                    count += 1
                    nums.append(t)

print(len(list(set(nums))))
import math
from useful_functions import is_prime

def proper_divisors(n):
    a = [1]
    for i in range(2, math.ceil(math.sqrt(n)), 1):
        if(n % i == 0):
            a += [i, n // i]
    return(a)

def next(n):
    return sum(proper_divisors(n))

def cycle(n):
    l = [n]
    i = next(n)
    while(i > n and i <= 10**6 and i not in l):
        # print(i)
        l.append(i)
        i = next(i)
    if(i != n):
        return []
    return l

if __name__ == "__main__":
    longest_chain = [1]
    for i in range(2, 10**6+1, 1):
        current = cycle(i)
        if(len(current) > len(longest_chain)):
            longest_chain = current
    print(min(longest_chain))
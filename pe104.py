import sys
import math

def power(x, n):
    t = 1
    for i in range(n):
        t *= x
        if(t >= 10**25):
            t //= 10**9
    return(t)

def pandigital(n):
    if(n < 10**8): return False
    s = str(n)[:9]
    return sorted(s) == list("123456789")

def solve():
    # only care about first 10 digits and last 10 digits
    # last 10 digits: compute fib numbers % 10**9
    # if those are pandigital, get first 10 digits
    # using approximation that fn1 = phi^i / sqrt5
    # https://en.wikipedia.org/wiki/Fibonacci_sequence#Computation_by_rounding
    phi = (1 + math.sqrt(5))/2
    i = 2
    # # last 9 digits
    l1, l2 = 1, 1
    while(True):
        l1, l2 = l2, (l1+l2)%10**9
        i += 1
        if(pandigital(l2)):
            f = round(power(phi, i) / math.sqrt(5))
            if(pandigital(f)):
                return(i)

if __name__ == "__main__":
    print(solve())
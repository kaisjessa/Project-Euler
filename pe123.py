from useful_functions import *
def rem(a, n):
    return ((a - 1) ** n + (a + 1) ** n) % a**2

def solve(upper):
    largest = 0
    f = 2
    # how many primes to generate
    while(largest < upper):
        primes = sieve(f)
        n = len(primes)-1
        largest = rem(primes[n], n)
        f *= 2
    # solution upper bounded by f
    left = 1
    right = n-1
    while(left < right):
        mid = (left + right)//2
        # n (of p_n) will be odd
        if(mid % 2 == 0):
            mid += 1
        if(rem(primes[mid], mid) >= upper and rem(primes[mid-2], mid-2) < upper):
            return mid
        elif(rem(primes[mid], mid) < upper):
            left = mid + 2
        else:
            right = mid - 2
    return(mid)

if __name__ == "__main__":
    n = 10**10
    print(solve(n))
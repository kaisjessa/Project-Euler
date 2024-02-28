from useful_functions import *
import itertools

# generate list of first 15 primes
primes = [2]
while(len(primes) < 15-1):
    primes.append(next_prime(primes[-1]))

# consider n whose only prime factors are exactly first k primes
# determine the lowest such n for which n**2 has > 8*10**6 factors
def loop_primes(k, upper):
    best = float('inf')
    for c in itertools.combinations_with_replacement(list(range(1, 10)), k):
        c = list(c)[::-1]
        total = 1
        for i in range(k):
            total *= (2*c[i]+1)
        # if n**2 has more than upper factors, determine n
        if(total > upper):
            n = 1
            for i in range(k):
                n *= primes[i]**c[i]
            best = min(best, n)
    return(best)

if __name__ == "__main__":
    best = float('inf')
    current_best = float('inf')
    i = 0
    # keep trying primes until n starts increasing by introducing more primes
    while(best >= current_best):
        best = current_best
        current_best = loop_primes(i, 8*10**6)
        i += 1
    print(best)
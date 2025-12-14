from useful_functions import sieve, unique_prime_factors
primes = sieve(100000)

def A(n):
    rem = 1
    for k in range(2,n+1):
        rem = (10*rem + 1) % n
        if(rem == 0):
            return k
    return None

if __name__ == "__main__":
    arr = []
    for p in primes:
        print(p)
        if(p <= 5):
            continue
        facts = unique_prime_factors(A(p))
        if(facts == [2] or facts==[5] or facts==[2,5]):
            arr.append(p)
    print(sum(primes) - sum(arr))
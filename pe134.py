from useful_functions import sieve
def lowest_sol(p1, p2):
    unit = 10**(len(str(p1)))
    num = p1
    count = 0
    while(num % p2 > 0):
        num += unit
        count += 1
    return(num)

def lowest_sol2(p1, p2):
    a = 10**(len(str(p1)))
    b = p2 - p1
    m = p2
    x = (pow(a, m-2, m) * b) % m
    return (a*x + p1)

if __name__ == "__main__":
    primes = sieve(1_001_000)
    total = 0

    for i in range(2, len(primes)-1):
        p1 = primes[i]
        p2 = primes[i+1]
        if(p1 > 1_000_000):
            break
        total += lowest_sol2(p1, p2)
    print(total)
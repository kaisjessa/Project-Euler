from useful_functions import miller_rabin, sieve


def prob_next_prime(p0):
    if p0 == 2:
        return 3
    i = p0 + 2
    while True:
        if miller_rabin(i):
            return i
        i += 2


def is_valid(n, primes):
    adds = (1, 3, 7, 9, 13, 27)

    b = n**2
    # make sure not divisible by small prime (fastest)
    for p in primes:
        for k in adds:
            if (b + k) % p == 0 and (b + k) != p:
                return False
    # make sure all are primes (using fast check)
    for k in adds:
        if not miller_rabin(b + k):
            return False
    # make sure such primes are consecutive (slow-check)
    p = b + 1
    for k in adds[1:]:
        if not prob_next_prime(p) == b + k:
            return False
        p = b + k
    return True


if __name__ == "__main__":
    upper = 150 * 10**6
    primes = sieve(10**3)
    total = 0
    divs = (3, 7, 13)
    candidates = filter(lambda n: (n % k > 0 for k in divs), range(10, upper, 10))
    for n in candidates:
        if is_valid(n, primes):
            total += n
    print(total)

import math
import random

"""
Sieve of Eratosthenes

n: upper bound for largest prime
"""


def sieve(n):
    is_prime = [True for i in range(0, n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    primes = [2]

    for i in range(3, n, 2):
        if is_prime[i]:
            p = i
            primes.append(p)
            for j in range(i**2, n + 1, i):
                is_prime[j] = False
    return primes


"""
Returns True if x is prime, false otherwise
prime_list: optional argument containing list of known primes
"""


def is_prime(x, prime_list=[]):
    if x < 4:
        return x > 1
    if x in prime_list:
        return True
    if len(prime_list) > 0 and x < prime_list[-1] and x not in prime_list:
        return False
    if x % 2 == 0 or x % 3 == 0:
        return False
    upper = math.isqrt(x) + 1
    # check 6k +- 1
    k = 1
    while 6 * k - 1 <= upper:
        if x % (6 * k - 1) == 0 or x % (6 * k + 1) == 0:
            return False
        k += 1
    return True


"""
given prime p0, determine the next prime
"""


def next_prime(p0):
    i = p0 + 1
    while True:
        if is_prime(i):
            return i
        i += 1


"""
given prime p, determine the previous prime
"""


def prev_prime(p1):
    i = p1 - 1
    while i > 2:
        if is_prime(i):
            return i
        i -= 1
    return 2


"""
given integer n, returns list of prime factors of n
"""


def prime_factors(n):
    l = []
    m = 2
    while m <= n:
        while n % m == 0:
            l.append(m)
            n //= m
        m = next_prime(m)
    return l


def unique_prime_factors(n):
    l = []
    m = 2
    while m <= n:
        if n % m == 0:
            l.append(m)
            while n % m == 0:
                n //= m
        m = next_prime(m)
    return l


"""
given integer n, returns phi(n) = euler totient function, number of integers 1 <= i < n where gcd(i,n) = 1
"""


def phi(n):
    if n <= 1:
        return 1
    if is_prime(n):
        return n - 1
    r = n
    for p in unique_prime_factors(n):
        r *= 1 - 1 / p
    return int(r)


"""
greatst common divisor of a and b
"""


def gcd(a, b):
    # while(b != 0):
    #     t = b
    #     b = a % b
    #     a = t
    # return(a)
    return math.gcd(a, b)


"""
Returns True if n is a perfect square, False otherwise
"""


def is_perfect_square(n):
    sqrtn = math.isqrt(n)
    return sqrtn * sqrtn == n


"""
Returns list of Fibonacci numbers up to num
"""


def fibonacci_numbers(num):
    fibs = [1, 1]
    for i in range(2, num + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs


"""
Returns True if n is *probably* prime, False otherwise
probabilistic primality test
much faster than deterministic
only use deterministic after passing this test
"""


def miller_rabin(n, k=3):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True

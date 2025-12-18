from useful_functions import unique_prime_factors
from math import isqrt


def is_progressive(n):
    for d in range(1, n):
        q = n // d
        r = n % d
        (a, b, c) = sorted([d, q, r])
        if a * b * c == 0:
            continue
        if b / a == c / b:
            print(b / a)
            return True
    return False


if __name__ == "__main__":
    total = 0
    upper = 1_000_000
    for n in range(isqrt(upper)):
        if is_progressive(n**2):
            total += n**2
            print(n, unique_prime_factors(n))
    print(total)

from useful_functions import is_perfect_square
from math import isqrt, gcd


# def is_progressive(n):
#     for d in range(1, n):
#         q = n // d
#         r = n % d
#         (a, b, c) = sorted([d, q, r])
#         if a * b * c == 0:
#             continue
#         if b / a == c / b:
#             print(b / a, d, q, r)
#             return True
#     return False


def get_n(a, b, l):
    return a**3 * b * l**2 + b**2 * l


if __name__ == "__main__":
    total = 0
    upper = 10**12
    limit = int(upper ** (1 / 3))
    for a in range(limit):
        for b in range(1, a):
            if gcd(a, b) > 1:
                continue
            l = 1
            n = get_n(a, b, l)
            while n < upper:
                if is_perfect_square(n):
                    total += n
                l += 1
                n = get_n(a, b, l)
    print(total)

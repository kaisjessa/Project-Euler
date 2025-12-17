from math import isqrt
from useful_functions import is_perfect_square, prime_factors


def f(k):
    return 5 * k**2 + 4 * k + 1


def g(k):
    return 5 * k**2 - 4 * k + 1


if __name__ == "__main__":
    # k = b / 2
    # for k in range(0, 100_000_000_000, 8):
    #     fk = f(k)
    #     gk = g(k)
    #     if is_perfect_square(fk):
    #         print(k, isqrt(fk), prime_factors(isqrt(fk)), prime_factors(isqrt(fk) - 1))
    #     if is_perfect_square(gk):
    #         print(k, isqrt(gk), prime_factors(isqrt(gk)), prime_factors(isqrt(gk) - 1))

    sols = [17, 305, 5473, 98209, 1762289, 31622993]
    for i in range(1, len(sols)):
        print(sols[i], sols[i - 1], (sols[i]) % (sols[i - 1]))

    As = [17, 305]
    for n in range(2, 12):
        As.append(18 * As[n - 1] - As[n - 2])
    print(sum(As))

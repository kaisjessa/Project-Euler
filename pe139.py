from math import gcd, isqrt


def can_tile(a, b, c):
    return c % (b - a) == 0


def get_triple(m, n):
    return (m**2 - n**2, 2 * m * n, m**2 + n**2)


if __name__ == "__main__":
    total = 0
    limit = 100_000_000
    upper = isqrt(limit // 2)
    for m in range(1, upper):
        for n in range(1 + m % 2, m, 2):
            (a, b, c) = get_triple(m, n)
            perimeter = a + b + c
            if perimeter > limit:
                break
            if gcd(n, m) != 1:
                continue
            if b > a:
                a, b = b, a
            if can_tile(a, b, c):
                total += limit // perimeter
    print(total)

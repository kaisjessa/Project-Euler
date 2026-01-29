import time

# def last_digits(n):
#     current = 1
#     for i in range(2, n + 1):
#         if i % 10 != 0:
#             current *= i % 10
#         while current % 10 == 0:
#             current //= 10
#         print(i, current)


def legendre(n, p):
    total = 0
    i = 1
    current = n // p**i
    while current > 0:
        total += current
        i += 1
        current = n // p**i
    return total


def calc_a(n):
    m_5 = legendre(n, 5)
    m_2 = legendre(n, 2)
    k = m_2 - m_5
    a = pow(2, k, 10**5)
    return a


def get_prods(n):
    prods = {}
    prods[0] = 1
    current = 1
    for i in range(1, min(n, 10**5) + 1, 1):
        if i % 2 != 0 and i % 5 != 0:
            current *= i
        prods[i] = current % 10**5
    return prods


def calc_b(n):
    prods = get_prods(n)
    b = 1
    j = 0
    while n // 5**j > 2:
        i = 0
        while n // (2**i * 5**j) > 2:
            m = n // (2**i * 5**j)
            b *= prods[m % 10**5]
            b %= 10**5
            i += 1
        j += 1
    return b


def solve(n):
    a = calc_a(n)
    b = calc_b(n)
    return (a * b) % 10**5


if __name__ == "__main__":
    start = time.time()
    u = 10**12
    print(solve(u))
    print(f"Finished in {round(time.time()-start,2)}s")

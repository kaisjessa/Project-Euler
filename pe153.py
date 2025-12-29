from math import isqrt, gcd


def real_divisor_sum(n):
    # total = 0
    # for a in range(1, upper + 1):
    #     total += a * (upper // a)
    #     # print(a, (upper // a))
    # return total
    # OEIS
    s = sum(n - (n % m) for m in range(1, n + 1))
    return s


# def complex_divisor_sum(upper):
#     total = 0
#     for a in range(1, upper // 2 + 1):
#         # print(a)
#         l = range(1, a + 1)
#         l = filter(lambda b: (a**2 + b**2) // gcd(a, b) <= upper, l)
#         for b in l:
#             # smallest integer divisible by a+bi
#             # is (a**2 + b**2) / gcd(a,b)
#             # when b = 0, gcd(a,b)=a
#             n = (a**2 + b**2) // gcd(a, b)
#             if n > upper:
#                 # print(a, b)
#                 break
#             total += a * (upper // n)
#             if b > 0:
#                 total += a * (upper // n)
#             if a > b:
#                 total += 2 * b * (upper // n)
#     return total + real_divisor_sum(upper)


def add_pair(a, b, upper):
    total = 0
    root = a**2 + b**2
    if root > upper:
        return total
    k = 1
    n = root
    while n <= upper:
        n = k * root
        total += 2 * k * a * (upper // n)
        # if a > 0:
        #     total += k * a * (upper // n)
        if b < a:
            total += 2 * k * b * (upper // n)
        k += 1
    return total


def coprime_divisor_sum(upper):
    total = 0
    s = isqrt(upper)
    for a in range(1, s + 1):
        for b in range(1, max(2, a)):
            if a**2 + b**2 > upper:
                break
            if gcd(a, b) == 1:
                total += add_pair(a, b, upper)
                pass
    return total


if __name__ == "__main__":
    upper = 10**8
    # a = real_divisor_sum(upper)
    a = 8224670422194237  # real_divisor_sum(upper)
    b = coprime_divisor_sum(upper)
    print(a + b)

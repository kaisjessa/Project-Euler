from math import sqrt
from useful_functions import is_perfect_square, prime_factors, fibonacci_numbers

# phi = (1 + sqrt(5)) / 2
# psi = (1 - sqrt(5)) / 2
# a = 3 / 2 - 1 / (2 * sqrt(5))
# # b = (1 / 10) * (15 + sqrt(5))
# b = 3 - a


# def Gs(num):
#     gs = [1, 4]
#     for i in range(2, num):
#         gs.append(gs[i - 1] + gs[i - 2])
#     return gs


# def G(n):
#     return round(a * pow(phi, n) + b * pow(psi, n))


# def series(x):
#     # return round(a * (1 / (1 - phi * x) - 1) + b * (1 / (1 - psi * x) - 1), 5)
#     return (3 * x**2 + x) / (1 - x - x**2)


# def fibonacci_factors(n):
#     facts = []
#     for f in fibonacci_numbers(n):
#         if f > 1 and n % f == 0:
#             facts.append(f)
#     return facts


def rec(starts):
    pairs = []
    for pair in starts:
        x0, y0 = pair
        x = -9 * x0 - 4 * y0 - 14
        y = -20 * x0 - 9 * y0 - 28
        x0 = x
        y0 = y
        pairs.append((x, y))
    return pairs


if __name__ == "__main__":
    sols = [2]
    pairs = [(2, -7), (0, -1), (0, 1), (-4, 5), (-3, 2), (-3, -2)]
    while len(sols) < 30:
        pairs = rec(pairs)
        for pair in pairs:
            x, y = pair
            if x > 0 and x not in sols:
                sols.append(x)
    print(sum(sols[:30]))

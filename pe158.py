# from itertools import permutations, combinations
from string import ascii_lowercase
from math import comb


def count_sols(n):
    # 1. choose n letters for the string -> (26 choose n)
    # 2. choose index for the break, 0 <= k <= n-2
    # 3. (n choose k) letters for first half s1, (n-k choose n-k)=1 letters for second half s2
    # 4. s1 and s2 are each in reverse alphabetical order, 1 option of ordering
    count = 0
    choice = comb(26, n)
    for k in range(0, n - 1):
        count += choice * comb(n, k)
    return count


# def solve(u):
#     f0 = [1 for _ in range(26)]
#     f1 = [0 for _ in range(26)]
#     for n in range(2, u + 1):
#         g0 = [0 for _ in range(26)]
#         g1 = [0 for _ in range(26)]
#         # for each pair of letters x and y
#         # if x < y then f1[x] += f0[y]
#         # if x >= y then f1[x] += f1[y], f0[x] += g0[y]
#         for x in range(26):
#             for y in range(26):
#                 if x < y:
#                     g1[x] += f0[y] - (n - 2)
#                 elif x > y:
#                     g1[x] += f1[y] - (n - 2)
#                     g0[x] += f0[y]
#         f0 = g0
#         f1 = g1
#     return sum(f1)


# def brute_force(u):
#     s0 = list(ascii_lowercase)
#     s1 = []
#     for n in range(2, u + 1):
#         g0 = []
#         g1 = []
#         for x in ascii_lowercase:
#             for s in s0:
#                 if x in s:
#                     continue
#                 y = s[0]
#                 a = ascii_lowercase.index(x)
#                 b = ascii_lowercase.index(y)
#                 if a < b:
#                     g1.append(x + s)
#                 elif a > b:
#                     g0.append(x + s)
#             for s in s1:
#                 if x in s:
#                     continue
#                 y = s[0]
#                 a = ascii_lowercase.index(x)
#                 b = ascii_lowercase.index(y)
#                 if x > y:
#                     g1.append(x + s)
#         s0 = g0
#         s1 = g1
#     return len(s1)


if __name__ == "__main__":
    u = 26
    best = 0
    for n in range(1, u + 1):
        best = max(best, count_sols(n))
    print(best)
    # print(brute_force(u))

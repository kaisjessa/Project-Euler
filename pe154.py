from math import factorial, comb
import sys

# def choose(n, i, j, k):
#     if i + j + k != n:
#         raise ValueError("Must have i+j+k=n")
#     return factorial(n) // (factorial(i) * factorial(j) * factorial(k))


def two_five(n):
    a = 0
    b = 0
    while n > 0 and n % 2 == 0:
        a += 1
        n //= 2
    while n > 0 and n % 5 == 0:
        b += 1
        n //= 5
    return (a, b)


# (x+y+z)^n = Sum_{i+j+k=n} n!/(i!j!k!) x^i y^j z^k
if __name__ == "__main__":
    n = 200_000
    count = 0
    goal = (12, 12)  # 2^a * 5^b

    # d[m] = (a,b) => m = 2**a * 5**b * k
    # where gcd(2,k) == gcd(5,k) == 0
    d = {}
    for i in range(0, n + 1):
        d[i] = two_five(i)
    # df[m] = (a,b) => m! = 2**a * 5**b * k
    # where gcd(2,k) == gcd(5,k) == 0
    df = {}
    df[0] = (0, 0)
    for i in range(1, n + 1):
        t = df[i - 1][0] + d[i][0]
        f = df[i - 1][1] + d[i][1]
        df[i] = (t, f)

    # Compute C(i,j,k) = n! / i!j!k!
    # WLOG use i <= j <= k
    # where k = n - i - j
    for i in range(0, n // 3 + 1, 1):
        for j in range(i, n // 2 + 1, 1):
            k = n - i - j
            if j < i or k < j or k < i:
                break
            twos = df[n][0] - df[i][0] - df[j][0] - df[k][0]
            fives = df[n][1] - df[i][1] - df[j][1] - df[k][1]
            if twos >= goal[0] and fives >= goal[1]:
                # print(i, j, k)
                # consider permutations of i,j,k
                # if i==j==k, 1 permutation
                # if i==j or i==k or j==k, 3 permutations
                # else 6 permutations
                if i == j and j == k:
                    count += 1
                elif i == j or j == k or i == k:
                    count += 3
                else:
                    count += 6
    print(count)

    # # compute C(n,i,j) = C(n,i) * C(i,j)
    # count = 0
    # for i in range(1, n + 1, 1):
    #     # if i % 10 not in [1, 2, 3, 6, 7, 8]:
    #     #     continue
    #     t1 = df[n][0] - df[i][0] - df[n - i][0]
    #     f1 = df[n][1] - df[i][1] - df[n - i][1]
    #     for j in range(0, i // 2 + 1):
    #         t2 = df[i][0] - df[j][0] - df[i - j][0]
    #         f2 = df[i][1] - df[j][1] - df[i - j][1]
    #         if t1 + t2 >= goal[0] and f1 + f2 >= goal[1]:
    #             count += 2
    #             if j == i // 2:
    #                 count -= 1
    #     # print(i, count)
    # print(count)

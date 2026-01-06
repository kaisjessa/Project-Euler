from math import isqrt
import time


def count_divisors(n):
    count = 0
    for i in range(1, isqrt(n) + 1):
        if n % i > 0:
            continue
        count += 2
        if i * i == n:
            count -= 1
    return count


def solve(u):
    count = 0
    for n in range(1, u + 1):
        upper = 10**n
        for s in range(0, u + 1):
            for t in range(0, u + 1):
                b = 2**s * 5**t
                if (upper * (1 + b)) % b == 0:
                    p = (upper * (1 + b)) // b
                    # print(f"1/{1} + 1/{b} = {p}/{upper}")
                    count += count_divisors(p)
        for s in range(1, u + 1):
            a = 2**s
            for t in range(1, u + 1):
                b = 5**t
                if ((upper * a + upper * b) % (a * b)) == 0:
                    p = (upper * a + upper * b) // (a * b)
                    # print(f"1/{a} + 1/{b} = {p}/{upper}")
                    count += count_divisors(p)
    return count


# def brute_force(u):
#     count = 0
#     for n in range(1, u + 1):
#         for p in range(1, 2 * 10**n + 1):
#             for a in range((2 * 10**n // p), (10**n // p), -1):
#                 if (10**n * a) % (p * a - 10**n) == 0:
#                     b = (10**n * a) // (p * a - 10**n)
#                     count += 1
#     return count


if __name__ == "__main__":
    start = time.time()
    u = 9
    print(solve(u))
    print(f"Finished in {round(time.time()-start,2)}s")

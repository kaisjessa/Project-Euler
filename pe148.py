from math import comb, log
from useful_functions import prime_factors


# def count_sevens(n, k):
#     return n // 7 > k // 7 + (n - k) // 7


# def choose_count(n, k):
#     return comb(n, k) % 7 > 0


# def count_array(lower, upper):
#     d = {}
#     for n in range(lower, upper):
#         d[n] = 0
#         for k in range(0, n + 1):
#             d[n] += choose_count(n, k)
#     return d


def recursive_list(n):
    if n == 0:
        return [1]
    prev_list = [1]
    for l in range(n):
        new_list = []
        for i in range(1, 8):
            new_list += [e * i for e in prev_list]
        prev_list = new_list
    return prev_list


if __name__ == "__main__":
    upper = 10**9
    max_power = int(log(upper // 10, 7)) + 1
    arr = recursive_list(max_power)
    i = upper // 7**max_power
    j = upper % 7**max_power
    total = sum(arr)
    total = i * (i + 1) * total // 2
    total += (i + 1) * (sum(arr[:j]))
    print(total)

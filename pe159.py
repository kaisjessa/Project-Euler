import time
from math import isqrt

# from useful_functions import prime_factors, unique_prime_factors, sieve


def digital_root(n):
    if n == 0:
        return 0
    return 1 + ((n - 1) % 9)


# primes = sieve(1_000_000)
# roots = {}
# for p in primes:
#     roots[p] = digital_root(p)


# def DRS(n):
#     total = 0
#     for i in range(9, 1, -1):
#         while n % i == 0:
#             total += i
#             n //= i
#     if n == 1:
#         return total
#     if n in primes:
#         total += roots[n]
#         return total
#     for p in prime_factors(n):
#         total += roots[p]
#     return total


# def all_factorizations(n):
#     facts = set()
#     facts.add((n,))
#     if n == 1:
#         return set()
#     if n in primes:
#         return facts
#     for p in unique_prime_factors(n):
#         m = n // p
#         sub_facts = all_factorizations(m)
#         facts.update(set(tuple(sorted((p,) + fact)) for fact in sub_facts))
#     return facts


# def brute_force(n):
#     best = 0
#     for fact in all_factorizations(n):
#         temp = sum([digital_root(m) for m in fact])
#         best = max(best, temp)
#     return best


def solve():
    mdrs = {}
    for n in range(2, 1_000_000):
        mdrs[n] = digital_root(n)
    for i in range(2, 1_000_000, 1):
        for j in range(2, isqrt(i) + 1, 1):
            if i % j:
                continue
            mdrs[i] = max(mdrs[i], mdrs[j] + mdrs[i // j])
    return mdrs


if __name__ == "__main__":
    start = time.time()
    mdrs = solve()
    print(sum(mdrs.values()))
    print(f"Finished in {round(time.time()-start,2)}s")

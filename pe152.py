from fractions import Fraction
from useful_functions import unique_prime_factors


# def sum_product(S):
#     total = 0
#     for i in range(len(S)):
#         t = 1
#         for j in range(len(S)):
#             if j != i:
#                 t *= S[j] ** 2
#                 print(S[j])
#         total += t
#     return total


# def reciprocal_square_sum(S):
#     total = 0
#     for n in S:
#         total += Fraction(1, n**2)
#     return total


def stored_sums(S):
    bound = Fraction(1, 2)
    R = {}
    count = 0
    # if k (partial sum) + rep (1/s**2) + remaining_sum < bound
    # then even if we added all remaining 1/n**2 to R[k+rep]
    # it would not reach bound
    # so don't bother storing
    remaining_sum = sum(Fraction(1, s**2) for s in S)
    for i in range(len(S)):
        s = S[i]
        rep = Fraction(1, s**2)
        remaining_sum -= rep
        # if len(R.keys()) > 0:
        #     print(
        #         s,
        #         len(R.keys()),
        #         # float(min(R.keys())),
        #         # float(max(R.keys())),
        #         # float(remaining_sum),
        #         # float(remaining_sum + min(R.keys())),
        #     )
        R2 = R.copy()
        R2[rep] = R.get(rep, 0) + 1
        for k in filter(lambda k: k + rep == bound, R.keys()):
            count += R2.get(k + rep, 0) + R[k]
            # print(s, count)

        for k in filter(
            lambda k: k + rep < bound and k + rep + remaining_sum >= bound, R.keys()
        ):
            # if k + remaining_sum >= bound:
            #     R2[k] = R2.get(k, 0) + R[k]
            R2[k + rep] = R2.get(k + rep, 0) + R[k]
        R = R2
    return count


# def count_halves(upper):
#     bound = Fraction(1 / 2**2) + Fraction(1 / 3**2) + Fraction(1 / 4**2)
#     S = [Fraction(1, n**2) for n in range(5, upper + 1)]
#     combs = []
#     for r in range(1, len(S)):
#         combs += [sum(s) for s in combinations(S, r) if sum(s) <= bound]
#     return combs


if __name__ == "__main__":
    upper = 78
    S = list(range(2, upper + 1))
    # playing around with eliminating values related to prime multiples
    S = [n for n in S if max(unique_prime_factors(n)) in [2, 3, 5, 7, 13]]
    S = [n for n in S if not n >= 16 or not any(n % p == 0 for p in [16, 25, 49])]
    # print(S)
    # print(len(S))
    t = stored_sums(S)
    print(t)

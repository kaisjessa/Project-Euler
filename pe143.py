from math import isqrt


# parameterization formula derived from proof of Euler's formula
# for generating Pythagorian triples
def get_triple(m, n):
    return (n**2 + 2 * n * m, m**2 - n**2, n**2 + n * m + m**2)


def get_pairs(upper):
    pairs = {}
    limit = isqrt(upper) + 1
    for m in range(1, limit):
        for n in range(1, m + 1):
            a, b, _ = get_triple(m, n)
            if b > a:
                a, b = b, a
            if a + b > upper:
                break
            k = 1
            while k * a + k * b <= upper:
                pairs[k * a] = pairs.get(k * a, set())
                pairs[k * a].add(k * b)
                k += 1
    return pairs


def solve():
    upper = 120_000
    sums = set()
    pairs = get_pairs(upper)
    for p in pairs.keys():
        for q in pairs[p]:
            # find r such that (p,r) and (q,r) in pairs
            for r in pairs.get(q, set()):
                if r == 0:
                    continue
                if p + q + r > upper:
                    continue
                if r not in pairs[p]:
                    continue
                # if r not in pairs[q]:
                #     continue
                # print(p, q, r, (p + q + r))
                sums.add(p + q + r)
    return sums


if __name__ == "__main__":
    sums = solve()
    print(sum(sums))

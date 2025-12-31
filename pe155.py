from fractions import Fraction


def parallel(a, b):
    return a + b


def series(a, b):
    return Fraction(1, Fraction(1, a) + Fraction(1, b))


if __name__ == "__main__":
    b = 1
    u = 18
    S = {}
    S[1] = set()
    S[1].add(b)
    combined_set = set()
    combined_set.add(b)
    for n in range(2, u + 1):
        S[n] = set()
        for i in range(1, n // 2 + 1):
            j = n - i
            if i > j:
                continue
            for f1 in S[i]:
                for f2 in S[j]:
                    p = parallel(f1, f2)
                    s = series(f1, f2)
                    S[n].add(p)
                    S[n].add(s)
                    combined_set.add(p)
                    combined_set.add(s)
    print(len(combined_set))

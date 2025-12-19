from useful_functions import is_perfect_square


def square_list(upper):
    return [n**2 for n in range(upper)]


# def min_shared_key(A, B):
#     for k in A.keys():
#         if k in B.keys() and len(A[k]) > 1 and len(B[k]) > 1:
#             return k
#     return None


def get_pair_dicts(upper):
    A = {}
    B = {}
    sq = square_list(upper)
    for i in range(1, len(sq)):
        for j in range(i + 1, len(sq)):
            n = sq[j]
            m = sq[i]
            if (n + m) % 2 == 0:
                A[(n + m) // 2] = A.get((n + m) // 2, [])
                A[(n + m) // 2].append((n, m))
                B[(n - m) // 2] = B.get((n - m) // 2, [])
                B[(n - m) // 2].append((n, m))
    return (A, B)


def solve(upper):
    # A: (n**2 + m**2)/2
    # B: (n**2 - m**2)/2
    A, B = get_pair_dicts(upper)
    for x in A.keys():
        # x is the midpoint between at least two pairs of squares
        if len(A[x]) > 1:
            for pair in A[x]:
                # x+y and x-y are squares
                y = (pair[0] - pair[1]) // 2
                if y in A.keys() and y in B.keys():
                    for pair2 in A[y]:
                        z = (pair2[0] - pair2[1]) // 2
                        # y+z and y-z are squares
                        # just need x+z and x-z
                        if is_perfect_square(x + z) and is_perfect_square(x - z):
                            return x + y + z
    return -1


if __name__ == "__main__":
    upper = 1
    sol = solve(upper)
    while sol < 0:
        upper *= 10
        sol = solve(upper)
    print(sol)

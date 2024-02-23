# https://en.wikipedia.org/wiki/Newton_polynomial
# N(x) = sum_(j=0 to k) a_j * n_j(x)
# n_0(x) = 1; n_j(x) = n_(j-1)(x) * (x - x_j)
# a_j = dd[y_0, ..., y_j]
def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def t(n):
    return n**3

def dd(points):
    arr = [p[1] for p in points]
    a = arr
    while(len(a) > 1):
        a = [a[i+1]-a[i] for i in range(len(a)-1)]
    return a[0]

def compute_poly(points, x):
    l = len(points)
    aks = []
    for i in range(1, l+1):
        a = dd(points[:i])
        for k2 in range(1, i):
            a //= k2
        aks.append(a)
    total = 0
    for i in range(l):
        term = aks[i]
        for j in range(0, i):
            term *= (x - points[j][0])
        total += term
    return total

def first_wrong_term(points):
    return compute_poly(points, len(points)+1)


if __name__ == "__main__":
    points = []
    for n in range(1, 11):
        points.append((n, u(n)))

    total = 0
    for k in range(1, 11):
        total += first_wrong_term(points[:k])

    print(total)
            
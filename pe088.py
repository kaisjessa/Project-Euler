import math
from useful_functions import *

def factors(n):
    l = []
    for m in range(2, int(math.sqrt(n))+1):
        if(n % m == 0):
            l.append(m)
    return(l + [n])

# n, current, sum, prod, depth
def get_all_k(n, c, s, p, d):
    all = []
    if(c == 1):
        k2 = n - s
        k = d + k2
        if(k > 1):
            return [k]
    else:
        for f in factors(c):
            # print(n, f)
            all += get_all_k(n, c // f, s+f, p*f, d+1)
    return(all)

def get_k(n):
    return get_all_k(n, n, 0, 1, 0)

if __name__ == "__main__":
    upper = 12000
    ks = [math.inf for i in range(2*upper)]
    for n in range(2, 2*upper+1):
        for k in get_k(n):
            ks[k] = min(ks[k], n)
    print(sum(list(set(ks[2:upper+1]))))
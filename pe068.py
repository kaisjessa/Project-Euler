# 14 <= sum of rows <= 18
# 10 must be outside digit
from itertools import permutations

def list_to_str(l):
    first_digit = str(min([a[0] for a in l]))
    flat = ''.join([str(i) for s in l for i in s])
    splitter = flat.index(first_digit)
    flat = flat[splitter:] + flat[:splitter]
    return(int(flat))

if(__name__ == "__main__"):
    a1 = 10
    (a0, a2, a3, a4, a5, a6, a7, a8, a9) = (0,0,0,0,0,0,0,0,0)
    max_found = 0
    for assn in permutations(list(range(1,10))):
        (a0, a2, a3, a4, a5, a6, a7, a8, a9) = assn
        perms = [[a1, a0, a2], [a3, a2, a4], [a5, a4, a6], [a7, a6, a8], [a9, a8, a0]]
        sums = [sum(a) for a in perms]
        if(14 <= a1 + a0 + a2 and a1 + a0 + a2 <= 18 and len(list(set(sums))) == 1):
            candidate = list_to_str(perms)
            max_found = max(max_found, candidate)

    print(max_found)


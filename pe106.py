import itertools

def power_set(arr):
    comb = []
    for i in range(0, len(arr)+1):
        comb += [list(x) for x in itertools.combinations(arr, i)]
    return(comb)

def get_required_subset_pairs(arr):
    pairs = []
    subs = power_set(arr)
    for i in range(len(subs)-1):
        for j in range(i+1, len(subs)):
            B = subs[i]
            C = subs[j]
            if(len(B)==len(C) # we know |B| > |C| => S(B) > S(C) already
               and len(B) > 1 # don't need empty set or |B| = 1 since we know there's no repeats
               and max(B) >= min(C) # we already know if max(B) < min(C) then S(B) < S(C)
               and False in [(B[i] < C[i]) for i in range(len(B))] # all bi < ci => S(B) = b0 + b1 + ... + bk < c0 + c1 + ... + ck = S(C)
               and True not in [(x in C) for x in B] # disjoint (also covers B = A)
               ):
                pairs.append((B, C))
    return(pairs)


if __name__ == "__main__":
    n = 12
    s = list(range(0,n))
    pairs = get_required_subset_pairs(s)
    print(len(pairs))
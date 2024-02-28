def get_darts():
    darts = {}
    for i in range(1, 21):
        darts[f"S{i}"] = i
        darts[f"D{i}"] = 2*i
        darts[f"T{i}"] = 3*i
    darts["S25"] = 25
    darts["D25"] = 50
    return(darts)

# assume partial is complete up to n-1
# for each partition of n into i + j = (n-1) + 1 = (n-2) + 2 = ... = 1 + (n-1)
# each pair of (s1, s2) in partial[i] x partial[j] sums to n
# keep the ones with less than 3 dart throws
def get_partial(n, partial):
    scores = []
    for i in range(1, n):
        j = n - i
        for s1 in partial[i]:
            for s2 in partial[j]:
                if(len(s1) + len(s2) < 3):
                    scores.append(s1 + s2)
    for d in darts.keys():
        if(darts[d] == n):
            scores.append([d])
    return(scores)

# assume partial is complete up to n-1
# for each partition of n = m + r = 0 + n = 1 + (n-1) + ...
# for each p in partial[m] (uses 2 or less darts), if we can achieve r with a double k, add p+[k] to final scores
def get_final(n, partial):
    scores = []
    for m in range(0, n):
        for p in partial[m]:
            r = n - m
            for k,v in darts.items():
                if(v == r and "D" in k and p + [k] not in scores and p[::-1]+[k] not in scores):
                    scores.append(p + [k])
    return(scores)

if __name__ == "__main__":
    darts = get_darts()
    # partial[n] = ways to get a score of n with 2 or less throws
    # final[n] = ways to get a score of n with 3 or less throws ending on a double
    partial = {}
    partial[0] = [[]]
    partial[1] = [["S1"]]
    final = {}
    count = 0
    for n in range(2, 100):
        partial[n] = get_partial(n, partial)
        final[n] = get_final(n, partial)
        count += len(final[n])
    print(count)
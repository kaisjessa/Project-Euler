
def count_non_bouncy(max_len):
    # keep track of the number of increasing/decreasing/equal number that start with each digit
    increasing = {}
    decreasing = {}
    equal = {}
    for i in range(0, 10):
        increasing[i] = 0
        decreasing[i] = 0
        equal[i] = 1

    count = 9 # len(equal) = 9
    for p in range(1, max_len):
        ni = {}
        nd = {}
        for i in range(0, 10):
            ni[i] = 0
            nd[i] = 0

        # count numbers of length p we can make using the previously determined p-1
        # add a digit before to make it still increasing/decreasing
        for a in range(1, 10):
            for d in range(1, a+1):
                ni[d] += increasing[a]
            for d in range(a, 10):
                nd[d] += decreasing[a]

        # count numbers of length p we can make using '0'*p, '1'*p, '2'*p, ..., '9'*p
        for a in range(0, 10):
            for d in range(1, a):
                ni[d] += equal[a]
            for d in range(a+1, 10):
                nd[d] += equal[a]
        
        count += sum([v for k,v in ni.items()]) + sum([v for k,v in nd.items()]) + 9 # len(equal) = 9 always
        increasing, decreasing = ni, nd
    return(count)


if __name__ == "__main__":
    l = count_non_bouncy(100)
    print(l)
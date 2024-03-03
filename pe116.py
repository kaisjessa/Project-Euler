# number of binary strings of length n
# such as 1's appear in groups of exactly m
# don't need to be separated
def F(m, n):
    vals = {}
    for i in range(0, m):
        vals[i] = 1
    vals[m] = 2
    for i in range(m+1, n+1):
        # start with a block of length m
        vals[i] = vals[i-m]
        # start with a 0
        vals[i] += vals[i-1]
    # subtract 1 for the string with all 0's
    return(vals[n]-1)

if __name__ == "__main__":
    n = 50
    print(F(2, n) + F(3, n) + F(4, n))
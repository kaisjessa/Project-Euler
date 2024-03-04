

def solve(n):
    vals = {}
    vals[0] = 1
    vals[1] = 1
    vals[2] = 2
    vals[3] = 4
    for i in range(4, n+1):
        vals[i] = vals[i-1] # starts with empty square
        vals[i] += vals[i-2] # starts with 2-block
        vals[i] += vals[i-3] # starts with 3-block
        vals[i] += vals[i-4] # starts with 4-block
    return(vals[n])


if __name__ == "__main__":
    n = 50
    print(solve(n))
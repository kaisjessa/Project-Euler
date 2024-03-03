def first_n(m, upper):
    vals = {}
    for i in range(0, m):
        vals[i] = 1
    vals[m] = 2
    vals[m+1] = 4
    i = m + 1
    while(vals[i] < upper):
        i += 1
        vals[i] = vals[i-1]+1
        for j in range(m+1, i+1):
            vals[i] += vals[i-j]
        # print(i, vals[i])
    return(i)


if __name__ == "__main__":
    print(first_n(50, 10**6))
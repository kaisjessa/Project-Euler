n = 50
vl = [0 for i in range(n+1)]

def solve():
    vl[0], vl[1], vl[2] = 1, 1, 1
    vl[3] = 2
    vl[4] = 4
    for i in range(5, n+1):
        vl[i] = vl[i-1]+2
        for j in range(i-4, 0, -1):
            vl[i] += vl[j]
        # print(i, vl[i])
    return(vl[n])

if __name__ == "__main__":
    print(solve())
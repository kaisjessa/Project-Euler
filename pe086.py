import math

if __name__ == "__main__":
    count = 0
    M = 0
    triples = []
    while(count <= 10**6):
        # count = 0
        # M is the largest side
        M += 1
        for n in range(1, 2*M + 1):
            l = math.sqrt(M**2 + n**2)
            # perfect square
            if(math.floor(l) == math.ceil(l)):
                # pairs (n-1, 1), (n-2, 2), ..., (n/2, n/2) or ((n+1)/2, (n-1)/2) depending on even or odd
                # need to discount pairs (x, y) with x >= M
                count += math.floor(n/2)
                if(n > M):
                    count -= (n-M-1)
        #print(M, count)
    print(M)
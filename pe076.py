
if __name__ == "__main__":
    n = 100
    partials = [[0 for i in range(n+1)] for i in range(n+1)]
    
    for a in range(1, n+1):
        for b in range(1, a+1):
            if(a<=2 or a==b or b==1):
                partials[a][b] = 1
            else:
                for i in range(1, min(a-b, b)+1):
                    partials[a][b] += partials[a-b][i]
    print([sum(p)-1 for p in partials][100])
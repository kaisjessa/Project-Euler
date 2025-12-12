import math

upper = 120_000

def get_rads(n):
    rads = [1 for i in range(0, n+1)]
    rads[0] = 0
    rads[1] = 1

    for i in range(2, n, 1):
        if(rads[i]==1):
            for j in range(i, n+1, i):
                rads[j] *= i
    return(rads)

if __name__ == "__main__":
    rad=get_rads(upper)
    count = 0
    total = 0
    for a in range(1, upper//2+1):
        for b in range(a+1, upper, 1 if a%2 else 2):
            c = a + b
            if(c >= upper):
                continue
            if(rad[a]*rad[b]*rad[c] >= c):
                continue
            if(math.gcd(rad[a], rad[b]) != 1):
                continue
            count += 1
            total += c
    print(count, total)
import math

if __name__ == "__main__":
    total = 0
    upper = 10**9 // 3
    for n in range(4, upper, 2):
        c = n // 2
        for a in [n-1, n+1]:
            h = math.isqrt(a**2 - c**2)
            if(c**2 + h**2 == a**2):
                total += n + 2*a
    print(total)
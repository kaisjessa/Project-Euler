import math

# 1/3 < n/d < 1/2
# => d/3 < n < d/2
# writes as a <= n < b for integers a,b
# d/3 integer => a = d/3 + 1 = floor(d/3)+1
# d/3 decila =? a = ceil(d/3) = floor(d/3)+1
# d/2 integer => b = d/2 = math.ceil(d/2)
# d/2 decimal => b = d/2 + 1 = math.ceil(d/2)

# need n,d coprime

if __name__ == "__main__":
    k = 12000
    l = []
    for d in range(2, k+1):
        lower = math.floor(d/3)+1
        upper = math.ceil(d/2)
        for n in range(lower, upper):
            l.append(float(n/d))
    print(len(set(l)))
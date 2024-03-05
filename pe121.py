import itertools
import math

def payout(n):
    half = n // 2 + 1
    total = 0
    for i in range(half, n+1, 1):
        for combo in itertools.combinations(list(range(1, n+1)), i):
            current = 1
            for c in range(1, n+1):
                if(c in combo):
                    current *= 1/(c+1)
                else:
                    current *= (1 - 1/(c+1))
            total += current
    return(math.floor(1/total))

if __name__ == "__main__":
    n = 15
    print(payout(n))
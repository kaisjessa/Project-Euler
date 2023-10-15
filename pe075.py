from useful_functions import *
import math

if __name__ == "__main__":
    l = 1500000
    counts = [0 for i in range(l+1)]
    for m in range(3, int(math.sqrt(l))+1, 2):
        for n in range(1, m, 2):
            if(gcd(m,n) == 1):
                a = m*n
                b = (m**2 - n**2)/2
                c = (m**2 + n**2)/2
                s = int(a+b+c)
                k = 1
                while(k*s <= l):
                    counts[k*s] += 1
                    k += 1
    count = [x == 1 for x in counts]
    print(sum(count))
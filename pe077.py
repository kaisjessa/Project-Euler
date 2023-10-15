from useful_functions import *

if __name__ == "__main__":
    n = 75
    partials = [[0 for i in range(n+1)] for i in range(n+1)]
    
    current = 0
    a = 1
    while(current <= 5000):
        b = 2
        while(b <= a):
            if(a == b):
                partials[a][b] = 1
            elif(b == 2 and a % b == 0):
                partials[a][b] = 1
            else:
                i = 2
                while(i <= min(a-b, b)):
                    partials[a][b] += partials[a-b][i]
                    i = next_prime(i)
            b = next_prime(b)
        current = sum(partials[a])
        a += 1
    print(a-1)
import math
from useful_functions import is_prime

def R(k):
    return int("1"*k)

def A(n):
    rem = 1
    for k in range(2,n+1):
        rem = (10*rem + 1) % n
        if(rem == 0):
            return k
    return None


if __name__ == "__main__":
    count = 0
    total = 0
    n = 1
    while count < 25:
        n += 1
        if(n % 2 == 0 or n % 5 == 0):
            continue
        if(is_prime(n)):
            continue
        if((n-1) % A(n) == 0):
            total += n
            count += 1
    print(total)
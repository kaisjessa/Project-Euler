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
    goal = 1_000_000
    upper = 1594323 # 3**13
    for n in range(goal, upper):
        if(n % 2 == 0 or n % 5 == 0):
            continue
        if(A(n) > goal):
            break
    print(n)
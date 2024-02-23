import math
from useful_functions import *

# https://www.wolframalpha.com/input?i=2%28x%29%28x-1%29+%3D+y%28y-1%29

def is_square(n):
    return math.isqrt(n)**2 == n

def solve():
    m = 10**12
    sqrt2 = math.sqrt(2)
    n = 0
    x = 0
    y = 0
    while(y < m):
        a = 3 - 2*sqrt2
        b = 3 + 2*sqrt2
        x = (-2*a**n -sqrt2*a**n -2*b**n + sqrt2*b**n - 4)//8
        y = (-1 +  math.sqrt(8*x**2 - 8*x + 1))//2
        n += 1
        # print(x,y)
    return(x ,y)

if __name__ == "__main__":
    x, y = solve()
    print(int(-x))
    #x: 2 * 2 * 1871 * 94482467
    #y: 2 * 2 * 137 * 1877 * 972199
    #x-1: 3 * 288109 * 818101
    #y-1: 3 * 7 * 1583 * 30081521

    
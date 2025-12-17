from math import isqrt
from useful_functions import prime_factors

def fib(num):
    fibs = [1,1]
    for i in range(2, num):
        fibs.append(fibs[i-1] + fibs[i-2])
    return(fibs)

# def Af(x, terms):
#     fibs = fib(terms)
#     total = 0
#     for i in range(1, terms+1):
#         total += pow(x, i) * fibs[i-1]
#         print(pow(x, i) * fibs[i-1])
#     return(total)

# def is_perfect_square(n):
#     sqrtn = isqrt(n)
#     return sqrtn * sqrtn == n

# def A(x):
#     return x / (1 - x - x**2)

if __name__ == "__main__":
    index = 15
    fibs = fib(2*index + 1)
    print(fibs[index*2]*fibs[index*2-1])
def count_solutions(n):
    num_factors = 1
    nn = n**2
    primes = [2, 3, 5, 7, 11, 13, 17]
    i = 0
    while(nn > 1 and i <= 6):
        r = primes[i]
        if(nn % r == 0):
            temp = 0
            while(nn % r == 0):
                temp += 2
                nn //= r**2
            num_factors *= (temp + 1)
        i += 1
    # print(num_factors)
    # if(i >= 7): return 0
    return (num_factors+1)//2

def solve():
    n = 4
    sols = 0
    for i in range(510510):
        sols = count_solutions(n)
        if(sols > 1000):
            return n
        n += 1

if __name__ == "__main__":
    print(solve())
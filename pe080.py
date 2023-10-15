from decimal import *
getcontext().prec = 103

def dig_sum(n):
    s = Decimal(n).sqrt()
    s = str(s).replace('.','')[:-3]
    return sum([int(i) for i in s])
if __name__ == "__main__":
    squares = [n**2 for n in range(1, 11)]
    total = 0
    for i in range(2, 100):
        if(i not in squares):
            total += dig_sum(i)
    print(total)
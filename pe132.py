from useful_functions import sieve

primes = sieve(200000)

def R_modulo(k, p):
    if(10 % p == 0):
        return 1
    digits = [1]
    for i in range(1, p):
        rem = (digits[i-1] * 10) % p
        if(rem == 1):
            break
        digits.append((digits[i-1] * 10) % p)
    period = i
    remaining = digits[:k % period]
    total = sum(remaining) % p
    total += sum(digits) * (k // period)
    total %= p
    return(total)

if __name__ == "__main__":
    k = 10**9
    arr = []
    for prime in primes:
        if(len(arr) >= 40):
            break
        if(R_modulo(k, prime) == 0):
            arr.append(prime)
    print(sum(arr))
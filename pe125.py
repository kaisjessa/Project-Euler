import math


def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def solve(upper: int) -> int:
    total = 0
    valids = set()
    for start in range(1, math.isqrt(upper) + 1, 1):
        l = 1
        temp = start**2 + (start + l) ** 2
        while temp < upper:
            if is_palindrome(temp) and temp not in valids:
                valids.add(temp)
                total += temp
            l += 1
            temp += (start + l) ** 2
    return total


if __name__ == "__main__":
    upper = 10**8
    print(solve(upper))

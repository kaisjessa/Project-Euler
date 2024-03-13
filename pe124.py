from useful_functions import *
from math import log, floor
from itertools import product


def rad(n: int) -> int:
    total = 1
    for i in unique_prime_factors(n):
        total *= i
    return total


def get_power_tuples(n: int, upper: int) -> tuple[list, list[tuple[int, ...]]]:
    facts = unique_prime_factors(n)
    bounds = []
    for p in facts:
        b = floor(log(upper, p))
        bounds.append(list(range(1, b + 1)))
    power_tuples = list(product(*bounds))
    return facts, power_tuples


def powers_of_factors(n: int, upper: int) -> list[int]:
    prime_factors, power_tuples = get_power_tuples(n, upper)
    powers = []
    for p in power_tuples:
        temp = 1
        for i, j in zip(p, prime_factors):
            temp *= j**i
        if temp <= upper:
            powers.append(temp)
    return sorted(powers)


def solve(upper: int, index: int) -> int:
    rad_list = [0, 1]
    n = 1
    while len(rad_list) <= index:
        while n in rad_list:
            n += 1
        rad_list += powers_of_factors(n, upper)
    return rad_list


if __name__ == "__main__":
    upper = 100_000
    index = 10_000
    r = solve(upper, index)
    print(r[index])

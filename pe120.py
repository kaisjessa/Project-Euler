def rem(a, n):
    return ((a - 1) ** n + (a + 1) ** n) % a**2


if __name__ == "__main__":
    total = 0
    for a in range(3, 1001):
        cmax = 2 * a
        n = 3
        current = rem(a, n)
        while rem(a, n) != 2 * a:
            cmax = max(cmax, current)
            n += 2
            current = rem(a, n)
        total += cmax
    print(total)

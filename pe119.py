def sum_of_digits(n):
    return sum([int(x) for x in str(n)])


# returns True if n is a power of m
def is_power(n, m):
    if n == 1:
        return True
    if n % m == 0:
        return is_power(n // m, m)
    else:
        return False


if __name__ == "__main__":
    n = 30
    a_list = [81]
    lower = "10"
    upper = "99"

    while len(a_list) < 3 * n:
        lower = lower[:-1] + "01"
        upper += "9"
        lsum = sum([int(x) for x in lower])
        hsum = sum([int(x) for x in upper])
        for base in range(2, hsum + 1):
            p = 1
            while base**p < int(lower):
                p += 1
            while base**p <= int(upper):
                if sum_of_digits(base**p) == base:
                    a_list.append(base**p)
                p += 1
    print(a_list[n - 1])

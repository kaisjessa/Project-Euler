def search(a, b, d):
    if a == b:
        return a * (fast_count(a, d) == a)
    if fast_count(a, d) > b:
        return 0
    if fast_count(b, d) < a:
        return 0
    c = (a + b) // 2
    return search(a, c, d) + search(c + 1, b, d)


def fast_count(n, d):
    count = 0
    k = 0
    rem = 0
    while n > 0:
        digit = n % 10
        if digit < d:
            count += k * (10 ** (k - 1)) * digit
        elif digit > d:
            count += 10**k + k * (10 ** (k - 1)) * digit
        else:
            count += k * (10 ** (k - 1)) * digit + rem + 1
        rem += 10**k * digit
        n //= 10
        k += 1
    return int(count)


# def count_digits(n, d):
#     total = 0
#     count = 0
#     d = str(d)
#     for i in range(0, n + 1):
#         count += str(i).count(d)
#         if i == count:
#             total += count
#     return count


if __name__ == "__main__":
    upper = 10**10
    total = 0
    for d in range(1, 10):
        total += search(0, d * upper, d)
    print(total)

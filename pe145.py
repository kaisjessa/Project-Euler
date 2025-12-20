def reverse(n):
    global reverse_times
    rn = int(str(n)[::-1])
    return rn


def no_even(n):
    while n > 0:
        if n % 2 == 0:
            return False
        n //= 10
    return True


def solve(digits):
    if digits % 2 == 0:
        return 20 * 30 ** (digits // 2 - 1)
    if digits in [1, 5, 9]:
        return 0
    count = 0
    for a in range(10 ** (digits - 1) + 1, 10**digits, 2):
        ra = reverse(a)
        if no_even(a + ra):
            count += 2
    return count


if __name__ == "__main__":
    total = 0
    for digits in range(1, 10):
        total += solve(digits)
    print(total)

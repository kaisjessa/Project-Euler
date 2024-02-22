
# find last 10 digits of 28433 * 2^7830457 + 1

n = 28433
for i in range(7830457):
    n *= 2
    n %= 10**10
n += 1
print(n)
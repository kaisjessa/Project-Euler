import itertools

squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
squares = [s.replace('9', '6') for s in squares]

digits = list("0123456789")
comb = itertools.combinations(digits, 6)
comb = list(comb)
l = len(comb)

count = 0
for i in range(0, l, 1):
    c1 = comb[i]
    c1 = [c.replace('9', '6') for c in c1]
    for j in range(i, l, 1):
        c2 = comb[j]
        c2 = [c.replace('9', '6') for c in c2]
        if(False not in [(s[0] in c1 and s[1] in c2) or (s[0] in c2 and s[1] in c1) for s in squares]):
            count += 1

print(count)
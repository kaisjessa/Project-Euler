# numbers under 1e7 that arrive at 89
# 9,999,999 -> 7*81 = 567 upper bound
# just need to figure out which of 1-567 reach 1 or 89

def next_in_chain(n):
    return sum([int(d)**2 for d in str(n)])

if __name__ == "__main__":
    u = 567
    chains = [0 for i in range(u+1)]
    for i in range(1, u+1):
        j = i
        while(j not in [1, 89]):
            j = next_in_chain(j)
        chains[i] = j

    total = chains.count(89)
    current = next_in_chain(567)
    for i in range(568, 10**7):
        if(i % 10 == 0):
            current = next_in_chain(i)
        else:
            current += 2 * (i % 10) - 1
        if(chains[current] == 89):
            total += 1
    print(total)
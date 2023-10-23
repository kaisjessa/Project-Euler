hands = []
with open("files/pe054_poker.txt", 'r') as f:
    for line in f.readlines():
        l = line.strip().split(" ")
        hands.append([tuple(l[:5]), tuple(l[5:])])

# lines = """5H 5C 6S 7S KD 2C 3S 8S 8D TD
#     5D 8C 9S JS AC 2C 5C 7D 8S QH
#     2D 9C AS AH AC 3D 6D 7D TD QD
#     4D 6S 9H QH QC 3D 6D 7H QD QS
#     2H 2D 4C 4D 4S 3C 3D 3S 9S 9D """

# for line in lines.split("\n"):
#     l = line.strip().split(" ")
#     hands.append([tuple(l[:5]), tuple(l[5:])])

vals = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
for i in range(2, 10):
    vals[str(i)] = i

# given hand, determines rank, highest card in rank, and highest card
def determine_hand(hand):
    rank = -1
    hrank = -1
    nums = [vals[a[0]] for a in hand]
    suits = [a[1] for a in hand]
    high = max(nums)
    straight = sorted(nums)[::-1] == [high, high-1, high-2, high-3, high-4]
    flush = False not in [suits[0] == suits[i] for i in range(len(suits))]
    counts = {n: nums.count(n) for n in nums}
    next_highs = sorted(nums)[::-1]
    # royal flush
    if(straight and flush and high == vals['A']):
        rank = 0
        hrank = vals["A"]
    # straight flush
    elif(straight and flush):
        rank = 1
        hrank = high
    # four of a kind
    elif(4 in counts.values()):
        rank = 2
        hrank = max([a for a in nums if nums.count(a) == 4])
    # full house
    elif(3 in counts.values() and 2 in counts.values()):
        rank = 3
        hrank = max([a for a in nums if nums.count(a)==3])
    # flush
    elif(flush):
        rank = 4
        hrank = high
    # straight
    elif(straight):
        rank = 5
        hrank = high
    # 3 of a kind
    elif(3 in counts.values()):
        rank = 6
        hrank = max([a for a in nums if nums.count(a)==3])
    # 2 pairs
    elif(list(counts.values()).count(2) == 2):
        rank = 7
        hrank = max([a for a in nums if nums.count(a)==2])
    # 1 pair
    elif(2 in counts.values()):
        rank = 8
        hrank = max([a for a in nums if nums.count(a)==2])
    # high card
    else:
        rank = 9
        hrank = high
    r = [14-rank, hrank] + next_highs
    return r

if __name__ == "__main__":
    num_wins = 0
    for hand in hands:
        h1 = hand[0]
        h2 = hand[1]

        r1 = determine_hand(h1)
        r2 = determine_hand(h2)
        i = 0
        while(i < 6 and r2[i] <= r1[i]):
            if(r1[i] > r2[i]):
                num_wins += 1
                break
            i += 1
    print(num_wins)


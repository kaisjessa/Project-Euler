import random

monopoly = """GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T1 H2"""
monopoly = monopoly.split(" ")
#print(len(monopoly))
jail = monopoly.index("JAIL")

def roll(n):
    r1 = random.randint(1, n)
    r2 = random.randint(1, n)
    return(r1 + r2)

cc_list = ["" for i in range(14)] + ["GO", "JAIL"]
ch_list = ["" for i in range(6)] + ["GO", "JAIL", "C1", "E3", "H2", "R1", "next R", "next R", "next U", "back 3"]
random.shuffle(cc_list)
random.shuffle(ch_list)

def process_move(current, dice, prev_rolls):
    if(len(prev_rolls) >= 2 and dice==prev_rolls[-1] and dice==prev_rolls[-2]):
        return jail
    current = (current + dice) % 40
    square = monopoly[current]
    if(square == "G2J"):
        return jail
    action = ""
    if(square.startswith("CC")):
        action = cc_list.pop(0)
        cc_list.append(action)
    if(square.startswith("CH")):
        action = ch_list.pop(0)
        ch_list.append(action)
    if(len(action) > 0):
        if(action in ["GO", "JAIL", "C1", "E3", "H2", "R1"]):
           current = monopoly.index(action)
        if("next" in action):
            while monopoly[current][0] != action[-1]:
                current = (current + 1) % 40
        if("back" in action):
            current = (current - 3) % 40
    return current

if __name__ == "__main__":
    # sides on dice
    n = 4
    # start at GO
    current = 0
    # count of landing on each square
    counts = [0 for i in range(40)]
    # list of last 2 rolls
    rolls = []

    # play rounds
    for i in range(10**6):
        current = process_move(current, roll(n), rolls)
        counts[current] += 1
        rolls.append(current)
        rolls = rolls[-2:]

    probs = [(counts[i], monopoly[i]) for i in range(40)]
    probs = sorted(probs)[::-1][:3]
    s = ""
    for _, p in probs:
        s += "{:02}".format(monopoly.index(p))
    print(s)
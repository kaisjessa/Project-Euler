import math
def get_pairs():
    pairs = []
    with open("files/pe099_base_exp.txt", 'r') as f:
        for l in f.readlines():
            pairs.append([int(i) for i in l.split(",")])
    return(pairs)


if __name__ == "__main__":
    pairs = get_pairs()
    highest = -1
    index = -1
    for i in range(len(pairs)):
        p = pairs[i]
        c = p[1]*math.log(p[0])
        if(c > highest):
            highest = c
            index = i
    print(index + 1)

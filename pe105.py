import itertools

def is_valid(arr):
    sums = []
    sum_dict = {}
    l = len(arr)
    for k in range(l):
        sum_dict[k] = []
        for i in itertools.combinations(arr, k):
            s = sum(i)
            sum_dict[k].append(s)
            # if this subset sum matches another
            if s in sums:
                return False
            # if this sum is smaller than a sum for a smaller subset
            for r in range(0, k):
                if(s < max(sum_dict[r])):
                    # print(i, s, r, sum_dict[r])
                    return False
            sums.append(s)
    return True

def get_sets():
    sets = []
    with open("files/pe105_sets.txt", 'r') as f:
        for l in f.readlines():
            sets.append([int(i) for i in l.split(",")])
    return(sets)


if __name__ == "__main__":
    sets = get_sets()
    total = 0
    for s in sets:
        if(is_valid(s)):
            total += sum(s)
    print(total)
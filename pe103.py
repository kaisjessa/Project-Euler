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

def add_list(arr, q):
    return [arr[i] + q[i] for i in range(len(arr))]

if __name__ == "__main__":
    arr = [20, 20+11, 20+18, 20+19, 20+20, 20+22, 20+25]
    best_sum = sum(arr)
    best_set = arr
    for k in range(1, 3):
        p = list(range(-k, k+1))
        q = list(range(-k, k+1))
        q = itertools.product(p, q)
        for i in range(5):
            q = list(itertools.product(p, q))
            q = [(a,*_) for (a,(_)) in q]
            # total sum < current best sum
            q = [qq for qq in q if sum(qq) < 0]
        for qq in q:
            current = add_list(arr, qq)
            if(sum(current) < best_sum and is_valid(current)):
                print(current)
                best_set = current
                best_sum = sum(current)
    print(''.join([str(i) for i in best_set]))
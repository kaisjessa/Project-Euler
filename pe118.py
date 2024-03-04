from useful_functions import *
import itertools
import sys

def prime_partitions(s):
    if(len(s) == 0):
        return [[]]
    if(len(s) == 1):
        if(is_prime(int(s))):
            return [[int(s)]]
        else:
            return [[]]
    arr = []
    for i in range(1, len(s)+1, 1):
        if(is_prime(int(s[:i]))):
            for a in prime_partitions(s[i:]):
                # make sure the list is in order
                # prevent double counting
                if(i == len(s) or (len(a) > 0 and int(s[:i]) < min(a))):
                    arr.append([int(s[:i])] + a)
    return(arr)


if __name__ == "__main__":
    digs = '123456789'
    total = 0
    for t in itertools.permutations(digs):
        s = ''.join(t)
        p = prime_partitions(s)
        total += len(p)
    print(total)
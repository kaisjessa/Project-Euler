import math

if __name__ == "__main__":
    low_diff = 1
    mn = 0
    md = 0
    for d in range(1, 10**6):
        for n in range(int(299999*d/700000), int(3*d/7)):
            f = abs(3/7-n/d)
            if(f < low_diff):
                low_diff = f
                mn = n
                md = d
    print(mn)
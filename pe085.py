import math

# def num_rects(n, m):
#     count = 0
#     for i in range(n+1):
#         for j in range(m+1):
#             count += i*j
#     return count

def num_rects(n, m):
    first = n*(n+1)/2
    second = m*(m+1)/2
    return first * second

if __name__ == "__main__":
    goal = 2*10**6
    pair = (0,0)
    closest = 0
    area = 0
    m = 1
    while(m <= int(math.sqrt(goal)) + 1):
        n = 1
        while(n <= m):
            num = num_rects(n,m)
            if(abs(goal-num) < abs(goal-closest)):
                closest = num
                pair = (m, n)
                area = m * n
            n += 1
            if(num > goal):
                break
        m += 1
    print(area)
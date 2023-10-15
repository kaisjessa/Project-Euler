import math
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations

if __name__ == "__main__":
    p = [1, 1, 2, 3]
    found = False
    n = len(p)
    while(not found):
        current = 0
        lower = 1 - math.sqrt(24*n + 1)
        lower /= 6
        lower = math.ceil(lower)

        upper = 1 + math.sqrt(24*n + 1)
        upper /= 6
        upper = math.floor(upper)

        for k in range(lower, upper+1, 1):
            if(k != 0):
                index = n-(k*(3*k-1)/2)
                if(index >= 0):
                    current += (-1)**(k+1)*p[int(index)]
        p.append(current % 10**6)
        if(current % 10**6 == 0):
            found = True
        else:
            n += 1
    print(n)
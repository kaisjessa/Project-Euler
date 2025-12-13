from useful_functions import sieve, is_prime

def get_hex(index, branch):
    if(index == -1):
        return 1
    if(branch == 6):
        return 2 + 6 * (index*(index+1))//2 + branch*(index+1) - 1
    return 2 + 6 * (index*(index+1))//2 + branch*(index+1)

def get_neighbours(index, branch):
    if(branch) == 0:
        l = []
        top = get_hex(index+1, branch)
        l.append(top)
        l.append(top+1)
        l.append(get_hex(index, branch)+1)
        l.append(get_hex(index-1, branch))
        l.append(top-1)
        l.append(get_hex(index+2, branch)-1)
        return l
    if(branch == 6):
        l = []
        top = get_hex(index+1, branch)
        l.append(top)
        l.append(top-1)
        l.append(get_hex(index, branch)-1)
        l.append(get_hex(index-1, branch))
        l.append(get_hex(index-1, 0))
        l.append(get_hex(index, 0))
        return l
    l = []
    top = get_hex(index+1, branch)
    l.append(top-1)
    l.append(top)
    l.append(top+1)
    l.append(get_hex(index, branch)+1)
    l.append(get_hex(index-1, branch))
    l.append(get_hex(index, branch)-1)
    return l

def PD(index, branch, primes):
    current = get_hex(index, branch)
    neighbours = get_neighbours(index, branch)
    diffs = [abs(current-n) for n in neighbours]
    primes = [p for p in diffs if is_prime(p, primes)]
    return(len(primes))


if __name__ == "__main__":
    primes = sieve(100)
    goal = 2000
    count = 1
    index = 0
    while(count < goal):
        for branch in range(0, 7):
            if(PD(index, branch, primes) == 3):
                count += 1
                if(count == goal):
                    print(count, get_hex(index, branch))
        index += 1
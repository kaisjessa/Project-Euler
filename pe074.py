facts = [1]
for i in range(1, 10):
    j = i * facts[i-1]
    facts.append(j)

def fact_sum(n):
    digits = list(str(n))
    s = sum([facts[int(d)] for d in digits])
    return(s)

if __name__ == "__main__":
    count = 0
    for i in range(3, 10**6):
        temp = [i]
        j = fact_sum(i)
        while(j not in temp):
            temp.append(j)
            j = fact_sum(j)
        if(len(temp) == 60):
            count += 1
    print(count)
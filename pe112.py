
def is_bouncy(n):
    s = str(n)
    if(len(s) == 1):
        return False
    if False not in [int(s[i+1]) >= int(s[i]) for i in range(len(s)-1)]:
        return False
    if False not in [int(s[i+1]) <= int(s[i]) for i in range(len(s)-1)]:
        return False
    return True

if __name__ == "__main__":
    bouncy_count = 0
    n = 1
    while(bouncy_count / n < 0.99):
        n += 1
        if(is_bouncy(n)):
            bouncy_count += 1
    print(n)
# def solve():
#     n = 15
#     m = [i-1 for i in range(n+1)]
#     print(m)
#     for k in range(4, n+1):
#         for i in range(1, k):
#             m[k] = min(m[k], 1 + m[i] + m[k-i])
#         if(k % 2 == 0):
#             m[k] = min(m[k], 2*m[k//2])
#     return m
# terms = {}
# terms[1] = [1]
# terms[2] = [1, 2]
# terms[3] = [1, 2, 3]

# def generate_terms(n):
#     if(n in terms.keys()):
#         return terms[n]
#     current = [i for i in range(1, n+1)]
#     for i in range(1, n//2+1):
#         temp = sorted(list(set(generate_terms(i) + generate_terms(n-i) + [n])))
#         if(len(temp) <= len(current)):
#             current = temp
#     terms[n] = current
#     return(current)

terms = {}
terms[1] = (1, [[1]])
terms[2] = (2, [[1, 2]])
terms[3] = (3, [[1, 2, 3]])

def generate_terms(n):
    if(n in terms.keys()):
        return terms[n]
    current = (n, [[i for i in range(1, n+1)]])
    for i in range(1, n//2+1, 1):
        left = generate_terms(i)[1]
        right = generate_terms(n - i)[1]
        for l in left:
            for r in right:
                c = sorted(list(set(l+r+[n])))
                if(len(c) < current[0]):
                    current = (len(c), [c])
                elif(len(c) == current[0]):
                    current = (current[0], current[1] + [c])
    terms[n] = current
    return(current)


if __name__ == "__main__":
    u = 200
    total = 0
    for n in range(1, u+1):
        num_terms = generate_terms(n)[0]-1
        total += num_terms
    print(total)
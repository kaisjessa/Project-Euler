from useful_functions import *
import itertools

# def solve(n):
#     M = [0 for i in range(10)]
#     S = [0 for i in range(10)]
#     for i in range(10**(n-1)+1, 10**n, 2):
#         if(is_prime(i)):
#             for d in range(0, 10):
#                 c = str(i).count(str(d))
#                 if c > M[d]:
#                     M[d] = c
#                     S[d] = i
#                     print(i, M)
#                 elif c == M[d]:
#                     S[d] += i
#             print(i)
#     print(M)
#     print(S)
#     return(sum(S))

# returns True if there exists a prime of length k with k repeats of digit d
# False otherwise
def prime_exists(n, k, d):
    r = n - k # remaining digits
    p = list(range(0, 10))
    p.remove(d)
    q = p.copy()
    if(r > 1):
        q = list(itertools.product(p,p))
        for i in range(r-2):
            q = list(itertools.product(p, q))
            q = [(a,*_) for (a,(_)) in q]
            # sorted
            q = [qq for qq in q if list(qq) == sorted(qq)]
    else:
        q = [[i] for i in q]
    s1 = str(d)*k
    for qq in q:
        s2 = ''.join([str(qqq) for qqq in list(qq)])
        for temp in set(itertools.permutations(s1+s2)):
            if(temp[0] != '0'):
                temp = int(''.join(temp))
                if(is_prime(temp)):
                    return True
    return(False)

def generate_prime_sum(n, k, d):
    total = 0
    r = n - k # remaining digits
    p = list(range(0, 10))
    p.remove(d)
    q = p.copy()
    if(r > 1):
        q = list(itertools.product(p,p))
        for i in range(r-2):
            q = list(itertools.product(p, q))
            q = [(a,*_) for (a,(_)) in q]
            # sorted
            q = [qq for qq in q if list(qq) == sorted(qq)]
        q = [qq for qq in q if list(qq) == sorted(qq)]
    else:
        q = [[i] for i in q]
    s1 = str(d)*k
    for qq in q:
        s2 = ''.join([str(qqq) for qqq in list(qq)])
        for temp in set(itertools.permutations(s1+s2)):
            if(temp[0] != '0'):
                temp = int(''.join(temp))
                if(is_prime(temp)):
                    total += temp
    return(total)

if __name__ == "__main__":
    n = 10
    # M = [0 for i in range(10)]
    # for d in range(10):
    #     for k in range(9, 0, -1):
    #         if(prime_exists(n, k, d)):
    #             M[d] = k
    #             break
    # print(M)
    M = [8, 9, 8, 9, 9, 9, 9, 9, 8, 9]
    total = 0
    for d in range(0, 10):
        total += generate_prime_sum(n, M[d], d)
    print(total)

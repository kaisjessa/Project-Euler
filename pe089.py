'''Numerals must be arranged in descending order of size.
M, C, and X cannot be equalled or exceeded by smaller denominations.
D, L, and V can each only appear once.

Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.
'''

strs = ["I", "V", "X", "L", "C", "D", "M"]
eqs = [1, 5, 10, 50, 100, 500, 1000]
d_to_n = {}
n_to_d = {}
for i in range(len(strs)):
    d_to_n[strs[i]] = eqs[i]
    n_to_d[eqs[i]] = strs[i]
nums = []
with open("files/pe089_roman.txt", 'r') as f:
    for l in f.readlines():
        nums.append(l.strip())

def roman_to_num(s):
    if(len(s) == 1):
        return d_to_n[s]
    else:
        first = s[0]
        second = s[1]
        if(strs.index(first) < strs.index(second)):
            return roman_to_num(s[1:]) - d_to_n[first]
        return d_to_n[first] + roman_to_num(s[1:])

def num_to_roman(n):
    # multiples of each power of 10
    r = list(str(n))[::-1]
    m = {}
    i = 1
    for s in r:
        m[i] = int(s)
        i *= 10
    ret = ""
    for k in list(m.keys())[::-1]:
        # k: base, m[k]: multiple of base
        d = ""
        if(m[k] in [0, 1, 2, 3, 4]):
            d = m[k] * n_to_d[k]
        if(m[k] in [5, 6, 7, 8, 9]):
            d = n_to_d[5*k] + (m[k] - 5) * n_to_d[k]
        if(m[k] == 4 and "M" not in d):
            d = n_to_d[k] + n_to_d[5*k]
        if(m[k] == 9 and "M" not in d):
            d = n_to_d[k] + n_to_d[10*k]
        ret += d
    return(ret)

if __name__ == "__main__":
    total = 0
    for s in nums:
        l1 = len(s)
        n = roman_to_num(s)
        s = num_to_roman(n)
        l2 = len(s)
        total += l1 - l2
    print(total)
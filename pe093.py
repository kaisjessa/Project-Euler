# from operator import add, sub, mul, floordiv, truediv
from itertools import permutations, combinations_with_replacement

def get_digs():
    sets = []
    for k in range(1234, 6789+1):
        ar = [int(i) for i in str(k)]
        a,b,c,d = ar
        if(a < b and b < c and c < d):
            sets.append(''.join([str(i) for i in [a,b,c,d]]))
    return(sets)

def get_ops():
    ops = []
    # div = floordiv
    operators = ['+', '-', '*', '/']
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ops.append((operators[i], operators[j], operators[k]))
    return ops

def get_eqs(a,x,b,y,c,z,d):
    eqs = []
    eqs.append( a + x + b + y + c + z + d )
    eqs.append("(" + a + x + b + ")" + y + c + z + d )
    eqs.append( a + x + "(" + b + y + c + ")" + z + d )
    eqs.append( a + x + b + y + "("+ c + z + d + ")")
    eqs.append( "(" + a + x + b + y + c + ")" + z + d )
    eqs.append( a + x + "(" + b + y + c + z + d + ")")
    eqs.append( "((" + a + x + b + ")" + y + c + ")" + z + d )
    eqs.append( "(" + a + x + "(" + b + y + c + "))" + z + d )
    eqs.append( a + x + "((" + b + y + c + ")" + z + d + ")")
    eqs.append( a + x + "(" + b + y + "(" + c + z + d + "))")
    eqs.append( "(" + a + x + b + ")" + y + "(" + c + z + d + ")")
    return(eqs)


if __name__ == "__main__":
    digits = get_digs()
    ops = get_ops()
    best_n = 28
    best_comb = "1234"

    count = 0
    # a < b < c < d (126)
    for dig in digits:
        l = []
        # permutations of a,b,c,d (24)
        for a,b,c,d in permutations(dig):
            # choice of operations (64)
            for x,y,z in ops:
                # choice of parentheses (11)
                eqs = get_eqs(a,x,b,y,c,z,d)
                # evaluate all
                for e in eqs:
                    try: 
                        l.append(eval(e))
                    except:
                        pass
                # determine smallest digit not present
        # print(l)
        t = 1.0
        while(t in l):
            t += 1.0
        if(t > best_n):
            best_n = t
            best_comb = dig
    print(best_comb)

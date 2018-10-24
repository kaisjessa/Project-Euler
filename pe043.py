import math
import itertools
digits = [0,1,2,3,4,5,6,7,8,9]
primes = [2,3,5,7,11,13,17]
pandigitals = list(itertools.permutations(digits))

total = 0
for num in pandigitals:
	s_arr = [str(n) for n in list(num)]
	s = "".join(s_arr)
	if(int(s[1:4])%2==0 and int(s[2:5])%3==0 and int(s[3:6])%5==0 and int(s[4:7])%7==0 and int(s[5:8])%11==0 and int(s[6:9])%13==0 and int(s[7:10])%17==0):
		total += int(s)
print(total)

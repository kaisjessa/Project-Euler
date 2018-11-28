'''
total of 9 digits
a*b=x
len(a)+len(b)+len(x)=9

'''

arr=['1','2','3','4','5','6','7','8','9']
total = 0
used_ints = []
for a in range(1, 100):
	for b in range(a, 10000):
		x = a*b
		s = sorted(list(str(a)+str(b)+str(x)))
		if(s==arr and x not in used_ints):
			used_ints.append(x)
			total += x
print(total)

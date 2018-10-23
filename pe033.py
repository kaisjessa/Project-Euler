'''
n<d
let x be the cancelled digit
first digits cancel:
(10x+n)/(10x+d)=(n/d)
first and second digits cancel:
(10x+n)/(10d+x)=(n/d)
second and first digits cancel:
(10n+x)/(10x+d)=(n/d)
secon digits cancel:
(10n+x)/(10d+x)=(n/d)

'''


frac_list = []
for a in range(10,100):
	for b in range(a+1, 100):
		q = float(a)/float(b)
		a0 = float(str(a)[0])
		a1 = float(str(a)[1])
		b0 = float(str(b)[0])
		b1 = float(str(b)[1])
		#cancel first digits
		if(a0==b0 and b1 != 0):
			if(q == (a1/b1)):
				frac_list.append([a1, b1])
		#cancel first and last digits
		if(a0==b1 and b0 != 0):
			if(q == (a1/b0)):
				frac_list.append([a1, b0])
		#cancel last and first digits
		if(a1==b0 and b1 != 0):
			if(q == (a0/b1)):
				frac_list.append([a0, b1])
		#cancel last digits
		if(a1==b1 and b0 != 0):
			if(1 == (a0/b0)):
				frac_list.append([a0, b0])
n = 1
d = 1
for i in frac_list:
	n = n * i[0]
	d = d * i[1]

def gdc(num, den):
	for x in range(2, num+1):
		if num % x == 0 and den % x == 0:
			return(gdc(int(num/x), int(den/x)))
	return(den)

print(gdc(int(n),int(d)))



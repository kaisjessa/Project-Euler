import math
import itertools

def poly(a, n):
	if(a==3):
		return int(n*(n+1)/2)
	if(a==4):
		return int(n**2)
	if(a==5):
		return int(n*(3*n-1)/2)
	if(a==6):
		return int(n*(2*n-1))
	if(a==7):
		return int(n*(5*n-3)/2)
	if(a==8):
		return int(n*(3*n-2))

arr = [[] for x in range(9)]

for a in range(3, 9):
	n = 1
	x = poly(a,n)
	while x <= 9999:
		if(x >= 1000):
			arr[a].append(x)
		n += 1
		x = poly(a,n)

def cyc(x, y):
	return int(str(x)[2:4]) == int(str(y)[0:2])

indices = [3, 4, 5, 6, 7, 8]
orders = list(itertools.permutations(indices))
#orders = [[3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3]]

for o in orders:
	a = arr[o[0]]
	b = arr[o[1]]
	c = arr[o[2]]
	d = arr[o[3]]
	e = arr[o[4]]
	f = arr[o[5]]
	for aa in a:
		for bb in b:
			if cyc(aa, bb):
				for cc in c:
					if cyc(bb, cc):
						for dd in d:
							if cyc(cc, dd):
								for ee in e:
									if cyc(dd, ee):
										for ff in f:
											if cyc(ee, ff):
												if cyc(ff, aa):
													print(aa+bb+cc+dd+ee+ff)
													quit()


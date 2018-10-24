import math
'''
y = n(3n-1)/2
n = (sqrt(24y+1)+1)/6

'''

def is_pentagonal(y):
	if(y<1):
		return False
	if((math.floor((math.sqrt(24*y+1)+1)/6)) == (math.ceil((math.sqrt(24*y+1)+1)/6))):
		return True
	return False

def solution():
	for n in range(1, 5000):
		j = int(n*(3*n-1)/2)
		for m in range(n+1, 5000):
			k = int(m*(3*m-1)/2)
			if(is_pentagonal(j+k) and is_pentagonal(k-j)):
				return(k-j)
	return("not found")


print(solution())
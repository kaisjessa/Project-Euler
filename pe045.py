import math
#Triangle: Tn=n(n+1)/2
#Pentagonal: Pn=n(3n−1)/2
#Hexagonal: Hn=n(2n−1)

def is_triangle_pentagonal(y):
	if((math.floor((math.sqrt(8*y+1)-1)/2)) == (math.ceil((math.sqrt(8*y+1)-1)/2)) and
		(math.floor((-1*math.sqrt(24*y+1)-1)/6)) == (math.ceil((-1*math.sqrt(24*y+1)-1)/6))):
		return True
	return False


found = 0
index = 143
while found == 0:
	index += 1
	num = index * (2*index - 1)
	if(is_triangle_pentagonal(num)):
		found = num

print(found)

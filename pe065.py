#e = [2;1,1,2,1,1,4,1,1,...,2k,1,1,...]
e = [2]
c = 1
for i in range(0, 99):
	if(i%3==1):
		e.append(2*c)
		c += 1
	else:
		e.append(1)
e1 = e[::-1]
#e1 = [4,1,1,2,1,2]

num = 1
dem = e1[0]
for elem in e1[1:]:
	#add previous element to fraction
	num += dem*elem
	#take reciprocal
	temp = num
	num = dem
	dem = temp

print(sum([int(i) for i in str(dem)]))

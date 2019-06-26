#p=1, q=1
#(p+2q)/(p+q)
#p=num, q=dem

p = 1
q = 1
count = 0
for i in range(1000):
	if(len(str(p)) > len(str(q))):
		count += 1
	num = p + 2*q
	dem = p + q
	p = num
	q = dem
print(count)

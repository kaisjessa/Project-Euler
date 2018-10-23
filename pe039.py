import math
p_list = []

for a in range(1, math.ceil(1000/3)):
	for b in range(a, math.ceil(1000/2)):
		c = math.sqrt(a**2+b**2)
		if math.ceil(c)==math.floor(c) and a+b+c<=1000:
			p_list.append(a+b+int(c))

max_count = 0
max_p = 0
for i in p_list:
	if p_list.count(i) > max_count:
		max_count = p_list.count(i)
		max_p = i
print(max_p)


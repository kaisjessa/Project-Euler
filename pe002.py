count = 0

a = 1
b = 1

while b <= 4000000:
	c = a + b
	if(c%2==0):
		count += c
	a = b
	b = c

print(count)
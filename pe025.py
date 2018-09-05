count = 2

f1 = 1
f2 = 1

while len(str(f2)) < 1000:
	count += 1
	temp = f2
	f2 += f1
	f1 = temp
print(count)
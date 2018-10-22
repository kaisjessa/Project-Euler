int_list = []

for a in range(2, 101):
	for b in range(2, 101):
		int_list.append(a**b)

print(len(list(set(int_list))))
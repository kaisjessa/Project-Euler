from itertools import permutations
x = list(permutations(list(range(10))))
s = ""
for i in x[1000000-1]:
	s += str(i)
print(s)

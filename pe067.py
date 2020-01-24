s = ""
with open("p067_triangle.txt") as f:
	for line in f:
		s += line

x = [[int(n) for n in i.split()] for i in s.split("\n")][:-1]
#print(x)
for i in range(len(x)-1, 0, -1):
	temp = []
	for j in range(len(x[i])-1):
		temp.append(max((x[i-1][j]+x[i][j]),(x[i-1][j]+x[i][j+1])))
	x.pop()
	x.pop()
	x.append(temp)
print(x[0][0])

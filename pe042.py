chars = sorted(list("QWERTYUIOPASDFGHJKLZXCVBNM"))
with open("p042_words.txt") as f:
	text = f.readlines()
	f.close()
arr = text[0].split(",")
arr = [x.replace('"','') for x in arr]
values = []
for word in arr:
	val = 0
	for char in word:
		val = val + chars.index(char)+1
	values.append(val)

triangles = [1]
x = 1
while(triangles[-1] <= max(values)):
	triangles.append(int(x*(x+1)*(1/2)))
	x += 1

count = 0
for val in values:
	if val in triangles:
		count += 1
print(count)

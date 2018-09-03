with open("names.txt") as f:
	text = f.readlines()
text_arr = text[0].replace('"','').split(",")
text_arr = sorted(text_arr)

total = 0

for i in range(len(text_arr)):
	temp = 0
	for c in text_arr[i]:
		temp += ord(c)-64
	total += (i+1)*temp
print(total)
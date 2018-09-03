from num2words import num2words
count = 0

for i in range(1,1001):
	count += len(num2words(i).replace("-","").replace(" ",""))
print(count)
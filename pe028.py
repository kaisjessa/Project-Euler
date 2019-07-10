'''
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

'''
def cycle(x):
	total = 0
	count = 0
	increment = 2
	i=1
	while(i <= x**2):
		total += i
		count += 1
		i += increment
		if count % 4 ==0:
			increment += 2
	return(total)

print(cycle(10))
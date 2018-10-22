'''Coins:
1
2
5
10
20
50
100
200
Number of ways to make 200 using other numbers
'''
count = 0
for a in range(200, -1, -200):
	for b in range(a, -1, -100):
		for c in range(b, -1, -50):
			for d in range(c, -1, -20):
				for e in range(d, -1, -10):
					for f in range(e, -1, -5):
						for g in range(f, -1, -2):
							count += 1
print(count)
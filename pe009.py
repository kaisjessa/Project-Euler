import math

for c in range(1000):
	for b in range(c):
		a = 1000 - c - b
		if(a**2 + b**2 == c**2):
			print(a*b*c)
			quit()
import math
import itertools
prime_list = [2]

def prime_generator(x):
	for test in range(3, x+1):
		is_prime = True
		for prime in prime_list:
			if(prime > math.sqrt(test)):
				break
			if(test%prime==0):
				is_prime = False
				break
		if(is_prime):
			prime_list.append(test)

def is_prime(x):
	if(x in prime_list):
		return True
	if(x<2):
		return False
	if(x==2):
		return True
	if(x%2==0):
		return False
	for i in range(3, math.ceil(math.sqrt(x))+1, 2):
		if x % i == 0:
			return False
	return True

def double_concat(a, b):
	return is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a)))
prime_generator(10000)


max_index = len(prime_list)
for a in range(max_index-4):
	p1 = prime_list[a]

	for b in range(a+1, max_index-3):
		p2 = prime_list[b]
		if(double_concat(p1, p2)):

			for c in range(b+1, max_index-2):
				p3 = prime_list[c]
				if(double_concat(p1, p3) and double_concat(p2, p3)):

					for d in range(c+1, max_index-1):
						p4 = prime_list[d]
						if(double_concat(p1, p4) and double_concat(p2, p4) and double_concat(p3, p4)):

							for e in range(d+1, max_index):
								p5 = prime_list[e]
								if(double_concat(p1, p5) and double_concat(p2, p5) and double_concat(p3, p5) and double_concat(p4, p5)):
									print(p1+p2+p3+p4+p5)
									quit()



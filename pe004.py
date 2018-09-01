import math
def isPalindrome(x):
	s = str(x)
	temp = int(math.floor(len(s)/2))
	return s[0:temp] == s[3:][::-1]

for n in range(999*999, 100*100-1, -1):
	if(isPalindrome(n)):
		i = 999
		for i in range(999, 99, -1):
			if(n % i == 0 and n/i>99 and n/i<1000):
				print(n)
				quit()
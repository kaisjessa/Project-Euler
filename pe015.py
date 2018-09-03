import math
'''
for an NxN grid, we must have exactly
N movements down and N movements right
The path is of length 2N
Out of 2N "slots", we must decide which of those are movements right
This means that the number of paths is 2N choose N
'''

def path_length(x):
	return(int(math.factorial(2*x)/(math.factorial(x)**2)))

print(path_length(20))

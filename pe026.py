import math
max_length = 0
find_d = 0

d = 2

def cycle_length(d):
	cycle = []
	remainders = []
	cycle.append(1)
	current_int = 1
	remainders.append(current_int)

	while(len(remainders)==len(set(remainders))):
		current_int = (10*current_int) % d
		remainders.append(current_int)
		cycle.append(math.floor(10*current_int/d))

	return(len(cycle)-1)


for d in range(2, 1000):
	if(cycle_length(d) > max_length):
		max_length = cycle_length(d)
		find_d = d
print(find_d, cycle_length(find_d))
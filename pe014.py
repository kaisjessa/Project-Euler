max_chain = 0
max_int = -1

def collatz(x,c):
	if(x==1):
		#print(c)
		return(c)
		quit()
	if(x % 2 == 0):
		return(collatz(x/2,c+1))
	if(x % 2 == 1):
		return(collatz(3*x+1,c+1))

for i in range(1, 1000000):
	temp = collatz(i,1)
	if(temp > max_chain):
		max_chain = temp
		max_int = i
print(max_int, max_chain)
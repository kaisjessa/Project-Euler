def reverse_digits(n):
	s = ""
	for i in range(len(str(n))-1, -1, -1):
		s += str(n)[i]
	return(s)

def is_palindromic(n):
	if(len(str(n)) % 2 == 0):
		return(str(n)[:int(len(str(n))/2)] == reverse_digits(str(n)[int(len(str(n))/2):]))
	else:
		return(str(n)[:int((len(str(n))-1)/2)] == reverse_digits(str(n)[int((len(str(n))-1)/2+1):]))


#for all numbers under 10000, it will become palindromic after 50 iterations or it is Lychrel
def lychrel(n):
	#assume lychrel for all numbers
	A = [True]*(n+1)

	for i in range(0, n+1):
		count = 0
		j = i
		#try to arrive at a palindrome within 50 iterations
		#if we arrive at a palindrome, i is not lychrel so A[i] becomes False
		while(count <= 50 and A[i]):
			count += 1
			temp = j + int(reverse_digits(j))
			if(is_palindromic(temp)):
				A[i] = False
			else:
				j = temp
	return(A.count(True))

print(lychrel(10000))


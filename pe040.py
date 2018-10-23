s = "".join(str(n) for n in range(1, 1000000))
prod = 1

ind = 1
while(ind <= 10**6):
	prod = prod * int(s[ind-1])
	ind = ind * 10
print(prod)
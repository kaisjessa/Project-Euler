count = 0
for i in range(10**6):
	bin_i = int("{0:b}".format(i))
	back_i = int(str(i)[::-1])
	back_bin_i = int(str(bin_i)[::-1])
	if(i==back_i and bin_i == back_bin_i):
		count += i
print(count)
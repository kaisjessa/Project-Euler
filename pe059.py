import string
# ^: XOR
# char -> ASCII: ord()
# ASCII -> char: chr()

alph = list(string.ascii_lowercase)
with open("p059_cipher.txt") as f:
	arr = [int(a) for a in f.readlines()[0].split(",")]
	f.close()


index = 0
chars = [0, 0, 0]
words = []

for i in range(0, len(arr), 3):
	temp = arr[i] ^ ord(alph[chars[0]])
	if not ((temp >= 32 and temp <= 90) or (temp >= 97 and temp <= 122)):
		chars[0] += 1
		i = 0
for i in range(1, len(arr), 3):
	temp = arr[i] ^ ord(alph[chars[1]])
	if not ((temp >= 32 and temp <= 90) or (temp >= 97 and temp <= 122)):
		chars[1] += 1
		i = 1
for i in range(2, len(arr), 3):
	temp = arr[i] ^ ord(alph[chars[2]])
	if not ((temp >= 32 and temp <= 90) or (temp >= 97 and temp <= 122)):
		chars[2] += 1
		i = 2	
total = 0
for k in range(len(arr)):
	words.append(chr(arr[k] ^ ord(alph[chars[k%3]])))
	total += arr[k] ^ ord(alph[chars[k%3]])
print(''.join(words))
print(total)
	
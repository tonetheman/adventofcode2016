
data = open("input.txt","r").readlines()

import string
data = map(string.strip,data)

letters = []
for i in range(26):
	letters.append(0)

def clear_letters():
	global letters
	for i in range(26):
		letters[i] = 0

for d in data:
	c = ord(d[0])-ord('a')
	letters[c] = letters[c] + 1

print letters

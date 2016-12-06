
data = open("input.txt","r").readlines()

import string
data = map(string.strip,data)

class Letters:
	def __init__(self):
		self.letters = []
		for i in range(26):
			self.letters.append(0)
	def __str__(self):
		return str(self.letters)
		
meta_letters = []
for i in range(8):
	meta_letters.append(Letters())

for d in data:
	index = 0
	for cc in d:
		meta_letters[index].letters[ord(cc)-ord('a')] = meta_letters[index].letters[ord(cc)-ord('a')] + 1
		index = index + 1


def find_max_index(letters):
	max_index = -1
	max_val = -1
	for i in range(len(letters)):
		if letters[i] > max_val:
			max_index = i
			max_val = letters[i]
	return (max_index, max_val)

def find_least_index(letters):
	target_index = -1
	least_val = 1000000
	for i in range(len(letters)):
		if letters[i] < least_val:
			target_index = i
			least_val = letters[i]
	return (target_index, least_val)

for l in meta_letters:
	(max_index,max_val) = find_least_index(l.letters)
	print max_index, max_val, chr(max_index+ord('a'))

	

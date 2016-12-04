
from collections import OrderedDict

data = open("data.txt","r").readlines()
import string
data = map(string.strip,data)

import re

def check_chksum(letters,chk):
	result = []
	for k in range(5):
		max = -1
		max_index = -1
		# find the max value from the list
		for i in range(len(letters)):
			if letters[i]>max:
				max_index = i
				max = letters[i]
		# find the first position the max happens
		for i in range(len(letters)):
			if letters[i] == max:
				max_index = i
				break
		# print "found max and max index first pos", max, max_index, chr(ord('a')+max_index)
		result.append(chr(ord('a')+max_index))
		# zero out the max and find the next letter
		letters[max_index] = 0
		max = -1
		max_index = -1
	print "result", result,chk
	res_s = "".join(result)
	return chk == res_s

def checkit(d):

	# break it up into room code and chksum
	P = re.compile("([a-zA-Z-]+)([0-9]+)\[([a-zA-Z0-9]+)\]")
	m = P.search(d)
	code = m.group(1)
	sector_id = m.group(2)
	chk = m.group(3)

	# replace the - in the code
	code = code.replace("-","")
	code = re.sub("[0-9]","",code)

	code = "".join(sorted(code))

	letters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	for c in code:
		pos = ord(c)-ord('a')
		letters[pos] = letters[pos] + 1

	matches = check_chksum(letters,chk)

	if matches:
		return int(sector_id)
	else:
		return 0

def test():
	sum = 0
	sum = sum + checkit("aaaaa-bbb-z-y-x-123[abxyz]")
	sum = sum + checkit("a-b-c-d-e-f-g-h-987[abcde]")
	sum = sum + checkit("not-a-real-room-404[oarel]")
	sum = sum + checkit("totally-real-room-200[decoy]")
	print sum

sumit = 0
for d in data:
 	sumit = sumit + checkit(d)

print sumit


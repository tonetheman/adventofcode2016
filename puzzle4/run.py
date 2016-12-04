
from collections import OrderedDict

data = open("data.txt","r").readlines()
import string
data = map(string.strip,data)

import re

def checkit(d):

	P = re.compile("([a-zA-Z0-9-]+)\[([a-zA-Z0-9]+)\]")
	m = P.search(d)
	code = m.group(1)
	chk = m.group(2)

	# replace the - in the code
	code = code.replace("-","")

	code = "".join(sorted(code))

	code = re.sub("[0-9]","",code)
	counts = {}
	for c in code:
		if counts.has_key(c):
			counts[c] = counts[c] + 1
		else:
			counts[c] = 1

	# ocount = OrderedDict(sorted(counts.items(), key=lambda t: t[1]))
	
	print code, chk, ocount.keys()

checkit("aaaaa-bbb-z-y-x-123[abxyz]")
checkit("totally-real-room-200[decoy]")
checkit("not-a-real-room-404[oarel]")

# for d in data:
# 	checkit(d)

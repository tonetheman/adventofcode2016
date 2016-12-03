
data = open("input3.txt","r").readlines()

import string

data = map(string.strip,data)

count = 0

def check(d):
	global count

	d = d.split()
	d = map(int,d)
	print d

	good = True
	if d[0] + d[1] > d[2]:
		print "ok"
	else:
		good = False
	if d[1]+d[2] > d[0]:
		print "ok"
	else:
		good = False
	if d[0]+d[2] > d[1]:
		print "ok"
	else:
		good = False


	if good == False:
		pass
	else:
		count = count + 1

for d in data:
	check(d)

print count


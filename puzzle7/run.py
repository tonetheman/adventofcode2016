
import re

# 2 char palindrome matcher
P = re.compile(r"(.)(.)(\2)(\1)")

# used to split out the bracketed groups
PB = re.compile(r"\[.*?\]")

# used to match the brackets
PB2 = re.compile(r"\[(.*?)\]")

def support(s):
	res = False

	# a will hold stuff not in brackets
	a = PB.split(s)
	# find all the brackets
	b = PB.findall(s)
	c = []
	for tmp  in b:
		tmpd = PB2.findall(tmp)
		if len(tmpd)==0:
			continue
		# save off just the data from the brackets
		c.append(tmpd[0])

	# stuff not in brackets
	for ts in a:
		td = P.findall(ts)
		# did not find anything
		if len(td)==0:
			continue
		# eliminate not valid char 1 must be diff from char 2
		if td[0][0]==td[0][1]:
			continue
		res = True

	# stuff that was in the brackets
	for ts in c:
		td = P.findall(ts)
		if len(td) == 0:
			continue
		res = False

	"""
	print "orig",s
	print "not brackets",a
	print "brackets",b
	print "bracket data",c
	print
	"""
	print s,res

	return res

"""
support("abba[mnop]qrst")
support("abcd[bddb]xyyx")
support("aaaa[qwer]tyui")
support("ioxxoj[asdfgh]zxcvbn")
support("tony[is]really[cool]")
"""

data = open("input.txt","r").readlines()
import string
data = map(string.strip,data)

count = 0
for d in data:
	if support(d):
		count = count + 1
print count


import re

def supportTLS(s):
	P = re.compile(r"(.)(.)(\2)(\1)")
	B = re.compile(r"\[.*?\]")

	not_brackets = B.split(s)
	try:
		not_brackets.remove('')
	except ValueError:
		pass

	did_we_find_PAL = False
	for ts in not_brackets:
		m = P.search(ts)
		if m is None:
			continue
		match_value = m.group(0)
		if match_value[0] == match_value[1]:
			continue
		did_we_find_PAL = True

	find_PAL_in_brackets = False
	brackets = B.findall(s)
	for ts in brackets:
		ts=ts[1:-1]
		m = P.search(ts)
		if m is None:
			continue
		match_value = m.group(0)
		if match_value[0] == match_value[1]:
			continue
		find_PAL_in_brackets = True
		# print ts, m.group(0)

	if did_we_find_PAL:
		if find_PAL_in_brackets:
			return False
		else:
			return True
	else:
		return False

"""
print supportTLS("abba[mnop]qrst")
print supportTLS("abcd[bddb]xyyx")
print supportTLS("aaaa[qwer]tyui")
print supportTLS("ioxxoj[asdfgh]zxcvbn")
print supportTLS("tony[is]really[cool]")
"""

data = open("input.txt","r").readlines()
import string
data = map(string.strip,data)

count = 0
for d in data:
	if supportTLS(d):
		count = count + 1
print count

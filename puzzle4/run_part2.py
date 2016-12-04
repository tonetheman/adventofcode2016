
def decrypt(d):
	import re
	P = re.compile("([a-zA-Z-]+)([0-9]+)\[([a-zA-Z0-9]+)\]")
	m = P.search(d)
	
	code = m.group(1)
	sector_id = m.group(2)
	chk = m.group(3)

	res = []
	for c in code:
		if c == "-":
			# print ""
			res.append(" ")
			continue
		val_c = ord(c)
		a = ord(c)-ord('a')
		aa = a + int(sector_id)
		aaa = aa % 26
		aaaa = chr(ord('a') + aaa)
		# print c,val_c,a,aa,aaa,aaaa
		res.append(aaaa)

	return res


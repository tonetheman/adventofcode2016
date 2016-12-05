
import hashlib

passwd = "reyedfim"

res = [-1,-1,-1,-1,-1,-1,-1,-1]

i = 0
while True:
	m = hashlib.md5()
	m.update(passwd)
	m.update(str(i))
	h =  m.hexdigest()
	i = i + 1
	if h.startswith("00000"):
		pos = h[5]
		digit = h[6]
		pos = int(pos,16)
		if pos>7:
			continue
		print h, pos, digit, res
		if res[pos] == -1:
			res[pos] = digit

	notdone = False
	for idx in res:
		if idx == -1:
			notdone = True

	if notdone == False:
		break

print "final", res, "".join(res)

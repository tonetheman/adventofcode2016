
import hashlib

passwd = "reyedfim"

for i in range(5278568*2):
	m = hashlib.md5()
	m.update(passwd)
	m.update(str(i))
	h =  m.hexdigest()
	if h.startswith("00000"):
		key = passwd + str(i)
		print h,i,key, h[5]


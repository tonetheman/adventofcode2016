
data = open("input.txt","r").readlines()
import string
data=map(string.strip,data)

def onlydev(s):
	if s.startswith("/dev"):
		return True
	return False

def cvt_t(s):
	return int(s[0:-1])

data = filter(onlydev,data)
data = map(string.split,data)
viable_count = 0
for d1 in data:
	for d2 in data:
		if d1[0]!=d2[0]:
			# nodes are not the same
			
			used = cvt_t(d1[2])
			if used != 0:
				# used is not zero

				avail = cvt_t(d2[3])

				if used<avail:
					# used is less than avail
					# we have a viable pair!

					viable_count = viable_count + 1
					print d1[0],d2[0]

print "viable_count", viable_count


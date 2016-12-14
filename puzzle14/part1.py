
import md5


pc = []

def contains_triple(s):
	# print len(s)
	# print s
	for i in range(30):
		# print s[i],s[i+1],s[i+2]
		if s[i] == s[i+1] and s[i+1] == s[i+2]:
			return (True,s[i])
	return (False,None)

def contains_quint(s):
	for i in range(28):
		a = s[i]
		b = s[i+1]
		c = s[i+2]
		d = s[i+3]
		e = s[i+4]
		if a==b and b==c and c==d and d==e:
			return (True,a)
	return (False,None)

class Digest:
	def __init__(self,digest,matched_char,position):
		self.digest = digest
		self.matched_char = matched_char
		self.position = position
		self.position_target = position + 1000
	def __str__(self):
		return "{} {} {} {}".format(self.digest,self.matched_char,self.position,self.position_target)
	def check(self, current_index, other_digest, other_matched_char):
		if other_digest == self.digest:
			return False
		if other_matched_char != self.matched_char:
			print "SKIPPING not a possible match", self.digest, other_digest
			return False

		print "NEED TO CHECK FURTHER COULD MATCH", current_index, self.position_target, self.matched_char, self.digest, other_digest


		return False


SALT = "abc"

count = 0

while True:
	h = md5.new()
	h.update(SALT)
	h.update(str(count))

	digest = h.hexdigest()
	(res,matched_char) = contains_triple(digest)
	if res:
		pc.append(Digest(digest,matched_char,count))

		# now we found at least a triple check against other PC choices
		for tmp_pc in pc:
			tmp_pc.check(count, digest, matched_char)


	count = count + 1
	if count > 1040:
		break


# for match in pc:
#	print match



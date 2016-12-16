

def make_more(input):
	a = input
	b = a
	b = b[::-1]

	def switcher(c):
		if c == "0":
			return "1"
		elif c == "1":
			return "0"

	b = map(switcher,b)

	res = a + "0" + "".join(b)
	return res


def test():
	print make_more("1")
	print make_more("0")
	print make_more("11111")
	print make_more("111100001010")


def chk_single(s):
	if len(s)%2 != 0:
		print "INVALID MUST BE EVEN"
		return

	# pair wise check


input = "11110010111001001"

while len(input)<272:
	input = make_more(input)

print "final input", input




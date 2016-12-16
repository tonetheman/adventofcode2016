

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


def chksum(s):

	import itertools

	def pairwise(iterable):
		a = iter(iterable)
		return itertools.izip(a, a)


	while len(s)%2==0:
		res = []

		for a,b in pairwise(s):
			if a == b:
				res.append("1")
			else:
				res.append("0")

		s = "".join(res)

	print "DONE", s
	return s

def test_chksum():
	s = "110010110100"
	chksum(s)

def part1():
	input = "11110010111001001"

	while len(input)<272:
		input = make_more(input)

	input = input[0:272]
	print "final input", input,len(input)
	chksum(input)


part1()

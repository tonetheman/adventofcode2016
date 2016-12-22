import re, collections

P0 = re.compile("rotate (right|left) (\d+) steps")
P1 = re.compile("swap position (\d+) with position (\d+)")
P2 = re.compile("reverse positions (\d+) through (\d+)")
P3 = re.compile("move position (\d+) to position (\d+)")
P4 = re.compile("rotate based on position of letter ([a-z])")
P5 = re.compile("swap letter ([a-z]) with letter ([a-z])")
P6 = re.compile("rotate (left|right) (\d+) step")

data = open("input.xt","r").readlines()
import string
data = map(string.strip,data)

def handle_pattern_0(d,inp):
	m = P0.search(d)
	if m is None:
		return (False,None)
	direction = m.group(1)
	count = m.group(2)
	if direction=="right":
		d = collections.deque(inp)
		d.rotate(int(count))
	elif direction == "left":
		d = collections.deque(inp)
		d.rotate(-1 * int(count))
	return (True, "".join(list(d)))

def handle_pattern_1(d,inp):
	m = P1.search(d)
	if m is None:
		return (False,None)
	position1 = m.group(1)
	position2 = m.group(2)
	outp = []
	for i in inp:
		outp.append(i)
	
	tmp1 = outp[int(position1)]
	tmp2 = outp[int(position2)]
	outp[int(position1)] = tmp2
	outp[int(position2)] = tmp1
	return (True,"".join(outp))

def handle_pattern_2(d,inp):
	m = P2.search(d)
	if m is None:
		return (False,None)
	# reverse positions X through Y
	pos1 = int(m.group(1))
	pos2 = int(m.group(2))

	outp = []
	for i in inp:
		outp.append(i)

	r_part = outp[pos1:pos2+1]
	r_part.reverse()

	index = 0
	for i in range(pos1,pos2+1):
		outp[i] = r_part[index]
		index  = index + 1

	return (True,"".join(outp))

def handle_pattern_3(d,inp):
	m = P3.search(d)
	if m is None:
		return (False,None)

	# move letter in pos1
	# to index pos4
	pos1 = int(m.group(1))
	pos2 = int(m.group(2))

	outp = []
	for i in inp:
		outp.append(i)

	tmp1 = outp[pos1]
	del outp[pos1]

	outp.insert(pos2,tmp1)

	return (True,"".join(outp))

def handle_pattern_4(d,inp):
	m = P4.search(d)
	if m is None:
		return (False,None)
	# 
	# 
	letter = m.group(1)

	index = inp.find(letter)
	# print "index is", index
	if index>=4:
		index = index + 1

	d = collections.deque(inp)
	d.rotate(1+index)

	return (True,"".join(list(d)))

def handle_pattern_5(d,inp):
	# swaps letters
	# no matter the position
	m = P5.search(d)
	if m is None:
		return (False,None)
	letter1 = m.group(1)
	letter2 = m.group(2)
	outp = []
	for i in inp:
		if i == letter1:
			outp.append(letter2)
		elif i == letter2:
			outp.append(letter1)
		else:
			outp.append(i)
	return (True,"".join(outp))

def handle_pattern_6(d,inp):
	m = P6.search(d)
	if m is None:
		return (False,None)
	direction = m.group(1)
	count = m.group(2)
	if direction=="right":
		d = collections.deque(inp)
		d.rotate(int(count))
	elif direction == "left":
		d = collections.deque(inp)
		d.rotate(-1 * int(count))
	return (True, "".join(list(d)))


s="abcde"

def perform_single_step(d,inp):
	(res,res2) = handle_pattern_0(d,inp)
	if res:
		return res2
	(res,res2) = handle_pattern_1(d,inp)
	if res:
		return res2
	(res,res2) = handle_pattern_2(d,inp)
	if res:
		return res2
	(res,res2) = handle_pattern_3(d,inp)
	if res:
		return res2
	(res,res2) = handle_pattern_4(d,inp)
	if res:
		return res2
	(res,res2) = handle_pattern_5(d,inp)
	if res:
		return res2
	(res,res2) = handle_pattern_6(d,inp)
	if res:
		return res2

	print "ERR: did not handle input!"

def test():
	s = "abcde"
	new_s = perform_single_step("swap position 4 with position 0", s)
	print s, new_s
	s = new_s
	new_s = perform_single_step("swap letter d with letter b",s)
	print s,new_s
	s = new_s
	new_s = perform_single_step("reverse positions 0 through 4",s)
	print s, new_s
	s = new_s
	new_s = perform_single_step("rotate left 1 step",s)
	print s, new_s
	s = new_s
	new_s = perform_single_step("move position 1 to position 4",s)
	print s, new_s
	s = new_s
	new_s = perform_single_step("move position 3 to position 0",s)
	print s, new_s
	s = new_s
	new_s = perform_single_step("rotate based on position of letter b",s)
	print s, new_s
	s = new_s
	new_s = perform_single_step("rotate based on position of letter d",s)
	print s, new_s

# test()

def run_part1():
	data = open("input.xt","r").readlines()
	import string
	data = map(string.strip,data)
	s = "abcdefgh"
	for d in data:
		new_s = perform_single_step(d,s)
		s = new_s
	print "final",s

	# result here: gcedfahb

# run_part1()








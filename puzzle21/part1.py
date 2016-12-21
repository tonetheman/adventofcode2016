import re

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
	import collections
	m = P0.search(d)
	if m is None:
		return (False,None)
	direction = m.group(1)
	count = m.group(2)
	print "p0 match", direction, count
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
	print "p1 match", position1, position2
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

def handle_pattern_3(d):
	m = P3.search(d)
	if m is None:
		return (False,None)
	pos1 = m.group(1)
	pos2 = m.group(2)
	return (True,None)

def handle_pattern_4(d):
	m = P4.search(d)
	if m is None:
		return (False,None)
	letter = m.group(1)
	return (True,None)

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

def handle_pattern_6(d):
	m = P6.search(d)
	if m is None:
		return (False,None)
	return (True,None)

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
	(res,res2) = handle_pattern_3(d)
	if res:
		return
	(res,res2) = handle_pattern_4(d)
	if res:
		return
	(res,res2) = handle_pattern_5(d,inp)
	if res:
		return res2
	(res,res2) = handle_pattern_6(d)
	if res:
		return

	print "ERR: did not handle input!"

s = "abcde"
new_s = perform_single_step("swap position 4 with position 0", s)
print s, new_s
s = new_s
new_s = perform_single_step("swap letter d with letter b",s)
print s,new_s
s = new_s
new_s = perform_single_step("reverse positions 0 through 4",s)
print s, new_s



import string

def solve(s):
	x = 0
	y = 0
	cdir = 0

	positions = {}

	data = s.split(",")
	data = map(string.strip,data)
	for d in data:
		direction = d[0]
		steps = int(d[1:])

		if direction == "R":
			cdir = cdir + 1
		elif direction == "L":
			cdir = cdir - 1
		cdir = cdir%4

		if cdir == 0:
			for i in range(steps):
				y = y  + 1
				if positions.has_key((x,y)):
					print "found it", d, x,y, abs(x) + abs(y)
				else:
					positions[(x,y)] = 1
					print "i am here",d,x,y,abs(x)+abs(y)
		elif cdir == 1:
			for i in range(steps):
				x = x + 1
				if positions.has_key((x,y)):
					print "found it", d, x,y, abs(x) + abs(y)
				else:
					positions[(x,y)] = 1
					print "i am here",d,x,y,abs(x)+abs(y)
		elif cdir == 2:
			for i in range(steps):
				y = y - 1
				if positions.has_key((x,y)):
					print "found it",d,x,y,abs(x) + abs(y)
				else:
					positions[(x,y)] = 1
					print "i am here",d,x,y,abs(x)+abs(y)
		elif cdir == 3:
			for i in range(steps):
				x = x - 1
				if positions.has_key((x,y)):
					print "found it",d,x,y,abs(x) + abs(y)
				else:
					positions[(x,y)] = 1
					print "i am here",d,x,y,abs(x)+abs(y)

	print x,y, abs(x) + abs(y)

def test():
	solve("R2,L3")
	solve("R2,R2,R2")
	solve("R5,L5,R5,R3")

solve("L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4")
# solve("R8,R4,R4,R8")

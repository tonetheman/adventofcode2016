
import string

def solve(s):
	x = 0
	y = 0
	cdir = 0

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
			# north
			y = y + steps
		elif cdir == 1:
			x = x + steps
		elif cdir == 2:
			y = y - steps
		elif cdir == 3:
			x = x - steps
		

	print x,y, abs(x) + abs(y)

	
solve("R2,L3")
solve("R2,R2,R2")
solve("R5,L5,R5,R3")

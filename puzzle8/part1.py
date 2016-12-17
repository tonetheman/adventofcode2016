
EMPTY = "."

class Board:
	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols

		# python list of lists for 2d array
		self.b = []
		for i in range(self.rows):
			tmp = []
			for j in range(self.cols):
				tmp.append(EMPTY)
			self.b.append(tmp)

	def set_row(self,row,val):
		for i in range(self.cols):
			self.set(row,i,val)
	def clear_row(self,row):
		self.set_row(row,EMPTY)
	def get(self,row,col):
		return self.b[row][col]
	def set(self,row,col,val):
		self.b[row][col] = val

	def shift_row_right(self,row):
		tmp = []
		for i in range(self.cols):
			tmp.append(self.get(row,i))
		end_ = tmp[-1]
		tmp = tmp[0:-1]
		tmp.insert(0,end_)
		for i in range(self.cols):
			self.set(row,i,tmp[i])
	def shift_row_left(self,row):
		tmp = []
		for i in range(self.cols):
			tmp.append(self.get(row,i))
		start = tmp[0]
		tmp = tmp[1:]
		tmp.append(start)
		for i in range(self.cols):
			self.set(row,i,tmp[i])

	def shift_col_down(self,col):
		tmp = []
		for i in range(self.rows):
			tmp.append(self.get(i,col))
		end_ = tmp[-1]
		tmp = tmp[0:-1]
		tmp.insert(0,end_)
		for i in range(self.rows):
			self.set(i,col,tmp[i])
	def shift_col_up(self,col):
		tmp = []
		for i in range(self.rows):
			tmp.append(self.get(i,col))
		start = tmp[0]
		tmp = tmp[1:]
		tmp.append(start)
		for i in range(self.rows):
			self.set(i,col,tmp[i])

	def p(self):
		return str(self.b)
	def __str__(self):
		ts = ""
		for i in range(self.rows):
			ts = ts + str(self.b[i]) + "\n"
		return ts

	def count_lit_pixels(self):
		count = 0
		for i in range(self.rows):
			for j in range(self.cols):
				v = self.get(i,j)
				if v == "#":
					count = count + 1
		return count

	def rect(self,a,b):
		# a wide
		# b tall
		for col_idx in range(a):
			for row_idx in range(b):
				self.set(row_idx,col_idx,"#")

	def rotate_row(self,y,b):
		for i in range(b):
			self.shift_row_right(y)

	def rotate_col(self,x,b):
		for i in range(b):
			self.shift_col_down(x)

	def parse_single(self,s):
		import re
		P_RECT = re.compile("rect\s+(\d+)x(\d+)$")
		m  = P_RECT.match(s)
		if m is not None:
			a = int(m.group(1))
			b = int(m.group(2))

			self.rect(a,b)

			return

		P_ROT_ROW = re.compile("rotate row y=(\d+)\s+by\s+(\d+)$")
		m = P_ROT_ROW.match(s)
		if m is not None:
			a = int(m.group(1))
			b = int(m.group(2))

			self.rotate_row(a,b)

			return

		P_ROT_COL = re.compile("rotate column x=(\d+)\s+by\s+(\d+)$")
		m = P_ROT_COL.match(s)
		if m is not None:
			a = int(m.group(1))
			b = int(m.group(2))

			self.rotate_col(a,b)

			return

		print "not handled", s


def test():
	b = Board(3,7)
	b.rect(3,2)
	b.rotate_col(1,1)
	b.rotate_row(0,4)
	b.rotate_col(1,1)
	print b


def part1():
	b = Board(6,50)

	data = open("input.txt","r").readlines()
	import string
	data = map(string.strip,data)

	for d in data:
		b.parse_single(d)

	print b
	print b.count_lit_pixels()

part1()

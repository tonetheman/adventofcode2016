
class Board:
	def __init__(self):
		self.row = 1 
		self.col = 1
		self.b = [1,2,3,4,5,6,7,8,9]
		self.ROWS = 3
		self.COLS = 3
	def up(self):
		if self.row==0:
			return
		self.row = self.row - 1
	def down(self):
		if self.row==self.ROWS-1:
			return
		self.row = self.row + 1
	def left(self):
		if self.col==0:
			return
		self.col = self.col -1
	def right(self):
		if self.col==self.COLS-1:
			return
		self.col = self.col + 1
	def val(self):
		idx = self.row*self.ROWS+self.col
		return self.b[idx]
	def read(self,s):
		m = { "U" : self.up, "D" : self.down, "L" : self.left, "R" : self.right }
		for c in s:
			m[c]()	
	def __str__(self):
		return str(self.row) + ", " + str(self.col) + " --> " + str(self.val())

b = Board()
b.read("ULL")
print b
b.read("RRDDD")
print b
b.read("LURDL")
print b
b.read("UUUUD")
print b






class Board:
	def __init__(self):
		self.board = [[1,2,3],[4,5,6],[7,8,9]]
		self.row = 1
		self.col = 1
	def __str__(self):
		return str(self.row) + ", " + str(self.col) + " --> " + str(self.board[self.row][self.col])
	def up(self):
		if self.row == 0:
			return
		self.row = self.row-1
	def down(self):
		if self.row == 2:
			return
		self.row = self.row +1
	def left(self):
		if self.col == 0:
			return
		self.col = self.col - 1
	def right(self):
		if self.col == 2:
			return
		self.col = self.col + 1
	def read(self,s):
		for c in s:
			if c == "U":
				self.up()	
			elif c == "L":
				self.left()
			elif c == "R":
				self.right()
			elif c == "D":
				self.down()
			print "DBG:", c, self.__str__(),self.board[self.row][self.col]

		return self.board[self.row][self.col]

b = Board()
# print "starting", b
# print b.read("U")
print b.read("ULL")
print b.read("RRDDD")
print b.read("LURDL")
print b.read("UUUUD")



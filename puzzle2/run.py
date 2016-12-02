

class Board:
	def __init__(self):
		self.board = [1,2,3,4,5,6,7,8,9]
		self.pos = self._pos(1,1)
		self.x = 1
		self.y = 1
	def _pos(self,x,y):
		return x*3 + y
	def __str__(self):
		return str(self.pos) + " -> " + str(self.x) + ", " + str(self.y)
	def up(self):
		if self.y == 0:
			return
		self.y = self.y-1
	def down(self):
		if self.y == 2:
			return
		self.y = self.y +1
	def left(self):
		if self.x == 0:
			return
		self.x = self.x - 1
	def right(self):
		if self.x == 2:
			return
		self.x = self.x + 1
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
			print "DBG:", c, self.__str__(),self.board[self._pos(self.x,self.y)]

		return self.board[self._pos(self.x,self.y)]

b = Board()
print b.read("ULL")
print b.read("RRDDD")
print b.read("LURDL")
print b.read("UUUUD")



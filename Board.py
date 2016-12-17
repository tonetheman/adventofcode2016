
EMPTY = 0

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

b = Board(3,3)
b.set(0,0,1)
b.set(0,1,2)
b.set(1,1,5)
print b
b.shift_row_right(0)
print "shifted..."
print b
b.shift_row_left(0)
print "back..."
print b
b.shift_col_down(1)
print "shift 1 down..."
print b
print "shift 1 up..."
b.shift_col_up(1)
print b


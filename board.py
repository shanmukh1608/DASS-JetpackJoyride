import subprocess

def pos(x, y):
	return '\x1b[%d;%dH' % (y, x)

class board:


	def __init__(self, rows, columns):
		self._rows = rows
		self._columns = columns
		self._matrix = []

	def create_board(self):
		for i in range(self._rows):
			self.new = []
			for j in range(self._columns):
				self.new.append(" ")
			self._matrix.append(self.new)
	
	def printboard(self):
		for i in range(self._rows):
			for j in range(self._columns):
				print('%s%s' % (pos(j, i), self._matrix[i][j]), end='')
				# print(self._matrix[i][j], end='')
			print("")
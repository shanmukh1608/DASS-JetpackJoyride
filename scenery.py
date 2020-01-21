import random
# init()

class Scenery:

	def __init__(self):
		self._sky = "X"
		self._ground1 = "T"

	def create_ground(self, board):
		for i in range(board._columns):
			board._matrix[board._rows-2][i] = self._ground1
			board._matrix[board._rows-1][i] = "-"

	def create_sky(self, board):
		for i in range(board._columns):
			board._matrix[2][i] = self._sky

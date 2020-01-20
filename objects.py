from entity import entity
import random

class coins(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._len = 0
		self._width = 0
		self._mat = ["O"]

class lasers(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._orientation = random.randint(0, 2)

		if (self._orientation == 0):
			self._mat = ['|', '|', '|', '|']
			self._len = 3
			self._width = 0
		elif (self._orientation == 1):
			self._mat = ['----']
			self._len = 0
			self._width = 3
		else:
			self._mat = ['\\', ' \\', '  \\', '   \\']
			self._len = 3
			self._width = 4
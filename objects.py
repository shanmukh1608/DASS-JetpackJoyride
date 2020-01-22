from entity import entity
import random

class coins(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._len = 1
		self._width = 1
		self._mat = ["©©", "©©"]

class magnets(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._len = 4
		self._width = 8
		self._mat = \
		[" OOOOOOO ",
		"OOO   OOO",
		"OOO   OOO",
		" OOO OOO ",
		"OOOO OOOO"]

class bullets(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._len = 0
		self._width = 1
		self._mat = [">>"]

class snowballs(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._len = 0
		self._width = 2
		self._mat = ["@@"]

class lasers(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._orientation = random.randint(0, 2)

		if (self._orientation == 0):
			self._mat = ['|', '|', '|', '|', '|']
			self._len = 4
			self._width = 0
		elif (self._orientation == 1):
			self._mat = ['-------']
			self._len = 0
			self._width = 6
		else:
			self._mat = ['\\', ' \\', '  \\', '   \\', '    \\']
			self._len = 4
			self._width = 5

class speedup(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._len = 2
		self._width = 2
		self._mat = ['PP', 'PP']

		
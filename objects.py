from entity import entity

class coins(entity):
	def __init__(self, x, y, lent, wid):
		super().__init__(x, y, lent, wid)
		self._mat = ["O"]

class laser1(entity):
	def __init__(self, x, y, lent, wid):
		super().__init__(x, y, lent, wid)
		self._mat = ['|', '|', '|', '|']

class laser2(entity):
	def __init__(self, x, y, lent, wid):
		super().__init__(x, y, lent, wid)
		self._mat = ['----']\

class laser3(entity):
	def __init__(self, x, y, lent, wid):
		super().__init__(x, y, lent, wid)
		self._mat = ['\\', ' \\', '  \\', '   \\']

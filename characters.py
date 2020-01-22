from entity import entity
import time
import globalobjects
from globalobjects import obj_Board as board

class mando(entity):

	def __init__(self, x, y):
		super().__init__(x, y)
		self._mat = \
   		['__.-._ ', 
		'\'-._"7\'', 
		" /'.-c ", 
		' |  /T ', 
		'_)_/LI ']

		# self._shieldMat = \
		# ['S__.-._ S', 
		# 'S\'-._"7\'S', 
		# "S /'.-c S", 
		# 'S |  /T S', 
		# 'S_)_/LI S']

		self._shieldMat = \
   		['S_.-._S', 
		'S-._"7S', 
		"S/'.-cS", 
		'S|  /TS', 
		'S)_/LIS']

		self._len = 6
		self._width = 4

	def moveUp(self, x):
		if self._x - x > 2:
			if globalobjects.shieldActive == False:
				self.updateBoard(self._mat, )
				self._x = self._x - x
				self.updateBoard(self._mat, "put")
			else:
				self.updateBoard(self._shieldMat, )
				self._x = self._x - x
				self.updateBoard(self._shieldMat, "put")

	def moveDown(self, x):
		if self._x + x < board._rows - 6:
			if globalobjects.shieldActive == False:
				self.updateBoard(self._mat, )
				self._x = self._x + x
				self.updateBoard(self._mat, "put")
			else:
				self.updateBoard(self._shieldMat, )
				self._x = self._x + x
				self.updateBoard(self._shieldMat, "put")

	def moveLeft(self, y):
		if (self._y - y > 0):
			if globalobjects.shieldActive == False:
				self.updateBoard(self._mat, )
				self._y = self._y - y
				self.updateBoard(self._mat, "put")
			else:
				self.updateBoard(self._shieldMat, )
				self._y = self._y - y
				self.updateBoard(self._shieldMat, "put")

	def moveRight(self, y):
		if (self._y + y < board._columns):
			if globalobjects.shieldActive == False:
				self.updateBoard(self._mat, )
				self._y = self._y + y
				self.updateBoard(self._mat, "put")
			else:
				self.updateBoard(self._shieldMat, )
				self._y = self._y + y
				self.updateBoard(self._shieldMat, "put")

	def gravity(self):
		# displacement = (2*int(globalobjects.g_timer-time.time()) + 1)
		# self.moveDown(displacement)
		self.moveDown(1)
		# print(displacement)

		# if (g_timer < 3):
			# self.moveDown(g_timer)
		# else:
			# self.moveDown(2)

# class dragon(entity):

#         self._mat = \
#    ["         .---.               ",
#    "       .'___`.               ",
#    "       |xxxxx|               ",  
#    "       |_  #  _|             ",
#    "  .------`-#-'-----.         ",
#    " (_|\____/|.`                ",
#    "(  --< |\/    \//| |         ", 
#    "`.    ----.-=====,:========  ",
#    " ~-.__/_:_(``/|              ",
#    "    \__/======| /|           ",
#    "    |\|\    /|/|             ",
#    "    |_   \__/   _|           ",
#    "    |  `'|  |`'  |           ",
#    "    |    |  |    |           "]
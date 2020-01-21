from entity import entity
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

		self._len = 6
		self._width = 4

	def moveUp(self, x):
		if self._x - x > 2:
		   self.updateBoard(self._mat, )
		   self._x = self._x - x
		   self.updateBoard(self._mat, "put")

	def moveDown(self, x):
		if self._x + x < board._rows - 6:
			self.updateBoard(self._mat, )
			self._x = self._x + x
			self.updateBoard(self._mat, "put")

	def gravity(self, g_timer):
		self.moveDown(1)
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
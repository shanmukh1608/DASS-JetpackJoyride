from entity import entity

class mando(entity):

	def __init__(self, x, y, lent, wid):
		super().__init__(x, y, lent, wid)
		self._mat = \
   ["         .---.               ",
   "       .'___`.               ",
   "       |xxxxx|               ",  
   "       |_  #  _|             ",
   "  .------`-#-'-----.         ",
   " (_|\____/|.`                ",
   "(  --< |\/    \//| |         ", 
   "`.    ----.-=====,:========  ",
   " ~-.__/_:_(``/|              ",
   "    \__/======| /|           ",
   "    |\|\    /|/|             ",
   "    |_   \__/   _|           ",
   "    |  `'|  |`'  |           ",
   "    |    |  |    |           "]

	def moveUp(self, x):
		if self._x - x > 1:
		   self.putOnBoard(self._mat, )
		   self._x = self._x - x
		   self.putOnBoard(self._mat, "put")

# class dragon(entity):

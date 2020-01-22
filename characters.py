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
		if (self._y - y > 0 and self._y - y < board._columns):
			if globalobjects.shieldActive == False:
				self.updateBoard(self._mat, )
				self._y = self._y - y
				self.updateBoard(self._mat, "put")
			else:
				self.updateBoard(self._shieldMat, )
				self._y = self._y - y
				self.updateBoard(self._shieldMat, "put")

	def moveRight(self, y):
		if (self._y + y > 0 and self._y + y < board._columns):
			if globalobjects.shieldActive == False:
				self.updateBoard(self._mat, )
				self._y = self._y + y
				self.updateBoard(self._mat, "put")
			else:
				self.updateBoard(self._shieldMat, )
				self._y = self._y + y
				self.updateBoard(self._shieldMat, "put")

	def gravity(self):
		displacement = (min(10, 2*int(time.time()-globalobjects.g_timer) + 1))
		self.moveDown(displacement)
		# self.moveDown(1)
		# print(displacement)

		# if (g_timer < 3):
			# self.moveDown(g_timer)
		# else:
			# self.moveDown(2)

class dragon(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._mat = \
		["\_|  \\      // | \_/",
		"  \|\/|\_   //  /\/  ",
		"   (oo)\ \_//  /     ",
		"  //_/\_\/ /  |      ",
		" @@/  |=\  \  |      ",
		"      \_=\_ \ |      ",
		"        \==\ \|\_    ",
		"     __(\===\(  )\   ",
		"    (((~) __(_/   |  ",
		"         (((~) \  /  ",
		"         ______/ /   ",
		"         '------'    "]

		self._width = 20
		self._len = 11


	def setX(self, x):
		self._x = x
		if (self._x <= 5):
			self._x = 6
		if ( x >= board._rows - 14):
			x = board._rows - 14

class babyyoda(entity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._initialmat = \
["	              _.' :  `._				  ",
"             .-.'`.  ;   .'`.-.		  ",
"    __      / : ___\ ;  /___ ; \      __  ",
"  ,'_ \"\"--.:__;\".-.\";: :\".-.\":__;.--\"\" _`,",
"  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;",
"       `:-.._J '-.-'L__ `-- ' L_..-;'",
"         \"-.__ ;  .-\"  \"-.  : __.-\"",
"             L ' /.------.\ ' J",
"              \"-.   \"--\"   .-\"",
"             __.l\"-:_JL_;-\";.__",
"          .-j/'.;  ;\"\"\"\"  / .'\"-.",
"       .' /:`. \"-.:     .-\" .';  `.",
"    .-\"  / ;  \"-. \"-..-\" .-\"  :    \"-.			GOOD LUCK FROM YODA!",
" .+\"-.  : :      \"-.__.-\"      ;-._   \ ",
" ; \  `.; ;                    : : \"+. ;",
" :  ;   ; ;                    : ;  : \:",
" : `.\"-; ;  ;                  :  ;   ,/;",
" ;    -: ;  :                ;  : .-\"'  :",
" :\     \  : ;             : \.-\"      :",
"  ;`.    \  ; :            ;.'_..--  / ;",
"  :  \"-.  \"-:  ;          :/.\"      .'  :",
"    \       .-`.\        /t-\"\"  \":-+.   :",
"     `.  .-\"    `l    __/ /`. :  ; ; \  ;",
"       \   .-\" .-\"-.-\"  .' .'j \  /   ;/",
"        \ / .-\"   /.     .'.' ;_:'    ;",
"         :-\"\"-.`./-.'     /    `.___.'",
"               \ `t  ._  / ",
"               \"-.t-._:' "]

		self._mat = \
["	              _.' :  `._				  ",
"             .-.'`.  ;   .'`.-.		  ",
"    __      / : ___\ ;  /___ ; \      __  ",
"  ,'_ \"\"--.:__;\".-.\";: :\".-.\":__;.--\"\" _`,",
"  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;",
"       `:-.._J '-.-'L__ `-- ' L_..-;'",
"         \"-.__ ;  .-\"  \"-.  : __.-\"",
"             L ' /.------.\ ' J",
"              \"-.   \"--\"   .-\"",
"             __.l\"-:_JL_;-\";.__",
"          .-j/'.;  ;\"\"\"\"  / .'\"-.",
"       .' /:`. \"-.:     .-\" .';  `.",
"    .-\"  / ;  \"-. \"-..-\" .-\"  :    \"-.			YOU HAVE RESCUED BABY YODA!",
" .+\"-.  : :      \"-.__.-\"      ;-._   \ ",
" ; \  `.; ;                    : : \"+. ;",
" :  ;   ; ;                    : ;  : \:",
" : `.\"-; ;  ;                  :  ;   ,/;",
" ;    -: ;  :                ;  : .-\"'  :",
" :\     \  : ;             : \.-\"      :",
"  ;`.    \  ; :            ;.'_..--  / ;",
"  :  \"-.  \"-:  ;          :/.\"      .'  :",
"    \       .-`.\        /t-\"\"  \":-+.   :",
"     `.  .-\"    `l    __/ /`. :  ; ; \  ;",
"       \   .-\" .-\"-.-\"  .' .'j \  /   ;/",
"        \ / .-\"   /.     .'.' ;_:'    ;",
"         :-\"\"-.`./-.'     /    `.___.'",
"               \ `t  ._  / ",
"               \"-.t-._:' "]

		self._losingmat = \
["	              _.' :  `._				  ",
"             .-.'`.  ;   .'`.-.		  ",
"    __      / : ___\ ;  /___ ; \      __  ",
"  ,'_ \"\"--.:__;\".-.\";: :\".-.\":__;.--\"\" _`,",
"  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;",
"       `:-.._J '-.-'L__ `-- ' L_..-;'",
"         \"-.__ ;  .-\"  \"-.  : __.-\"",
"             L ' /.------.\ ' J",
"              \"-.   \"--\"   .-\"",
"             __.l\"-:_JL_;-\";.__",
"          .-j/'.;  ;\"\"\"\"  / .'\"-.",
"       .' /:`. \"-.:     .-\" .';  `.",
"    .-\"  / ;  \"-. \"-..-\" .-\"  :    \"-.			YOU HAVE FAILED TO RESCUE BABY YODA!",
" .+\"-.  : :      \"-.__.-\"      ;-._   \ ",
" ; \  `.; ;                    : : \"+. ;",
" :  ;   ; ;                    : ;  : \:",
" : `.\"-; ;  ;                  :  ;   ,/;",
" ;    -: ;  :                ;  : .-\"'  :",
" :\     \  : ;             : \.-\"      :",
"  ;`.    \  ; :            ;.'_..--  / ;",
"  :  \"-.  \"-:  ;          :/.\"      .'  :",
"    \       .-`.\        /t-\"\"  \":-+.   :",
"     `.  .-\"    `l    __/ /`. :  ; ; \  ;",
"       \   .-\" .-\"-.-\"  .' .'j \  /   ;/",
"        \ / .-\"   /.     .'.' ;_:'    ;",
"         :-\"\"-.`./-.'     /    `.___.'",
"               \ `t  ._  / ",
"               \"-.t-._:' "]

	def retInitialMat(self):
		return self._initialmat

	def retLosingMat(self):
		return self._losingmat

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
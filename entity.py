import globalobjects
from globalobjects import obj_Board as board

class point: 
    def __init__(self, x, y): 
        self._x = x 
        self._y = y 

class entity():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._mat = None
        self._len = 0
        self._width = 0

    def retPos(self):
        return (self._x, self._y)

    def retMat(self):
        return self._mat

    def retDim(self):
        return (self._len, self._width)
    
    def updateBoard(self, mat, flag="empty"):
        text = " Score: " + str(globalobjects.score) + " || Lives: " + str(globalobjects.lives) + " || Shield: " + ("Ready" if globalobjects.shield == 1 else "Not Ready") + (" || Time Left: " + str(globalobjects.timeleft) if globalobjects.timeleft > 0 else " || Boss Fight!")
        board._matrix[1] = [i for i in (text + (board._columns - len(text))*" ")]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if flag is "empty":
                    board._matrix[self._x + i][self._y + j] = ' '
                else:
                    board._matrix[self._x + i][self._y + j] = mat[i][j]
        # print(board._matrix)
	
    def moveLeft(self, y):
        if (self._y - y > 0):
            self.updateBoard(self._mat, )
            self._y = self._y - y
            self.updateBoard(self._mat, "put")

    def moveRight(self, y):
        if (self._y + y < board._columns):
            self.updateBoard(self._mat, )
            self._y = self._y + y
            self.updateBoard(self._mat, "put")

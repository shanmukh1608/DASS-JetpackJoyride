from globalobjects import obj_Board as board


class entity():
    def __init__(self, x, y, lent, wid):
        self._x = x
        self._y = y
        self._len = lent
        self._wid = wid
        self._mat = None

    def retPos(self):
        return (self._x, self._y)

    def retDim(self):
        return(self.len, self.wid)

    def retMat(self):
        return self._mat

    def putOnBoard(self, mat, flag="empty"):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if flag is "empty":
                    board._matrix[self._x + i][self._y + j] = ' '
                else:
                    board._matrix[self._x + i][self._y + j] = mat[i][j]
        # print(board._matrix)
	
    def moveLeft(self, y):
        if (self._y - y > 0):
            self.putOnBoard(self._mat, )
            self._y = self._y - y
            self.putOnBoard(self._mat, "put")

    def moveRight(self, y):
        if (self._y + y < board._columns//2):
            self.putOnBoard(self._mat, )
            self._y = self._y + y
            self.putOnBoard(self._mat, "put")

    def gravity(self, g_timer):
        if g_timer < 6:
            if g_timer % 6 == 0:
                self._x = self._x + 1

        elif g_timer < 12:
            if g_timer % 3 == 0:
                self._x = self._x + 1

        elif g_timer < 18:
            if g_timer % 1 == 0:
                self._x = self._x + 1

        else:
            self._x = self._x + 1

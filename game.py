import signal
import os
import subprocess
import time
import readInput as hack

from characters import mando
from globalobjects import obj_Board as board

os.system('clear')

kb = hack.KBHit()

mando = mando(10, 10, 0, 0)
mando.putOnBoard(mando._mat, flag="put")

while (1):
    text="f"
    if kb.kbhit():
        text = kb.getch()
    
    if text == "w":
        mando.moveUp(1)
    if text == "d":
        mando.moveRight(1)
    if text == "a":
        mando.moveLeft(1)

    board.printboard()


# print(mando._mat) 
# mat = mando.retMat()
# print(mat)
# 
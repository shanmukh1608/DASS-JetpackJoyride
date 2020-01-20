import signal
import os
import subprocess
import time
import readInput as hack
import random   
import cursor

from characters import mando
from objects import coins, lasers
from globalobjects import obj_Board as board

os.system('clear')
cursor.hide()

startTime = time.time()
lastCoinTime = time.time()
lastLaserTime = time.time()
g_timer = 0
tick = 0

coinsList = []
coinCount = 0

laserList = []
laserCount = 0

mando = mando(board._rows-7, 1)
kb = hack.KBHit()


while (1):
    mando.putOnBoard(mando._mat, flag="put")

    # mando.gravity(g_timer)
    if (tick % 2 == 0):
        mando.moveDown(1)
    # g_timer = g_timer + 1

    # if (mando.retPos()[0] == board._rows - 7): # if touches ground
        # g_timer = 0
        

    if (time.time() - lastCoinTime > 2):
        coinsList.append(coins(random.randint(2, board._rows - 3), board._columns - 1))
        coinsList[coinCount].putOnBoard(coinsList[coinCount].retMat(), flag="put")
        coinCount = coinCount + 1
        lastCoinTime = time.time()

    if (time.time() - lastLaserTime > 2):
        laserList.append(lasers(random.randint(2, board._rows - 7), board._columns - 6))
        laserList[laserCount].putOnBoard(laserList[laserCount].retMat(), flag="put")
        laserCount = laserCount + 1
        lastLaserTime = time.time()

    for (coin, laser) in zip(coinsList, laserList):        
        if (tick % 3 == 0):
            coin.moveLeft(1)
            laser.moveLeft(1)
        
        if (coin.retPos()[1] == 1):
            coin.putOnBoard(coin.retMat(), )
            del(coin)

        if (laser.retPos()[1] == 1):
            laser.putOnBoard(laser.retMat(), )
            del(laser)

    text="f"
    if kb.kbhit():
        text = kb.getch()
    
    if text == "w":
        mando.moveUp(5)
    if text == "d":
        mando.moveRight(1)
    if text == "a":
        mando.moveLeft(1)

    board.printboard()

    tick = tick + 1
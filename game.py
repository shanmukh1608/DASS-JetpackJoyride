import signal
import os
import subprocess
import time
import readInput as hack
import random   
import cursor

from characters import mando
from entity import point
from objects import coins, lasers
import globalobjects
from globalobjects import obj_Board as board

os.system('clear')
cursor.hide()

def checkCollision(obj1, obj2):
	l1 = point(obj1.retPos()[1], obj1.retPos()[0])
	r1 = point(obj1.retPos()[1] + obj1.retDim()[1], obj1.retPos()[0] + obj1.retDim()[0])

	l2 = point(obj2.retPos()[1], obj2.retPos()[0])
	r2 = point(obj2.retPos()[1] + obj2.retDim()[1], obj2.retPos()[0] + obj2.retDim()[0])

	if(l1._x > r2._x or l2._x > r1._x): 
		return 0

	if(l1._y > r2._y or l2._y > r1._y): 
		return 0
	
	return 1

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


while (globalobjects.lives > 0 and globalobjects.gameOver == True):
	mando.updateBoard(mando._mat, flag="put")

	# mando.gravity(g_timer)
	if (tick % 2 == 0):
		mando.moveDown(1)
	# g_timer = g_timer + 1

	# if (mando.retPos()[0] == board._rows - 7): # if touches ground
		# g_timer = 0
		
	if (time.time() - lastCoinTime > 2):
		coinsList.append(coins(random.randint(2, board._rows - 3), board._columns - 1))
		coinsList[coinCount].updateBoard(coinsList[coinCount].retMat(), flag="put")
		coinCount = coinCount + 1
		lastCoinTime = time.time()

	if (time.time() - lastLaserTime > 2):
		laserList.append(lasers(random.randint(2, board._rows - 7), board._columns - 6))
		laserList[laserCount].updateBoard(laserList[laserCount].retMat(), flag="put")
		laserCount = laserCount + 1
		lastLaserTime = time.time()

	for i in range(len(coinsList)):

		try:
			if (tick % 3 == 0):
				coinsList[i].moveLeft(1)
		except:
			pass

		try:
			if (checkCollision(coinsList[i], mando) == 1):
				globalobjects.score = globalobjects.score + 1
				coinsList[i].updateBoard(coinsList[i].retMat(), )
				del(coinsList[i])
				coinCount = coinCount - 1
		except:
			pass
			
		try:
			if (coinsList[i].retPos()[1] == 1):
				coinsList[i].updateBoard(coinsList[i].retMat(), )
				del(coinsList[i])
				coinCount = coinCount - 1
		except:
			pass

	for i in range(len(laserList)):
		
		try:
			if (tick % 3 == 0):
				laserList[i].moveLeft(1)
		except:
			pass

		try:
			if (checkCollision(laserList[i], mando) == 1):
				globalobjects.lives = globalobjects.lives - 1
				laserList[i].updateBoard(laserList[i].retMat(), )
				del(laserList[i])
				laserCount = laserCount - 1
		except:
			pass

		try:
			if (laserList[i].retPos()[1] == 1):
				laserList[i].updateBoard(laserList[i].retMat(), )
				del(laserList[i])
				laserCount = laserCount - 1
		except:
			pass


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
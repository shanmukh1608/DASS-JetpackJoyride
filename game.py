import signal
import os
import subprocess
import time
import readInput as hack
import random   
import cursor

from characters import mando
from entity import point
from objects import coins, lasers, bullets, speedup
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
lastPowerUpTime = time.time() #last time of collection
lastSpeedUpTime = time.time() #last time of activation
lastShieldTime = time.time()

g_timer = 0
tick = 0

coinsList = []
coinCount = 0

laserList = []
laserCount = 0

powerUpList = []
powerUpCount = 0

bulletList = []
bulletCount = 0

mando = mando(board._rows-7, 1)
kb = hack.KBHit()


while (globalobjects.lives > 0 and globalobjects.gameOver == False):

	if (globalobjects.shieldActive == True):
		mando.updateBoard(mando._shieldMat, flag="put")
		# mando._width = 6
	else:
		mando.updateBoard(mando._mat, flag="put")

	mando.gravity()


	if (time.time() - lastShieldTime >= 10):
		globalobjects.shieldActive = False
		# mando._width = 4

	if (time.time() - lastShieldTime >= 20):
		globalobjects.shieldAvailable = True
	
	if (time.time() - lastSpeedUpTime >= 10):
		globalobjects.speedup = False

	if (mando.retPos()[0] == board._rows - 1): # if touches ground
		globalobjects.g_timer = time.time()
		
	if (time.time() - lastCoinTime > 2):
		coinsList.append(coins(random.randint(3, board._rows - 3), board._columns - 1))
		coinsList[coinCount].updateBoard(coinsList[coinCount].retMat(), flag="put")
		coinCount = coinCount + 1
		lastCoinTime = time.time()

	if (time.time() - lastLaserTime > 2):
		laserList.append(lasers(random.randint(3, board._rows - 8), board._columns - 7))
		laserList[laserCount].updateBoard(laserList[laserCount].retMat(), flag="put")
		laserCount = laserCount + 1
		lastLaserTime = time.time()

	if (time.time() - lastPowerUpTime > 10):
		powerUpList.append(speedup(random.randint(3, board._rows - 7), board._columns - 6))
		powerUpList[powerUpCount].updateBoard(powerUpList[powerUpCount].retMat(), flag="put")
		powerUpCount = powerUpCount + 1
		lastPowerUpTime = time.time()

	for i in range(len(bulletList)):
		try:
			if (tick % 2 == 0):
				bulletList[i].moveRight(1 if globalobjects.speedup == False else 2)
		except:
			pass

		try:
			for j in range(len(laserList)):
				if (checkCollision(laserList[j], bulletList[i]) == 1):
					laserList[j].updateBoard(laserList[j].retMat(), )
					del(laserList[j])
					laserCount = laserCount - 1
		except:
			pass

		try:
			if (bulletList[i].retPos()[1] > board._columns - 5):
				bulletList[i].updateBoard(bulletList[i].retMat(), )
				del(bulletList[i])
				bulletCount = bulletCount - 1
		except:
			pass

	for i in range(len(coinsList)):

		try:
			if (tick % 3 == 0):
				coinsList[i].moveLeft(1 if globalobjects.speedup == False else 2)
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
			if (coinsList[i].retPos()[1] < 4):
				coinsList[i].updateBoard(coinsList[i].retMat(), )
				del(coinsList[i])
				coinCount = coinCount - 1
		except:
			pass

	for i in range(len(laserList)):
		
		try:
			if (tick % 3 == 0):
				laserList[i].moveLeft(1 if globalobjects.speedup == False else 2)
		except:
			pass

		try:
			if (checkCollision(laserList[i], mando) == 1):
				if (globalobjects.shieldActive == False):
					globalobjects.lives = globalobjects.lives - 1
				laserList[i].updateBoard(laserList[i].retMat(), )
				del(laserList[i])
				laserCount = laserCount - 1
		except:
			pass

		try:
			if (laserList[i].retPos()[1] < 4):
				laserList[i].updateBoard(laserList[i].retMat(), )
				del(laserList[i])
				laserCount = laserCount - 1
		except:
			pass

	for i in range(len(powerUpList)):
		try:
			if (tick % 3 == 0):
				powerUpList[i].moveLeft(1 if globalobjects.speedup == False else 2)
		except:
			pass
			
		try:
			if (checkCollision(powerUpList[i], mando) == 1):
				globalobjects.speedup = True
				lastSpeedUpTime = time.time()
				powerUpList[i].updateBoard(powerUpList[i].retMat(), )
				del(powerUpList[i])
				powerUpCount = powerUpCount - 1
		except:
			pass

		try:
			if (powerUpList[i].retPos()[1] < 4):
				powerUpList[i].updateBoard(powerUpList[i].retMat(), )
				del(powerUpList[i])
				powerUpCount = powerUpCount - 1
		except:
			pass
		
	text="x"
	if kb.kbhit():
		text = kb.getch()
	
	if text == "w":
		mando.moveUp(5)
		globalobjects.g_timer = time.time()
	if text == "d":
		mando.moveRight(1 if globalobjects.speedup == False else 2)
	if text == "a":
		mando.moveLeft(1 if globalobjects.speedup == False else 2)
	if text == " ":
		if globalobjects.shieldAvailable is True:
			globalobjects.shieldActive = True
			globalobjects.shieldAvailable = False
			lastShieldTime = time.time()
	if text == "f":
		bulletList.append(bullets(mando.retPos()[0]+2, mando.retPos()[1]+7))
		bulletList[bulletCount].updateBoard(bulletList[bulletCount].retMat(), flag="put")
		bulletCount = bulletCount + 1

	if text == "q":
		globalobjects.gameOver = True

	board.printboard()

	tick = tick + 1
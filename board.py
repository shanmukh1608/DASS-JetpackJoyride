import subprocess
import colorama
import colors
from colors import *
from colorama import Fore, Back, Style

def pos(x, y):
	return '\x1b[%d;%dH' % (y, x)

class board:


	def __init__(self, rows, columns):
		self._rows = rows
		self._columns = columns
		self._matrix = []

	def create_board(self):
		for i in range(self._rows):
			self.new = []
			for j in range(self._columns):
				self.new.append(" ")
			self._matrix.append(self.new)

	
	def printboard(self):
		for i in range(self._rows):
			for j in range(self._columns):
				if i<3:
					print('%s%s%s%s' % (pos(j, i), Back.BLUE,Fore.BLACK, self._matrix[i][j]), end='')
				elif i == self._rows - 1:
					print('%s%s%s%s' % (pos(j, i), Back.RED,Fore.BLACK, self._matrix[i][j]), end='')
				elif i == self._rows - 2:
					print('%s%s%s%s' % (pos(j, i), Back.GREEN,Fore.BLACK, self._matrix[i][j]), end='')
				elif self._matrix[i][j] == ">":
					print('%s%s%s%s' % (pos(j, i), Back.BLACK,Fore.RED, self._matrix[i][j]), end='')
				elif self._matrix[i][j] == "©":
					print('%s%s%s%s' % (pos(j, i), Back.BLACK,Fore.YELLOW, self._matrix[i][j]), end='')
				elif self._matrix[i][j] == "P":
					print('%s%s%s%s' % (pos(j, i), Back.BLACK,Fore.BLUE, self._matrix[i][j]), end='')
				elif self._matrix[i][j] == "O":
					print('%s%s%s%s' % (pos(j, i), Back.BLACK,Fore.RED, self._matrix[i][j]), end='')
				elif self._matrix[i][j] == "S":
					print('%s%s%s%s' % (pos(j, i), Back.BLACK,Fore.BLUE, self._matrix[i][j]), end='')
				elif self._matrix[i][j] == "@":
					print('%s%s%s%s%s' % (pos(j, i), Back.BLACK,Fore.WHITE,Style.BRIGHT, self._matrix[i][j]), end='')
				else:
					print('%s%s%s%s' % (pos(j, i), Back.BLACK,Fore.WHITE, self._matrix[i][j]), end='')

					# print('%s%s' % (pos(j, i), self._matrix[i][j]), end='')
					
			print("")
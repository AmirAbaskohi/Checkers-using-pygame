import pygame
from .constants import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from .pieces import Piece

class Board:

	def __init__(self):
		self.board = []
		self.selectedPiece = None
		self.redLeft = self.whiteLeft = 12
		self.redKings = self.whiteKings = 0
		self.createBoard()

	def drawCubes(self, win):
		win.fill(BLACK)
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

	def createBoard(self):
		for row in range(ROWS):
			self.board.append([])
			for col in range(COLS):
				if col % 2 == ((row + 1) % 2):
					if row < 3:
						self.board[row].append(Piece(row, col, WHITE))
					elif row > 4:
						self.board[row].append(Piece(row, col, RED))
					else:
						self.board[row].append(0)
				else:
					self.board[row].append(0)

	def draw(self, win):
		self.drawCubes(win)
		for row in range(ROWS):
			for col in range(COLS):
				piece = self.board[row][col]
				if piece != 0:
					piece.draw(win)
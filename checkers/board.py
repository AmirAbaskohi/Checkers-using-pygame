import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE

class Board:

	def __init__(self):
		self.board = []
		self.selectedPiece = None
		self.redLeft = self.whiteLeft = 12
		self.redKings = self.whiteKings = 0

	def drawCubes(self, win):
		win.fill(BLACK)
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

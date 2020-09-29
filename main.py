import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chechers')

def getRowColFromMouse(pos):
	x, y = pos
	row = y // SQUARE_SIZE
	col = x // SQUARE_SIZE
	return row, col

def main():
	run = True
	clock = pygame.time.Clock()
	board = Board()

	piece = board.getPiece(0, 1)

	while run:
		clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col = getRowColFromMouse(pos)
				piece = board.getPiece(row, col)
				board.move(piece, 4, 3)

		board.draw(WIN)
		pygame.display.update()

	pygame.quit()

main()

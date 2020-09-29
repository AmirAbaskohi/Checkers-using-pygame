import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chechers')

def main():
	run = True
	clock = pygame.time.Clock()
	board = Board()

	piece = board.getPiece(0, 1)
	board.move(piece, 4, 3)

	while run:
		clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				pass

		board.draw(WIN)
		pygame.display.update()

	pygame.quit()

main()

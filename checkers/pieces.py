from .constants import RED, WHITE, SQURE_SIZE, GREY

def Piece:

	PADDING = 10
	OUTLINE = 2

	def __init__(self, row, col, color):
		self.row = row
		self.col = col
		self.color = color
		self.king = False
		if self.color == RED:
			self.direction = -1
		else:
			self.direction = 1
		self.x = 0
		self.y = 0
		self.calPos()

	def calPos(self):
		self.x = SQURE_SIZE * self.col + SQURE_SIZE // 2
		self.y = SQURE_SIZE * self.row + SQURE_SIZE // 2

	def make_king(self):
		self.king = True

	def draw(self, win):
		radius = SQURE_SIZE//2 -self.PADDING
		pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
		pygame.draw.circle(win, GREY, (self.x, self.y), radius)

	def __repr__(self):
		return str(self.color)
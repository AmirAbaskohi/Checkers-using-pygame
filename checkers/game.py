import pygame
from .constants import RED, WHITE
from checkers.board import Board

class Game:

    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.validMoves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.getPiece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.validMoves = self.board.getValidMoves(piece)
                return True

        return False

    def _move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.validMoves:
            self.board.move(self.selected, row, col)
        else:
            return False
        
        return True

    def changeTurn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
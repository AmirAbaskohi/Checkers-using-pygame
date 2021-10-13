from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, maxPlayer, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if maxPlayer:
        maxEval = float('-inf')
        bestMove = None
        for move in getAllMoves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestMove = move

        return maxEval, bestMove
    else:
        minEval = float('inf')
        bestMove = None
        for move in getAllMoves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                bestMove = move

        return minEval, bestMove

def simulateMove(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def getAllMoves(board, color, game):
    moves = []

    for piece in board.getAllPieces(color):
        validMoves = board.getValidMoves(piece)
        for move, skip in validMoves.items():
            tempBoard = deepcopy(board)
            tempPiece = tempBoard.getPiece(piece.row, piece.col)
            newBoard = simulateMove(tempPiece, move, tempBoard, game, skip)
            moves.append(newBoard)

    return moves
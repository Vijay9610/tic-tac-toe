"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
    
    if countX <= countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)

    # check for illegal move
    i = action[0]
    j = action[1]

    if i < 0 or i >= 3 or j < 0 or j >= 3 or newBoard[i][j] != EMPTY:
        raise InvalidMove
    else:
        newBoard[i][j] = player(newBoard)
    
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def maxValue(board):
    v = float('-inf')
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    
    return v

def minValue(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        v = float('-inf')
        optimal = None
        for action in actions(board):
            if maxValue(result(board, action)) > v:
                optimal = action
        
        return optimal
    
    if player(board) == O:
        v = float('inf')
        optimal = None
        for action in actions(board):
            if minValue(result(board, action)) < v:
                optimal = action
        
        return optimal
        
    





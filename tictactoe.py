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
    x, o = (0, 0)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
    if x > o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    open = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                open.add((i, j))
    return open


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise RuntimeError
    
    res = copy.deepcopy(board)
    res[action[0]][action[1]] = player(board)
    return res


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
    
    for j in range(len(board[0])):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        elif board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY and winner(board) == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
def isEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                return False
    return True
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if isEmpty(board):
        return (0,0)
    if terminal(board):
        return None
    
    curr = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best_move = None

        for action in actions(board):
            new_board = result(board, action)
            min_val, _ = min_value(new_board)
            if min_val > v:
                v = min_val
                best_move = action
        return v, best_move
    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best_move = None

        for action in actions(board):
            new_board = result(board, action)
            max_val, _ = max_value(new_board)
            if max_val < v:
                v = max_val 
                best_move = action

        return v, best_move
    
    if curr == X:
        _, move = max_value(board)
    else:
        _, move = min_value(board)

    return move
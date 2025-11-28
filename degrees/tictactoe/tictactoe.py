"""
Tic Tac Toe Player
"""

import math

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
    xcount = 0
    ocount = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xcount += 1
            elif board[i][j] == O:
                ocount += 1

    if xcount > ocount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: 
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns a new board after applying the move.
    """
    i, j = action
    if i < 0 or j < 0:
        raise Exception("Invalid action")

    if board[i][j] is EMPTY:
        new_board = [row.copy() for row in board]
        new_board[i][j] = player(board)
        return new_board
    else:
        raise Exception("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range (3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY: 
            return board[i][0] 

    # Check columns
    for j in range (3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range (3):
        for j in range (3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    x_or_o = winner(board)
    if not x_or_o:
        return 0
    elif x_or_o == X:
        return 1
    return -1


def max_value(board):
    if terminal(board): # Returns True if game is over, False otherwise.
        return utility(board) # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
        # both terminal and utility call winner, which Returns the winner of the game, if there is one.
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    else:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_move = action
        return best_move

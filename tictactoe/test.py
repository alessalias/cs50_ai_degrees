from tictactoe import EMPTY, X, O, winner

board = [[EMPTY, X, EMPTY],
         [EMPTY, X, EMPTY],
         [EMPTY, X, EMPTY]]

w = winner(board)
print(w)
from Defs import Defs

class Board:
    def __init__(self):
        self.defs = Defs()

    def new_board(self):
        board = [ [ 0 for x in range(self.defs.cols) ]
                for y in range(self.defs.rows - 1) ]
        board += [[ 1 for x in range(self.defs.cols)]]
        for i in range(len(board)):
                board[i][0] = 9
                board[i][len(board[i]) - 1] = 9
        return board

    def check_filled_rows(self, board):
        yaaay = 0
        for y, row in enumerate(board):
            pos = 0
            for x, val in enumerate(row):
                if val:
                    pos += 1

            if pos == (len(row)) and y != len(board) - 1:
                backb = list(board)
                board[y] = [ 0 for x in range(self.defs.cols)]
                board[y][0] = 1
                board[y][len(row) - 1] = 1
                for j in range(0, y):
                    board[j+1] = backb[j]
                board[len(board) - 1] = [ 1 for x in range(self.defs.cols)]
                yaaay = 30
                break
#        board[0] = [ 0 for x in range(self.defs.cols)]
#        board[0][0] = 1
#        board[0][len(board)+1] = 1
        return board, yaaay
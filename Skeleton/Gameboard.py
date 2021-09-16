import db
import sys
class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
    
    def validateP1Move(self, move):
        if self.current_turn != 'p1':
            return False
        return self.checkBoard(move)

    def validateP2Move(self, move):
        if self.current_turn != 'p2':
            return False
        return self.checkBoard(move)

    def checkWin(self, row, column):
            win = False
            win = self.checkHorizontal(row, column)
            win = self.checkVertical(row, column)
            win = self.checkDiagonal(row, column)
    def checkHorizontal(self, row, col):
        left = max(col - 3, 0)
        right = min(col + 3, len(self.board))
    def checkVertical(row, col):
        pass
    def checkDiagonal(row, col):
        pass
    def checkBoard(self, move):
        column = int(move['column'][len(move['column'])-1]) -1
        if self.board[0][column] == 0:
            for i in range(6):
                if self.board[i][column] != 0:
                    if self.current_turn == 'p1':
                        self.board[i-1][column] = self.player1
                        self.current_turn = "p2"
                    else:
                        self.board[i-1][column] = self.player2
                        self.current_turn = "p1"
                    return True
            if self.current_turn == 'p1':
                self.board[len(self.board)-1][column] = self.player1
            else:
                self.board[len(self.board)-1][column] = self.player2
            if self.current_turn == "p1":
                self.current_turn = "p2"
            else:
                self.current_turn = "p1"

            return True
        return False
'''
Add Helper functions as needed to handle moves and update board and turns
'''
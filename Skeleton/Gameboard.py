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
        if len(self.player1) < 1 or len(self.player2) < 1:
            return "Game didn't start yet."
        if len(self.game_result) > 0:
            return "Game is over."
        if self.current_turn != 'p1':
            return "Not your turn."
        return self.checkBoard(move)

    def validateP2Move(self, move):
        if len(self.player1) < 1 or len(self.player2) < 1:
            return "Game didn't start yet."
        if len(self.game_result) > 0:
            return "Game is over."
        if self.current_turn != 'p2':
            return "Not your turn."
        return self.checkBoard(move)

    def checkWin(self, row, column):
            color = ""
            if self.current_turn == "p1":
                color = self.player1
            else:
                color  = self.player2
            if self.checkHorizontal(row, column, color):
                self.game_result = self.current_turn
                return
            if self.checkVertical(row, column, color):
                self.game_result = self.current_turn
                return
            if self.checkDiagonalLeft(row, column, color):
                self.game_result = self.current_turn
                return
            if self.checkDiagonalRight(row, column, color):
                self.game_result = self.current_turn
                return
    def checkHorizontal(self, row, col, color):
        left = max(col - 4, -1)
        right = min(col + 4, len(self.board[0]))
        count = 0
        for i in range(col, left, -1):
            if self.board[row][i] == color:
                count += 1
            else:
                break
        for i in range(col+1, right):
            if self.board[row][i] == color:
                count += 1
            else:
                break
        if count >= 4:
            return True
        return False

    def checkVertical(self, row, col, color):
        count = 0
        for i in range(row, min(row+5, len(self.board))):
            if self.board[i][col] == color:
                count += 1
            else:
                break
        if count >= 4:
            return True
        return False

    def checkDiagonalLeft(self, row, col, color):
        left = max(col - 4, -1)
        right = min(col + 4, len(self.board))
        count = 0
        rowOffset = 0
        for i in range(col, left, -1):
            if row + rowOffset < 0:
                break
            if self.board[row + rowOffset][i] == color:
                count += 1
                rowOffset -= 1
            else:
                break
        rowOffset = 1
        for i in range(col+1, right, 1):
            if row + rowOffset >= len(self.board):
                break
            if self.board[row + rowOffset][i] == color:
                count += 1
                rowOffset += 1
            else:
                break
        if count >= 4:
            return True
        return False

    def checkDiagonalRight(self, row, col, color):
        left = max(col - 4, -1)
        right = min(col + 4, len(self.board))
        count = 0
        rowOffset = 0
        for i in range(col, left, -1):
            if row + rowOffset >= len(self.board):
                break
            if self.board[row + rowOffset][i] == color:
                count += 1
                rowOffset += 1
            else:
                break
        rowOffset = -1
        for i in range(col+1, right, 1):
            if row + rowOffset < 0:
                break
            if self.board[row + rowOffset][i] == color:
                count += 1
                rowOffset -= 1
            else:
                break
        if count >= 4:
            return True
        return False

    def checkBoard(self, move):
        column = int(move['column'][len(move['column'])-1]) -1
        if self.board[0][column] == 0:
            for i in range(6):
                if self.board[i][column] != 0:
                    if self.current_turn == 'p1':
                        self.board[i-1][column] = self.player1
                        self.checkWin(i-1, column)
                        self.current_turn = "p2"
                    else:
                        self.board[i-1][column] = self.player2
                        self.checkWin(i-1, column)
                        self.current_turn = "p1"
                    
                    return ""
            if self.current_turn == 'p1':
                self.board[len(self.board)-1][column] = self.player1
            else:
                self.board[len(self.board)-1][column] = self.player2

            self.checkWin(len(self.board)-1, column)

            if self.current_turn == "p1":
                self.current_turn = "p2"
            else:
                self.current_turn = "p1"
            
            return ""
        return "No space left in column."
'''
Add Helper functions as needed to handle moves and update board and turns
'''
import db

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

    def checkBoard(self, move):
        column = int(move.column[len(move.column)-1]) -1
        if self.board[0][column] == 0:
            for i in range(7):
                if self.board[i][column] == 1 or self.board[i][column] == 2:
                    if self.current_turn == 'p1':
                        self.board[i-1][column] = self.colorToNum(self.player1)
                    else:
                        self.board[i-1][column] = self.colorToNum(self.player2)
                    return True
            if self.current_turn == 'p1':
                self.board[len(self.board)-1][column] = self.colorToNum(self.player1)
            else:
                self.board[len(self.board)-1][column] = self.colorToNum(self.player2)
            return True
        return False
        
    def colorToNum(color):
        if color == "red":
            return 1
        else:
            return 2
'''
Add Helper functions as needed to handle moves and update board and turns
'''
import db

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
    
    def validateP1Move(move):
        if self.current_turn != 'p1':
            return False
    def checkBoard(move):
        column = int(move.column[len(move.column)-1]) -1
        if self.board[0][column] == 0:
            for i in range(7):
                if self.board[i][column] == 1 or self.board[i][column] == 2:
                    self.board[i-1][column] = 3
'''
Add Helper functions as needed to handle moves and update board and turns
'''


    

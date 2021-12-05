BLACK = -1
WHITE = +1
SERIAL_X = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
SERIAL_Y = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

class Board:
    def __init__(self):
        this.board = [[0] * 15 for _ in range(15)]
    
    def __str__(self):
        def __str__(self):
        s = '   '
        for x in range(self.size):
            s += SERIAL_X[x] + ' '
        s += '\n'
        for y, row in enumerate(self.board):
            if y < 10:
                s += SERIAL_Y[y] + '  '
            else:
                s += SERIAL_Y[y] + ' '
            for x, col in enumerate(row):
                if col == BLACK:
                    s += 'x'
                elif col == WHITE:
                    s += 'o'
                else:
                    s += '.'
                s += ' '
            s += SERIAL_Y[y] + '\n'
        s += '   '
        for x in range(self.size):
            s += SERIAL_X[x] + ' '
        return s + '\n'
    def win(self, color):
        if self.size < 5:
            return False
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.check_horizontal(r, c, color) or self.check_vertical(r, c, color) or self.check_diagonal(r, c, color):
                        return True
    
    def check_horizontal(self, r, c, color):
        if c + 4 < len(self.board): 
            if self.board[r][c] == self.board[r][c+1] == self.board[r][c+2] == self.board[r][c+3] == self.board[r][c+4] == color:
                return True
        return False
    
    def check_vertical(self, r, c, color):
        if r + 4 < len(self.board):
            if self.board[r][c] == self.board[r+1][c] == self.board[r+2][c] == self.board[r+3][c] == self.board[r+4][c] == color:
                return True
        return False
    
    def check_diagonal(self, r, c, color):
        if r + 4 < len(self.board) and c + 4 < len(self.board):
            if self.board[r][c] == self.board[r+1][c+1] == self.board[r+2][c+2] == self.board[r+3][c+3] == self.board[r+4][c+4] == color:
                return True
        if r - 4 >= 0 and c + 4 < len(self.board):
            if self.board[r][c] == self.board[r-1][c+1] == self.board[r-2][c+2] == self.board[r-3][c+3] == self.board[r-4][c+4] == color:
                return True
        return False
        
    def set(self, c, r, color):
        if self.board[r][c] != 0:
            return False
        clean()
        self.board[r][c] = color
        self.show()
        return True
    def unset(self, c, r):
        clean()
        self.board[r][c] = 0
        self.show()
        return True
    
    def get(self, r, c):
        return self.board[r][c]
    
import numpy as np

class GameBoard:
    board = []
    row_count = 0
    column_count = 0
    
    def __init__(self):
        self.row_count = 6
        self.column_count = 7
        self.board = np.zeros((self.row_count, self.column_count))
        
    #Check if win in column
    def check_status_column(self, token):
        for column in range(self.column_count - 3):
            for row in range(self.row_count):
                if (self.board[row][column] == token and self.board[row][column + 1] == token
                        and self.board[row][column + 2] == token and self.board[row][column + 3] == token):
                    return True

    #Check if win in row
    def check_status_row(self, token):
        for column in range(self.column_count):
            for row in range(self.row_count - 3):
                if (self.board[row][column] == token and self.board[row + 1][column] == token
                        and self.board[row + 2][column] == token and self.board[row + 3][column] == token):
                    return True

    #Check if win in diagonal going up
    def check_status_diagonal_up(self, token):
        for c in range(self.column_count - 3):
            for r in range(self.row_count - 3):
                if (self.board[r][c] == token and self.board[r + 1][c + 1] == token
                        and self.board[r + 2][c + 2] == token and self.board[r + 3][c + 3] == token):
                    return True

    #Check if win in diagonal going down
    def check_status_diagonal_down(self, token):
        for c in range(self.column_count - 3):
            for r in range(3, self.row_count):
                if (self.board[r][c] == token and self.board[r - 1][c + 1] == token
                        and self.board[r - 2][c + 2] == token and self.board[r - 3][c + 3] == token):
                    return True

    #Check if draw
    def check_status_draw(self):
        ctr = 0
        for c in range(self.column_count - 1):
            for r in range(self.row_count - 1):
                if self.board[r][c] == 0:
                    ctr = ctr + 1
        if ctr == 0:
            return True
        else:
            return False

    #Check if win
    def check_result(self, token):
        if self.check_status_column(token):
            return True
        elif self.check_status_row(token):
            return True
        elif self.check_status_diagonal_up(token):
            return True
        elif self.check_status_diagonal_down(token):
            return True
        else:
            return False
    
    #Check if column choosen by players is full
    def column_not_full(self, col):
        return self.board[self.row_count - 1][col] == 0
    
    #Get next free row for choosen column
    def get_next_free_row(self, col):
            for r in range(self.row_count):
                if self.board[r][col] == 0:
                    return r
            return -1
    
    #Place token to the choosen column and row
    def place_token(self, row, col, token):
        self.board[row][col] = token
           
    #Print the board
    def print_board(self):
        print("-----------------")
        for r in range(self.row_count):
            print("| ", end="")
            for c in range(self.column_count):
                print(str(int(self.board[self.row_count -1 - r][c])) + " ", end="")
            print("|")
        print("-----------------")
        
    #Get columns that are not full yet
    def get_valid_columns(self):
        columns = []
        for c in range(self.column_count):
            if self.column_not_full(c):
                columns.append(c)
        return columns
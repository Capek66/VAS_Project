import numpy as np
import copy

class MiniMax():
    def evaluate_game(board_part, token):
        value = 0
        
        if(token == 1):
            opponent_token = 2
        else:
            opponent_token = 1
            
        if board_part.count(token) == 4:
            value += 100
        elif board_part.count(token) == 3 and board_part.count(0) == 1:
            value += 5
        elif board_part.count(token) == 2 and board_part.count(0) == 2:
            value += 2

        if board_part.count(opponent_token) == 3 and board_part.count(0) == 1:
            value -= 4

        return value

    def calculate_position_value(self, board, token):
        value = 0

        #Value center column
        center_array = [int(i) for i in list(board.board[:, 3])]
        center_count = center_array.count(token)
        value += center_count * 6

        #Value horizontal
        for r in range(6):
            board_row = [int(i) for i in list(board.board[r, :])]
            for c in range(4):
                board_part = board_row[c:c + 4]
                value += self.evaluate_game(board_part, token)

        #Value vertical
        for c in range(7):
            board_col = [int(i) for i in list(board.board[:, c])]
            for r in range(3):
                board_part = board_col[r:r + 4]
                value += self.evaluate_game(board_part, token)

        #Value diagonal up
        for r in range(3):
            for c in range(4):
                board_part = [board.board[r + i][c + i] for i in range(4)]
                value += self.evaluate_game(board_part, token)

        #Value diagonal down
        for r in range(3):
            for c in range(4):
                board_part = [board.board[r + 3 - i][c + i] for i in range(4)]
                value += self.evaluate_game(board_part, token)

        return value

    def is_leaf(self, board):
        return board.check_result(1) or board.check_result(2) or len(board.get_valid_columns()) == 0

    def minimax(self, board, depth, game_agent):
        valid_columns = board.get_valid_columns()
        is_leaf = self.is_leaf(self, board)

        if depth == 0 or is_leaf:
            if is_leaf:
                if self.calculate_position_value(self, board, 1):
                    return (None, -100000000000000)
                elif self.calculate_position_value(self, board, 2):
                    return (None, 100000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.calculate_position_value(self, board, 2))

        if game_agent:
            value = - np.Inf
            column = np.random.choice(valid_columns)
            for c in valid_columns:
                free_row = board.get_next_free_row(c)
                temp_board = copy.deepcopy(board)
                temp_board.place_token(free_row, c, 2)
                new_value = self.minimax(self, temp_board, depth-1, False)[1]
                if new_value > value:
                    value = new_value
                    column = c

            return column, value

        else:
            value = np.Inf
            column = np.random.choice(valid_columns)
            for c in valid_columns:
                free_row = board.get_next_free_row(c)
                temp_board = copy.deepcopy(board)
                temp_board.place_token(free_row, c, 1)
                new_value = self.minimax(self, temp_board, depth-1, True)[1]
                if new_value < value:
                    value = new_value
                    column = c

            return column, value
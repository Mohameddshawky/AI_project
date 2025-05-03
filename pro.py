class Gomoku:
    def __init__(self, board_size=15):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        

    def make_move(self, row, col, player):
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == 0:
            self.board[row][col] = player
            return True
        return False


    def is_winner(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    continue
                if j <= self.board_size - 5:
                    if all(self.board[i][j + k] == self.board[i][j] for k in range(5)):
                        return self.board[i][j]
                if i <= self.board_size - 5:
                    if all(self.board[i + k][j] == self.board[i][j] for k in range(5)):
                        return self.board[i][j]
                if i <= self.board_size - 5 and j <= self.board_size - 5:
                    if all(self.board[i + k][j + k] == self.board[i][j] for k in range(5)):
                        return self.board[i][j]
                if i <= self.board_size - 5 and j >= 4:
                    if all(self.board[i + k][j - k] == self.board[i][j] for k in range(5)):
                        return self.board[i][j]
        return 0  
    def is_draw(self):
        pass

    def evaluate_board(self):
        pass

    def _evaluate_line(self, line, player):

        pass

    def get_valid_moves(self):
        pass

    def minimax(self, depth, maximizing_player):

        pass

    def alpha_beta(self, depth, alpha, beta, maximizing_player):
        pass

    def human_vs_ai(self):
        pass

    def ai_vs_ai(self):
        pass

    def display_board(self):

        pass

    def set_board(self, board_state):
        pass

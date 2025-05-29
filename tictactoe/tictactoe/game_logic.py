import random
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.score_X = 0
        self.score_O = 0
        self.scoreboard = Scoreboard()

    def is_cell_empty(self, index):
        return self.board[index] == " "

    def make_move(self, index):
        if self.is_cell_empty(index):
            self.board[index] = self.current_player
            return True
        return False

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_winner(self):
        combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in combinations:
            a, b, c = combo
            same = self.board[a] == self.board[b] == self.board[c]
            not_empty = self.board[a] != " "
            if same and not_empty:
                #winner = self.board[a]
                #self.scoreboard.add_point(winner)
                return self.board[a]
        return None

    def is_draw(self):
        return " " not in self.board

    def reset_board(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def ai_move(self):
        empty_cells = [i for i, val in enumerate(self.board) if val == " "]
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return None

class Scoreboard:
    def __init__(self):
        self.score_X = 0
        self.score_O = 0

    def add_point(self, player):
        if player == "X":
            self.score_X += 1
        elif player == "O":
            self.score_O += 1
    def reset(self):
        self.score_X = 0
        self.score_O = 0

    def get_score(self):
        return self.score_X, self.score_O

    def __str__(self):
        return f"{self.score_X} | o: {self.score_O}"
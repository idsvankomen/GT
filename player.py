class Player():

    def __init__(self, strat):
        self.strategy = strat
        self.score = 0

    def make_move(self, moves):
        m1, m2, m3 = moves
        return self.strategy[m1][m2][m3]

    def update_score(self, score):
        self.score += score

    def reset_score(self):
        self.score = 0

    def get_score(self):
        return self.score
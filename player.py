class Player():

    def __init__(self, strat):
        self.strategy = strat
        self.moves = []
        self.score = 0

    def make_move(self, own_moves, opp_moves):
        return self.strategy(own_moves, opp_moves)

    def update_score(self, score):
        self.score += score

    def __str__(self):
        return self.strategy.__name__

def tit_for_tat(own_moves, opp_moves):
    if not own_moves:
        return 1
    else:
        return opp_moves[-1]

def hold_a_grudge(own_moves, opp_moves):
    if not own_moves:
        return 1
    elif own_moves[-1] == 1 and opp_moves[-1] == 1:
        return 1
    return 0
'''
Name: Ids van Komen & Bas Frelier
UvAID: 15191249 & 15269728
Description:
'''

import numpy as np

class Battle():
    def __init__(self, player1, player2, payoff_table):

        self.player1 = player1
        self.player2 = player2

        self.moves = [2,2,2]

        self.payoff_table = payoff_table

    def battle(self):

        move1 = self.player1.make_move(-1 * np.array(self.moves))
        move2 = self.player2.make_move(self.moves)

        idx = move1 + move2 + 2 if move1 == 0 and move2 == 1 else move1 + move2

        self.moves.append(idx)
        self.moves.pop(0)

        score1 = self.payoff_table[move1][move2]
        score2 = self.payoff_table[move2][move1]

        self.player1.update_score(score1)
        self.player2.update_score(score2)

'''
Name: Ids van Komen & Bas Frelier
UvAID: 15191249 & 
Description:
'''

import numpy as np

import player

class Battle():
    def __init__(self, player1, player2, payoff_table):

        self.player1 = player1
        self.player2 = player2

        self.payoff_table = payoff_table

    def battle(self):

        move1 = self.player1.make_move(self.player1.moves, self.player2.moves)
        move2 = self.player2.make_move(self.player2.moves, self.player1.moves)

        score1 = self.payoff_table[move1][move2]
        score2 = self.payoff_table[move2][move1]

        self.player1.update_score(score1)
        self.player2.update_score(score2)


if __name__ == '__main__':
    player1 = player.Player(player.tit_for_tat)
    player2 = player.Player(player.hold_a_grudge)
    sim = Battle(player1, player2)
    from pyics import GUI
    cx = GUI(sim)
    cx.start()
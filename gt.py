'''
Name: Ids van Komen & Bas Frelier
UvAID: 15191249 & 15269728
Description:
'''

import numpy as np

from pyics import Model
from pyics import paramsweep

from player import Player
import strats
from battle import Battle

import matplotlib.pyplot as plt

class Tournament(Model):
    def __init__(self, players, names):
        Model.__init__(self)

        self.rounds = 0
        self.players = players
        self.names = names

        self.make_param('DD', 1)
        self.make_param('DC', 5)
        self.make_param('CD', 0)
        self.make_param('CC', 3)
        self.make_param('reencounters', 50)

        payoff_table = [[self.DD, self.DC],[self.CD, self.CC]]
        n = len(players)
        self.battles = [Battle(players[i], players[j], payoff_table)
                        for i in range(n) for j in range(i+1, n)]

    def draw(self):
        plt.gca().cla()

        n = len(self.players)
        scores = [0 for _ in range(n)]

        for i, player in enumerate(self.players):
            scores[i] = player.get_score()


        for i in range(n):
            plt.bar(self.names[i], scores[i])
        plt.show()


    def reset(self):
        self.rounds = 0

        payoff_table = [[self.DD, self.DC],[self.CD, self.CC]]
        n = len(self.players)

        for player in self.players:
            player.reset_score()

        for battle in self.battles:
            battle.reset_moves()



    def step(self):
        self.rounds += 1
        if self.rounds > self.reencounters:
            return True

        for battle in self.battles:
            battle.battle()


if __name__ == '__main__':
    player1 = Player(strats.tit_for_tat)
    player2 = Player(strats.hold_a_grudge)
    player3 = Player(strats.always_cooperate)
    players = [player1, player2, player3]
    names = ['tit for tat', 'hold a grudge', 'always cooperate']

    sim = Tournament(players, names)

    from pyics import GUI
    cx = GUI(sim)
    cx.start()
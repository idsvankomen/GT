'''
Name: Ids van Komen & Bas Frelier
UvAID: 15191249 &
Description:
'''

import numpy as np

from pyics import Model
from pyics import paramsweep

import player
from battle import Battle

class Tournament(Model):
    def __init__(self, players):
        Model.__init__(self)

        self.rounds = 0
        self.players = players
        self.names = [str(p) for p in players]

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
        n = len(self.players)
        scores = [0 for _ in range(n)]

        for battle in self.battles:
            scores[self.names.index(str(battle.player1))] += battle.player1.score
            scores[self.names.index(str(battle.player2))] += battle.player2.score

        import matplotlib.pyplot as plt
        for i in range(n):
            plt.bar(self.names[i], scores[i])
        plt.show()


    def reset(self):
        self.rounds = 0


    def step(self):
        self.rounds += 1
        if self.rounds > self.reencounters:
            return True

        for battle in self.battles:
            battle.battle()


if __name__ == '__main__':
    player1 = player.Player(player.tit_for_tat)
    player2 = player.Player(player.hold_a_grudge)
    players = [player1, player2]
    sim = Tournament(players)

    from pyics import GUI
    cx = GUI(sim)
    cx.start()
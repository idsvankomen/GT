'''
Name: Ids van Komen & Bas Frelier
UvAID: 15191249 & 15269728
Description:
'''

from pyics import Model
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
        self.scores = [0 for _ in range(len(players))]

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

        for i in range(n):
            plt.bar(self.names[i], self.scores[i])
        plt.show()


    def reset(self):
        self.rounds = 0
        self.scores = [0 for _ in range(len(self.players))]

        for player in self.players:
            player.reset_score()

        payoff_table = [[self.DD, self.DC],[self.CD, self.CC]]
        n = len(self.players)

        self.battles = [Battle(self.players[i], self.players[j], payoff_table)
                        for i in range(n) for j in range(i+1, n)]


    def step(self):
        self.rounds += 1
        if self.rounds > self.reencounters:
            return True

        for battle in self.battles:
            battle.battle()

        for i, player in enumerate(self.players):
            self.scores[i] = player.get_score()

        return False

    def play(self):
        stop = False
        while not stop:
            stop = self.step()


if __name__ == '__main__':
    strts = [
        # bench mark strats
        strats.tit_for_tat,
        strats.hold_a_grudge,
        strats.always_cooperate,
        strats.always_defect,

        #own strats
        strats.tft_defect,
        strats.tft_dfct_bait,
        strats.average_move,
        strats.balanced_coop_v1,
        strats.balanced_coop_v2,
        strats.second2last,
        strats.copy_2back,
        strats.copy_3back,
        strats.pavlov,
        strats.pavlov_2wins
        ]

    names = ['TfT', 'HaG', 'AC', 'AD', 'TD', 'TDB', 'AM', 'BC1', 'BC2', 'StL',
             'C2B', 'C3B', 'Pav', 'Pav2']

    players = [Player(strts[i], names[i]) for i in range(len(strts))]

    sim = Tournament(players, names)

    from pyics import GUI
    cx = GUI(sim)
    cx.start()
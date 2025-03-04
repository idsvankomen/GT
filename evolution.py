from player import Player
from gt import Tournament
import strats
from random import random
import numpy as np

def genetic_algorithm(strts, order):
    print(order)
    new_strats = [[[[0 for _ in range(4)] for _ in range(4)]
                       for _ in range(4)] for _ in range(20)]

    for m1 in range(4):
        for m2 in range(4):
            for m3 in range(4):
                for j in range(20):
                    i = int(random() * 6)
                    new_strats[j][m1][m2][m3] = strts[order[i]][m1][m2][m3]
    return new_strats


def run_tournaments(players, names):

    strts = [[[[int(random()*2) for _ in range(4)] for _ in range(4)]
                       for _ in range(4)] for _ in range(20)]

    print(strts[0])
    while True:
        scores = [0 for _ in range(len(strts))]
        for i, strat in enumerate(strts):
            player = Player(strat)
            sim = Tournament(players + [player], names + ["genetic strat"])
            sim.play()
            scores[i] = sim.players[-1].get_score()
        print(scores)
        order = list(map(int, np.argsort(scores)))
        order.reverse()
        strts = genetic_algorithm(strts, order)

        print()
        print()

        if sum(scores) == 15000:
            break

    for i, strat in enumerate(strts):
        print()
        print(i, strat)



if __name__ == '__main__':
    player1 = Player(strats.tit_for_tat)
    player2 = Player(strats.hold_a_grudge)
    player3 = Player(strats.always_cooperate)
    players = [player1, player2, player3]
    names = ['tit for tat', 'hold a grudge', 'always cooperate']

    run_tournaments(players, names)
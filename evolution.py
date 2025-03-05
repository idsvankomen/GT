from player import Player
from gt import Tournament
import strats
from random import random
import numpy as np
from itertools import combinations
from math import comb

def genetic_algorithm(strts, order, n, k):
    new_strats = [[[[0 for _ in range(4)] for _ in range(4)]
                       for _ in range(4)] for _ in range(comb(n,k))]

    for m1 in range(4):
        for m2 in range(4):
            for m3 in range(4):
                for j, l in enumerate(combinations([i for i in range(n)], k)):
                    avg_move = sum(strts[order[i]][m1][m2][m3] for i in l) / k

                    rand = random() * 25
                    if avg_move >= 0.5:
                        if rand <= 1:
                            val = 0
                        else:
                            val = 1
                    else:
                        if rand <= 1:
                            val = 1
                        else:
                            val = 0
                    new_strats[j][m1][m2][m3] = val
    return new_strats


def run_tournaments(players, names, n, k, no_old_strats):

    strts = [[[[int(random()*2) for _ in range(4)] for _ in range(4)]
                       for _ in range(4)] for _ in range(20)]

    highest_score = 0
    no_diff = 0
    evolution = []
    while no_diff < 50:
        scores = [0 for _ in range(len(strts))]
        for i, strat in enumerate(strts):
            player = Player(strat, "genetic strat")
            sim = Tournament(players + [player], names + ["genetic strat"])
            sim.play()
            scores[i] = sim.players[-1].get_score()

        if highest_score == max(scores):
            no_diff += 1
        if max(scores) > highest_score:
            highest_score = max(scores)
            no_diff = 0

        evolution.append(highest_score)

        order = list(map(int, np.argsort(scores)))
        order.reverse()
        keep_strats = []
        for i in range(no_old_strats):
            keep_strats.append(strts[order[i]])
        strts = keep_strats + genetic_algorithm(strts, order, n, k)

    return evolution , highest_score

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

    res = []
    count = 0
    for n, k, no_old_strats in [(x, y, z) for x in [5,6,7] for y in [2,3,4] for z in [4,6,8]]:
        count += 1
        print(count)
        res.append(run_tournaments(players, names, n, k, no_old_strats))
    print(res)
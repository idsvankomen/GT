from pyics import paramsweep
from player import Player
from gt import Tournament
import strats

def run_experiments(sim):

    param_space = {
        'DD' : [1, 2, 3],
        'DC' : [7, 8, 9],
        'CD' : [-2, -1, 0],
        'CC' : [4, 5, 6],
        'reencounters': [10, 20, 50, 100]
        }

    paramsweep(sim, 1, param_space, ['scores'], measure_interval=0,
               csv_base_filename='experiments')

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

    run_experiments(sim)
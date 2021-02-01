from __future__ import print_function, division
from builtins import range

import numpy as np
from grid_world import standard_grid, negative_grid
from iterative_poicy_evaluation import print_values, print_policy

SMALL_ENOUGH = 1e-3
GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')

#this is deterministic
#all p(s',r|s,a) = 1 or 0

if __name__ == '__main__':
    """
    This grid gives you a reward of -0.1 for every non-terminal state
    We want to see if this will encourage finding a shorter path to the goal
    """

    grid = negative_grid()

    #print rewards
    print("rewards:")
    print_values(grid.rewards, grid)

    #state -> action
    #We'll randomly choose an action and update as we learn
    policy = {}
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ALL_POSSIBLE_ACTIONS)


    #initial policy
    print("Initial Policy")
    print_policy(policy, grid)

    #intialize V(s)

    V = {}
    states = grid.all_states()
    for s in states:
        #V[s] = 0
        if s in grid.actions:
            V[s] = np.random.random()
        else:
            #terminal state
            V[s] = 0

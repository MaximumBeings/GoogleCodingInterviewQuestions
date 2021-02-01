"""
Source: Lazy Programmer Udemy
"""

from __future__ import print_function, division
#from buitins import range
import numpy as np
from grid_world import standard_grid

SMALL_ENOUGH = 1e-3 # threshold for convergence

def print_values(V, g):
    for i in range(g.rows):
        print("--------------------------")
        for j in range(g.cols):
            v = V.get((i,j), 0)
            if v >= 0:
                print(" %.2f|" % v, end="")
            else:
                print("%.2f|" % v, end="") #-ve sign takes up extra space
        print("")


def print_policy(P, g):
    for i in range(g.rows):
        print("---------------------------")
        for j in range(g.cols):
            a = P.get((i,j), ' ')
            print(" %s |" % a, end="")
        print("")


if __name__ == '__main__':
    """
    Iterative policy evaluation
    Given a policy, let's find it's value function V(s)
    We will do this for both a uniform random policy and fixed policy
    NOTE:
    There are 2 sources of randomness
    p(a|s) - deciding what action to take given the state
    p(s',r|s,a) - the next state and reward given your state-action pair
    We are only modeling p(a|s) = uniform
    How would the code change if p(s',r|s,a) is not deterministic?
    """

    grid = standard_grid()

    """
    States will be positions (i,j)
    Simpler than tic-tac-toe because we only have one "game piece"
    That can only be at one position at a time
    """

    states = grid.all_states()


    ###Uniformly Random Actions
    #initialize V(s) = 0

    V = {}
    for s in states:
        V[s] = 0

    gamma = 1.0 #Discount Factor
    #repeat until convergence

    while True:
        biggest_change = 0
        for s in states:
            old_v = V[s]

            #V(s) only has value if it's not a terminal state

            if s in grid.actions:

                new_v = 0 # we will accumulate the answer
                p_a = 1.0 / len(grid.actions[s]) # Each action has equal probability
                for a in grid.actions[s]:
                    grid.set_state(s)
                    r = grid.move(a)
                    new_v += p_a * (r + gamma * V[grid.current_state()])
                V[s] = new_v
                biggest_change = max(biggest_change, np.abs(old_v - V[s]))



            #print("V[s] :" + str(np.abs(old_v - V[s])))
            #print()
            #print("Biggest_Change :" + str(biggest_change))
        if biggest_change < SMALL_ENOUGH:
            break

        print()
        print("values for uniformly random actions:")
        print_values(V, grid)
        print("\n\n")
        print()

    ###Fixed Policy ###
    policy = {
        (2,0): 'U',
        (1,0): 'U',
        (0,0): 'R',
        (0,1): 'R',
        (0,2): 'R',
        (1,2): 'R',
        (2,1): 'R',
        (2,2): 'R',
        (2,3): 'U',
    }


    print_policy(policy, grid)

    #intialize V(s) = 0

    V = {}

    for s in states:
        V[s] = 0

    #Let's see how V(s) Changes as we get further away from the reward
    gamma = 0.9 #Discount Factor

    #repeat until convergence
    while True:
        biggest_change = 0
        for s in states:
            old_v = V[s]

        # V(s) only has value if it's not a terminal state
            if s in policy:
                a = policy[s]
                grid.set_state(s)
                r = grid.move(a)
                V[s] = r + gamma * V[grid.current_state()]
                biggest_change = max(biggest_change, np.abs(old_v - V[s]))

        if biggest_change < SMALL_ENOUGH:
            break

        print()
        print("Values for Fixed Policy:")
        print_values(V,grid)


























































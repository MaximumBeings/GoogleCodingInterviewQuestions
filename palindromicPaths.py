"""
Print all palindromic paths from top left to bottom
right in a matrix

input = MAT[][] = [['a','a','a','b], ['b','a','a','a'],['a','b','b','a']]
"""

input = [['a','a','a','b'], ['b','a','a','a'],['a','b','b','a']]

import random
def palindromicPath(input):
    input = [x for y in input for x in y]
    checker = True

    while checker == True:
        final = []
        indexes = range(len(input))
        for x in range(len(input)):
            y = random.sample(indexes,1)[0]
            final.append(input[y])
            if x > 0:
                if final[x-1] == final[x]:
                    checker = True
        checker = False

    return final

print(palindromicPath(input))

"""
['a', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'b', 'a', 'b', 'b']
"""
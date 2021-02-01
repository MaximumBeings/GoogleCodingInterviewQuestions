"""
Given a sequence of numbers a1,a2......an, find
the number of pairs(i,j) such that ai+aj = ai*aj
"""

input = [-2,2,4,2,0,1,-2,5,4,7,2,8,9,4]


def pairs(input):
    soln = set()
    for x in range(len(input)):
        restOftheList = input[x:].copy()
        for y in range(1,len(restOftheList)):
            if input[x]+restOftheList[y] == input[x]*restOftheList[y]:
                soln.add((input[x],restOftheList[y]))

    return soln

print(pairs(input))

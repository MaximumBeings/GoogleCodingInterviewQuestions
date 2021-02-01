"""
Given an array check whether there is a quadruplet which sums to a target.ArithmeticError

Time = O(n^2logN)
Space = O(n^2)

input: A = [1, 0, -1, 0, -2, 2]
target = 0
output = True

input: A = [1, 2, 3, 4, 5]
target = 9
output = False
"""

input = [1, 0, -1, 0, -2, 2]
"""
MITx via Edx
Data Science and Computational Thinking
John Guttag
"""
def powerSet(elts):
    if len(elts) == 0:
        return [[]]
    else:
        smaller = powerSet(elts[1:])
        elt = [elts[0]]
        withElt = []
        for s in smaller:
            withElt.append(s + elt)
        allofthem = smaller + withElt
        return allofthem

print(powerSet([1, 0, -1, 0, -2, 2]))
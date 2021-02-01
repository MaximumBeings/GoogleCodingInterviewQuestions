"""
Given a triangle, find the minimum path sum
from top to bottom. Each
step you may move to adjacent
numbers on the row below. Fro example, given
the following triangle

[
    [2],
   [3,4],
  [6,5,7]
 [4, 1, 8, 3]

]

The minimum path sum from top to
bottom is 11 (i.e., 2 + 3 + 5, 1 = 11)
"""

input = [[2],[3,4],[6,5,7],[4, 1, 8, 3]]

def shortestPathTriangle(input):
    return (sum([min(x) for x in input]))

print(shortestPathTriangle(input))

"""
11
"""

def shortestPathTriangle_2(input):
    sum = min(input[0])
    previousIndex = input[0].index(min(input[0]))
    for x in range(1,len(input)):
        subSet = input[x][min(0,previousIndex):max(previousIndex+1,len(input))]
        sum = sum + min(subSet)
        previousIndex = input[x].index(min(subSet))
    return sum

print(shortestPathTriangle_2(input))
"""
11
"""


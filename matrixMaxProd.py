"""
Maximun product of 4 adjacent elements in a matrix.

input = [[6, 2, 3, 4],
         [5, 4, 3, 1],
         [7, 4, 5, 6],
         [8, 3, 1, 0]]

output = 1860
"""

input = [[6, 2, 3, 4],[5, 4, 3, 1],[7, 4, 5, 6],[8, 3, 1, 0]]

def proDuct(input):
    if len(input) == 0:
        return 0
    ans = 1
    for x in input:
        ans = ans * x
    return ans

def matrixMaxProd(input):
    final =[]
    for i in range(len(input)):
        final.append(proDuct(input[i]))
        final.append(proDuct([row[i] for row in input]))
    return max(final)

print(matrixMaxProd(input))

"""
1680
"""
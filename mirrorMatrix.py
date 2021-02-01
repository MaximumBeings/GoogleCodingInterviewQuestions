"""
Mirror of matrix across diagonal

input = [[1,2,4],
         [5,9,0],
         [3,1,7]]

output = [[1,5,3],
          [2,9,1],
          [4,0,7]]
"""

input = [[1,2,4],
         [5,9,0],
         [3,1,7]]


def mirrorMatrix(input):
    final =[]
    for x in range(len(input)):
        final.append([row[x] for row in input])
    return final

print(mirrorMatrix(input))
"""
[[1, 5, 3], [2, 9, 1], [4, 0, 7]]
"""
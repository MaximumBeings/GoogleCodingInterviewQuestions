"""
Print all elements in sorted order from row and column wise sorted matrix

input = [[10, 20, 30, 40],
         [15, 25, 35, 45],
         [27, 29, 37, 48],
         [32, 33, 39, 50]]

output: [10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 39, 40, 45, 48,50]
"""

input = [[10, 20, 30, 40],
         [15, 25, 35, 45],
         [27, 29, 37, 48],
         [32, 33, 39, 50]]

answer = sorted([x for row in input for x in row])
print(answer)
"""
[10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 39, 40, 45, 48, 50]
"""
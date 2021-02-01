"""
Print the following pattern for given number of rows

input = 5

"""

input = [[x for x in range(5,0,-1)] for x in range(5)]

for x in range(len(input)):
    input[x][~x] = "*"
print(input)

"""
[[5, 4, 3, 2, '*'],
[5, 4, 3, '*', 1],
[5, 4, '*', 2, 1],
[5, '*', 3, 2, 1],
['*', 4, 3, 2, 1]]
"""
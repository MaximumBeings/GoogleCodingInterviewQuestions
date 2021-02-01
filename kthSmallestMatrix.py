"""
Given a n  * n matrix where each of the rows and columns are sorted
in ascending order. Find the kth smallest element in the matric. Note
that it is the kth smallest element in the sorted order not the kth
distinct element.

matrix = [[1,5,9],
          [10, 11, 13],
          [12, 13, 15]]

k = 8
return 13
"""
horizontalCounter = 0
verticalCounter = 2
vD = 1


matrix = [[1,5,9],
          [10, 11, 13],
          [12, 13, 15]]


def HorizontalNavigator(matrix):
    length = len(matrix)
    k = 0
    startH = 0
    startV = 0
    for l in range(0,1):
        for x in range(0,len(matrix[l])):
            matrix[l][x] = k
            k = k + 1
        for v in range(1,3):
            for y in range(0,1):
                matrix[v][y] = k
                k = k + 1

    for l in range(1,2):
        for x in range(1,len(matrix[l])):
            matrix[l][x] = k
            k = k + 1
        for v in range(2,3):
            for y in range(1,2):
                matrix[v][y] = k
                k = k + 1

    for l in range(2,3):
        for x in range(2,len(matrix[l])):
            matrix[l][x] = k
            k = k + 1
    for v in range(3,3):
            for y in range(2,3):
                matrix[v][y] = k
                k = k + 1

    return matrix





print(HorizontalNavigator(matrix))


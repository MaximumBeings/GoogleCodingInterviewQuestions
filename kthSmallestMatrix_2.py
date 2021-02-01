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
import copy
horizontalCounter = 0
verticalCounter = 2
vD = 1
matrix = [[1,5,9],
          [10, 11, 13],
          [12, 13, 15]]
matrix_2 = copy.deepcopy(matrix)

def HorizontalNavigator(matrix, kthElement):
    length = len(matrix)
    k = 1
    start = 0
    stop = 1
    while start <=2 and stop <= 3:
        for l in range(start,stop):
            for x in range(start,len(matrix[l])):
                matrix[l][x] = k
                k = k + 1
            for v in range(stop,len(matrix[l])):
                for y in range(start,stop):
                    matrix[v][y] = k
                    k = k + 1
            start = start + 1
        stop = stop + 1
    for g in range(len(matrix)):
        for h in range(len(matrix)):
            if matrix[g][h] == kthElement :
                print(("The " + str(kthElement) + \
                    " smallest element is: " + str(matrix_2[g][h])))
    return (("Matrix Order :" + str(matrix)))

print(HorizontalNavigator(matrix, 4))
print()
print(HorizontalNavigator(matrix, 8))
print()
"""
The 4 smallest element is: 10
Matrix Order :[[1, 2, 3], [4, 6, 7], [5, 8, 9]]
The 8 smallest element is: 13
Matrix Order :[[1, 2, 3], [4, 6, 7], [5, 8, 9]]
"""












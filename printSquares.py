"""
Print squares of diagonal elements in O(n) time complexity.
input: [[1,2,3],
        [4,5,6],
        [7,8,9]]
output: 1, 25, 81
        9, 25, 49
"""

input = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def printMatrix(input):
    stop = len(input) - 1
    final,temp,temp_2 = [],[],[]
    for x in range(0,len(input)):
        temp.append(input[x][x]*input[x][x])
        temp_2.append(input[x][stop-x]*input[x][stop-x])
    final.append(temp)
    final.append(temp_2)
    return final

print(printMatrix(input))

"""
[[1, 25, 81],
[9, 25, 49]]
"""
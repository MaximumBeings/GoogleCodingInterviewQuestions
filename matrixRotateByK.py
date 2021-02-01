"""
Rotate the matrix by k times:
input: [[12,23,34],
       [45,56,67],
       [78,89,91]]
output: [[23,34,12],
         [56,67,45],
         [89.91.78]]
"""

input = [[12,23,34],[45,56,67],[78,89,91]]

def matrixRotateByK(input,k):
    for i in range(k):
        temp_1 = [row[i] for row in input]
        temp_2 = [row[i+1] for row in input]
        for x in range(len(input)):
            input[x][i] = temp_2[x]
        for x in range(len(input)):
            input[x][i+1] = temp_1[x]
    return input

print(matrixRotateByK(input,2))

"""
[[23, 34, 12],
[56, 67, 45],
[89, 91, 78]]
"""
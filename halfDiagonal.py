"""
Check whether center elements of matrix equals sum of half diagonals.

input = [[2, 9, 1, 4, -2],
         [6, 7, 2, 11, 4],
         [4, 2, 9, 2, 4],
         [1, 9, 2, 4, 4],
         [0, 2 4, 2, 5]]

output = YES

Explanation: Sum of Half Diagonal 1 = 2 + 7 = 9
Explanation: Sum of Half Diagonal 2 = 9 + 0 = 9
Explanation: Sum of Half Diagonal 3 = 11 -2 = 9
"""
input = [[2, 9, 1, 4, -2],
         [6, 7, 2, 11, 4],
         [4, 2, 9, 2, 4],
         [1, 9, 2, 4, 4],
         [0, 2, 4, 2, 5]]

def halfDiagonal(input):
    centerElement = input[len(input)-3][2]
    diagonal = [input[i][i] for i in range(len(input))]
    counterDiagonal =  [input[i][~i] for i in range(len(input))]
    center = len(diagonal)%2 + 2
    if sum(diagonal[0:center-1]) == centerElement \
    and diagonal[center-1] == centerElement \
    and sum(diagonal[center:]) == centerElement and \
    sum(counterDiagonal[0:center-1]) == centerElement and \
    counterDiagonal[center-1] == centerElement and \
    sum(counterDiagonal[center:]) == centerElement:
        return "Yes"
    return "No"

print(halfDiagonal(input))
"""
Yes
"""

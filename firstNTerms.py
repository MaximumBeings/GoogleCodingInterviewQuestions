"""
Write a program to print the first x terms
of the series 3N + 2 which are not multiples of 4

Time = O(n)
Space = O(1)
input = 10
output = [5,11,14,17,23,26,29,35,38,41]
"""

length = 10
start = 1

answer = []
while len(answer) <= length:
    term = 3 * start + 2
    if (term % 4 != 0):
        answer.append(3 * start + 2)
    start = start + 1

print(answer)

"""
[5, 11, 14, 17, 23, 26, 29, 35, 38, 41, 47]
"""
"""
Given a number N, put all elements
from 1 to n in an array in order
1, 3....4,2

Time = O(n)
Space = O(1)

input = 9
output = [1,3,5,7,9,8,6,4,2]
"""

input = [x for x in range(1,10)]

max = float("-inf")
min = float("inf")

N = 9
answer = []
for x in range(0,len(input)):
    if input[x] % 2 == 1:
        if input[x] > max:
            max = input[x]
            answer.append(input[x])

for x in range(len(input)-1,-1,-1):
    if input[x] % 2 == 0:
        if input[x] < min:
            min = input[x]
            answer.append(input[x])

print(answer)

"""
[1, 3, 5, 7, 9, 8, 6, 4, 2]
"""


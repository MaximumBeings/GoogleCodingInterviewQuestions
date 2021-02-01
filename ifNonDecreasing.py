"""
Given an array with n integers, your task is to check if it could
become non-decreasing by modifying at most one element. We define an
array as non-decreasing if array[i] <= array[i + 1] holds for every
i ( 1 <= i  < n)

input: [4, 2, 3]
output: True

Explanation: You could modify the first 4 to 1 to get a
non-decreasingarray

input: [4,2,1]
output: False

Explanation: You can't get a non-decreasing array by modifying
at most one element.
"""
input = [4,2,3]
input2 = [4,2,1]

def ifNonDecreasing(input):
    for x in range(1,len(input)):
        if input[x-1] > input[x]:
            input[x-1] = input[x] - 1
        elif input[x] < input[x-1]:
            input[x] = input[x-1] + 1

    for x in range(1,len(input)):
        if input[x-1] > input[x]:
            return False
        else:
            return True
print(ifNonDecreasing(input))
print(ifNonDecreasing(input2))
"""
True
False
"""


"""
Given an array of integers. Find the first missing
positive integer in linear time and constant space.
In other words, find the lowest positive integer that
does not exist in the array. The array can contain
duplicates and negative numbers as well

Time: O(n)
Space: O(1)

input = [3, 4, -1, 1]
output = 2

input: [0,1,2]
output: 3
"""
input = [3, 4, -1, 1]
input1 = [0,1,2]
input2 = [10,11,1,2]

def missingPositive(input):
    missing = float("inf")
    for x in range(len(input)):
        if input[x] + 1 in input:
            pass
        elif input[x] < 0:
            pass
        else:
            if input[x] + 1 < missing:
                missing = input[x] + 1
    return missing

print(missingPositive(input))
print(missingPositive(input2))

"""
2
3
"""
"""
Check if reversing subarray makes the array sorted.

input = [1,2,5,4,3]
output = YES
"""
import copy
input = [1,2,5,4,3]

def sortSubArray(input):
    input_2 = copy.deepcopy(input)
    tester = copy.deepcopy(input)
    input.sort()
    for x in range(len(input)):
        for y in range(len(input)):
            tester[x:y].sort(reverse=True)
            if tester == input_2:
                return "YES"
            tester = copy.deepcopy(input_2)
    return "NO"

print(sortSubArray(input))
"""
YES
"""

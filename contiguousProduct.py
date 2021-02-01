"""
Contract:
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

input = [2, 3, -2, 4]
output = [6]

input = [-2, 0, -1]
output = 0
"""
input = [2, 3, -2, 4]
input1 = [-2, 0, -1]

def contiguousProduct(input):
    largestProduct = 0
    largestSubarray = [0]
    for x in range(1, len(input),1):
        soln = input[x-1] * input[x]
        if soln > largestProduct:
            largestProduct = soln
            largestSubarray = [input[x-1]*input[x]]
        else:
            pass
    return largestSubarray

print(contiguousProduct(input))
print(contiguousProduct(input1))

"""
[6]
[0]
"""
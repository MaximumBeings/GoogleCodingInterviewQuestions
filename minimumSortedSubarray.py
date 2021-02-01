"""
Given an integer array, you need to find one
contiuous subarray that if you only sort this
subarray in ascending order, then the whole
array will be sorted in ascending order, too.
You need to find the shortest such subarray and output
its length.

input = [2,6,4,8,10,9,15]
output = 5

Explanation:  You need to sorted [6,4,8,10,9] in ascending order to make
the whole array sorted in ascending order.
"""
input = [2,6,4,8,10,9,15]

import copy
import random

def isSorted(input):
    input = copy.deepcopy(input)
    for x in range(1,len(input)):
        for y in range(x,len(input)):
            if input[x-1] > input[x]:
                return False
    return True

def minimumSubArray(input):
    input_2 = copy.deepcopy(input)
    checker = 0
    length = 0
    sampleSubsets = [x for x in range(len(input_2))]
    ans = []
    while checker < 100:
        start = random.sample(sampleSubsets,1)[0]
        stop = random.sample(sampleSubsets[start:],1)[0]
        if stop > start:
            try:
                subToSort = input_2[start:stop]
                length = len(subToSort)
                subToSort.sort()
                input_2[start:stop] = subToSort
                if isSorted(input_2) == True:
                    ans.append(length)
            except:
                pass
        input_2 = copy.deepcopy(input)
        checker = checker + 1
    return min(ans)
print(minimumSubArray(input))
"""
5
"""


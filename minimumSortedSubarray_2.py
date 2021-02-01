"""
Find the length of unsorted subarray such that sorting this subarray can sort
all the array. Print the start and end index.

input = [10,12,20,30,25,40,32,31,35,50,60]
output = 3 8
"""
import copy

input = [10,12,20,30,25,40,32,31,35,50,60]

def isSorted(input):
    input = copy.deepcopy(input)
    for x in range(1,len(input)):
        if input[x-1] > input[x]:
            return False
    return True

def minimumSubArray(input):
    final = []
    input_2 = copy.deepcopy(input)
    for x in range(len(input)):
        input_2 = copy.deepcopy(input)
        start = x
        stop = len(input_2)+1-x
        subToSort = input_2[start:stop]
        unSortedSub = input_2[start:stop]
        subToSort.sort()
        input_2[start:stop] = subToSort
        if isSorted(input_2) == True:
            final.append(unSortedSub)
            input_2 = copy.deepcopy(input)
    shortestSub = final[0]
    for x in final:
        if len(x) < len(shortestSub):
            shortestSub = x
    start = input.index(shortestSub[0])
    stop = input.index(shortestSub[-1])
    return (start,stop)

print(minimumSubArray(input))
"""
(3, 8)
"""


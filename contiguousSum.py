"""
Contract:
Find the maximum sum contiguous subarray.

input = [1,2,3,4,-10]
output = 10

"""
input = [1,2,3,4,-10]
input2 = [1,2,3,4,-10,50,5,6,-70,300]
input3 =  [1,2,3,4,-10,50]


def contiguousSum(input):
    largestSum = 0
    final=[]
    largestSubarray = []
    start = 0
    for x in range(0, len(input),1):
        largestSubarray = input[start:x+1]
        if sum(largestSubarray) > largestSum:
            largestSum = sum(largestSubarray)
            largestSubarray = input[start:x+1]
        elif sum(largestSubarray) < largestSum:
            final.append(input[start:x])
            start = x
            largestSubarray = input[start:x+1]
            largestSum = sum(largestSubarray)
    final.append(input[start:x+1])
    return max([sum(k) for k in final])

print(contiguousSum(input))
print(contiguousSum(input2))
print(contiguousSum(input3))

"""
10
230
40
"""
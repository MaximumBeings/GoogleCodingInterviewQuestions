"""
Contract: Given an unsorted integer array find the first missing positive integer
"""
import numpy as np
input = [1,2,2,2,0,4,3,9]
input2 = [1,-11,0]
input3 = [-8,-7,-6]
input4 = [1,2,0]
input5 = [3,4,-1,1]
input6 = [-8,-7,-6,10]
input7 = [6,2,3,-30,5,-11,0]
input8 = [1,3,2,5]
input9 = [10 , 11 , 1 , 2 ]
def firstPositiveMissing(input):
    ans=0
    input = np.array(input)
    input = list(set(input[input > -1]))
    input = np.array(input)
    input = list(set(input[input > 0]))
    #Edge Cases:
    if len(input) == 0:
        return 1
    elif len(input) == 1 and input[0] == 1:
        return input[0] + 1
    elif len(input) == 1 and input[0] > 1:
        return min(1,input[0]-1)
    elif len(input) == 2 and input[0] > 1:
        return input[0] -1
    elif len(input) == 2 and input[1] - input[0] == 1:
        return input[1] + 1
    else:
    #Normal Cases:
        for x in range(1,len(input)):
            if input[x]-input[x-1] >1:
                break
    ans = input[x-1]+1
    return ans

print(firstPositiveMissing(input))
print(firstPositiveMissing(input2))
print(firstPositiveMissing(input3))
print(firstPositiveMissing(input4))
print(firstPositiveMissing(input5))
print(firstPositiveMissing(input6))
print(firstPositiveMissing(input7))
print(firstPositiveMissing(input8))
print(firstPositiveMissing(input9))


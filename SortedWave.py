"""
Contract:
Given an unsorted array nums reorder it such that
nums[0] < nums[1] > nums[2] < nums[3]

input = [1,5,1,1,6,4]
output = [1,4,1,5,1,6]

input2 = [1,3,2,2,3,1]
output2 = [2,3,1,3,1,2]
"""

input = [1,5,1,1,6,4]
input2 = [1,3,2,2,3,1]

def SortedWave(input):
    for x in range(0,len(input)-1):
        if x%2 != 0 :
           if input[x-1] >= input[x]:
                temp = input[x]
                input[x] = input[x+1]
                input[x+1] = temp
        if x%2 == 0 :
           if input[x-1] <= input[x]:
                temp = input[x]
                input[x] = input[x+1]
                input[x+1] = temp
    return input

print(SortedWave(input))
print(SortedWave(input2))

"""
[1, 5, 1, 6, 1, 4]
[3, 2, 1, 2, 1, 3]
"""
"""
Given an array of n integers nums and a target, find
the number of index triplets i, j, k that satisfy the
condition nums[i] + nums[j] + nums[k] < target.

input: nums = [-2, 0, 1, 3], and target = 2
output = 2

Explanation: Because there are two triplets which sums are
less than 2:

[-2, 0, 1]
[-2, 0, 3]
"""
target = 2
input = [-2, 0, 1, 3]

import random

def arrayTriplets(input, target):
    final, temp = [], []
    counter = 0
    while counter < 1000:
        temp.append(random.sample(input, 1)[0])
        temp.append(random.sample(input, 1)[0])
        temp.append(random.sample(input, 1)[0])
        if sum(temp) < target and \
        temp[0] < temp[1] < temp[2]:
            if temp not in final:
                final.append(temp)
        temp = []
        counter += 1
    return final

#print(arrayTriplets(input, target))

"""
[[-2, 0, 3], [-2, 0, 1]]
"""

def getTriplets(input):
    getTriplets, res = [],[]
    for x in range(len(input)):
        for y in range(x,len(input)):
            for z in range(y, len(input)):
                getTriplets.append(input[x])
                getTriplets.append(input[y])
                getTriplets.append(input[z])
                res.append(getTriplets)
                getTriplets=[]
    return res

print(getTriplets(input))
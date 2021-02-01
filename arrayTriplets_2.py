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

def getTriplets(input):
    getTriplets, res = [],[]
    for x in range(len(input)):
        for y in range(x,len(input)):
            for z in range(y, len(input)):
                getTriplets.append(input[x])
                getTriplets.append(input[y])
                getTriplets.append(input[z])
                if (getTriplets[0] != getTriplets[1] \
                and getTriplets[0] != getTriplets[2] \
                and getTriplets[1] != getTriplets[2]):
                    res.append(getTriplets)
                getTriplets=[]
    return res

def arrayTriplets(input, target):
    final = []
    toUse = getTriplets(input)
    for x in toUse:
        if x[0] < x[1] < x[2] and sum(x) < 2:
            final.append(x)
    return final
print(arrayTriplets(input, target))

"""
[[-2, 0, 1], [-2, 0, 3]]
"""
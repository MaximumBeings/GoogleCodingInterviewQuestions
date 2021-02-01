"""
Given an array of n integers nums and a target, find
the number of index triplets i, k, k with
0 <= i < < j < k < n that satisfy the condition nums[i]
+ nums[j] + nums[k] < target.

input: nums = [-2, 0, 1, 3], and target = 2
output = 2

Explanation: Because there are two triplets which sums are
less than 2:

[-2, 0, 1]
[-2, 0, 3]
"""
target = 2

import random
final, temp = [], []
counter = 0
while counter < 100:
    temp.append(random.sample(input, 1))
    temp.append(random.sample(input, 1))
    temp.append(random.sample(input, 1))
    if sum(temp) < target:
        final.append(temp)
    temp = []
    counter += 1
print(final)


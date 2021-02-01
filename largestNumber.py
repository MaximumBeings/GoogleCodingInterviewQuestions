"""
Given an array of numbers. Arrange the array
in such a way that it yields the largest number.

input = [54, 546, 548, 60]
output = [5485466054]

input = [900, 99, 90]
output = [999900]
"""

import copy
input = [54, 546, 548, 60]
input1 =  [900, 99, 90]

def largestNumber(input):
    final = ""
    temp = copy.deepcopy(input)

    for x in range(len(input)):
        final = final + str(max(temp))
        temp.remove(max(temp))

    return int(final)

print(largestNumber(input))
print(largestNumber(input1))

"""
5485466054
9009990
"""
"""
Given an integer array find the maximum product of a triplet
in array

Time => O(n)
Space => O(1)

input = [10,3,5,6,20]
output = 1200

input = [1,-4,3,-6,7,0]
output = 168
"""
import random

input = [10,3,5,6,20]
input2 = [1,-4,3,-6,7,0]

def maxProduct(input):
    maximum = float("-inf")
    counter = 0
    while counter < 100:
        x1 = random.sample(input,1)[0]
        x2 = random.sample(input,1)[0]
        x3 = random.sample(input,1)[0]
        if x1 != x2 and x1 != x3 and x2 != x3:
            temp = x1 * x2 * x3
            if temp > maximum:
                maximum = temp
        else:
            pass
        counter = counter + 1
    return maximum

print(maxProduct(input))
print(maxProduct(input2))

"""
1200
168
"""
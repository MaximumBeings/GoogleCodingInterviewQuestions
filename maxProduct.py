"""
Given an array that contains both positive and negative integers, find the
product of the maximum subarray.

Time = O(n)  Space = O(1)
input = [-2, 0, -1]  ; output = 0
input = [-1,6,2,0,7,9] ;output = 63
"""
input = [-2, 0, -1]
input2 = [-1,6,2,0,7,9]
input3 = [8,-3,6,3,-1,4,0,3]
input4 = [3,3,2,-1]
input5 = [-1,2,12,0]

def proDuct(input):
    if len(input) == 0:
        return 0
    ans = 1
    for x in input:
        ans = ans * x
    return ans

def maxProduct(input):
    maximum = float("-inf")
    Secondmaximum = float("-inf")
    counter = 0
    for x in range(0, len(input)):
        if proDuct(input[0:x]) > maximum :
            maximum = proDuct(input[0:x])
        elif proDuct(input[x:len(input)-x]) > maximum :
            maximum = proDuct(input[x:len(input)-x])
        elif proDuct(input[x:len(input)]) > Secondmaximum:
                Secondmaximum = proDuct(input[x:len(input)])
        elif proDuct(input[0:len(input)-x]) > Secondmaximum:
                Secondmaximum = proDuct(input[0:len(input)-x])
        counter = counter + 1
    return max(maximum, Secondmaximum)

print(maxProduct(input))
print(maxProduct(input2))
print(maxProduct(input3))
print(maxProduct(input4))
print(maxProduct(input5))

"""
0
63
1728
18
24
"""


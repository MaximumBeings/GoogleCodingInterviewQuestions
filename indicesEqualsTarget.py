"""
Given an array of integers and another non-negative integer k, find if
there exists 2 indices i and j such that A[i] - A[j] = k, i != j

Time = O(n)
Space = O(n)

input : A = [1,5,3], k = 2
output = True

input = [2,7,5] , k = 3
output = True

input = [1,7,6], k = 0
output = False

"""
input,input2, input3 = [1,5,3], [2,7,5], [1,7,6]
k1, k2, k3 = 2, 3, 0

import copy

def indicesEqualToTarget(input,k):
    temp = []
    for x in range(len(input[0:len(input)])):
        xinput = input[x+1:len(input)].copy()
        for y in xinput:
            temp.append(input[x])
            temp.append(y)
            if abs(temp[0] - temp[1]) == k:
                return True
            temp=[]
    return False


print(indicesEqualToTarget(input,k1))
print(indicesEqualToTarget(input2,k2))
print(indicesEqualToTarget(input3,k3))
"""
True
True
False
"""


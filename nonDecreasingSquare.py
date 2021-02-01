"""
Given an array of integers A sorted in a non-decreasing order.
Return an array of the squares of each number - also in
a sorted non-decreasing order.

input = [-4,-1,0,3,10]
"""


input = [-4,-1,0,3,10]
input2 = [-7,-3, 2, 3, 11]

def nonDecreasingSquare(input):
    sQ=[]
    sQ.append(input[0] * input[0])
    for x in range(1,len(input)):
        temp = input[x] * input[x]
        sQ.append(temp)
        for y in range(1,len(sQ)):
            if sQ[y-1] > sQ[y]:
                temp = sQ[y-1]
                sQ[y-1] = sQ[y]
                sQ[y] = temp
    return sQ

print(nonDecreasingSquare(input))
print(nonDecreasingSquare(input2))

"""
[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]
"""
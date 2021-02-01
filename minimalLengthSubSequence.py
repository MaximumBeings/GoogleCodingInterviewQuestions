"""
Given an array of n positive integers and a positive integer s. Find
the minimal length of a contiguous subarray of which the sum >= s.
If there isn't one return 0.ArithmeticError
input = s = 7; nums = [2,3,1,2,4,3]
output =2
"""

input = [2,3,1,2,4,3]
s = 7
def minimumArray(input,s):
    final=[]
    res = []
    for x in range(len(input)):
        res.append(input[x])
        if sum(res) >= s:
            final.append(res)
            res = []

    index=len(final[0])
    for x in final:
        if len(x) < index:
            index = x
    if len(index)==0:
        return 0
    return index

print(minimumArray(input,s))

"""
[4, 3]
"""
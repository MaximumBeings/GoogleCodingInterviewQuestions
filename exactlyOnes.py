"""
Given an array of integers in which two elements
appear exactly once and all other elements appear exactly
twice. Find the two elements that appear only once.

Time: O(n)
Space: O(1)

input = [1,3,5,7,9,1,5,9]
output = [[3, 7]]
"""

input = [1,3,5,7,9,1,5,9]

def exactlyOnes(input):
    temp = []
    for x in range(len(input)):
        try:
            temp.remove(input[x])
        except:
            temp.append(input[x])
    return temp

print(exactlyOnes(input))

"""
[3, 7]
"""
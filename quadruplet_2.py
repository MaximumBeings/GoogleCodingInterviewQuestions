"""
Given an array check whether there is a quadruplet which sums
to a target.

Time = O(n^2logN)
Space = O(n^2)

input: A = [1, 0, -1, 0, -2, 2]
target = 0
output = True

input: A = [1, 2, 3, 4, 5]
target = 9
output = False
"""

input =[1, 2, 3, 4, 5]
input2 = [1, 0, -1, 0, -2, 2]

def quadruplet(input, target):
    temp , final = [] , []
    input_2 = input[len(input)::-1]
    for x in range(len(input)):
        res = [input[x]]
        res_2 = [input_2[x]]
        for y in range(1,len(input),1):
            toUse = res + input[x+y:y+3+x]
            toUse2 = res_2 + input_2[x+y:y+3+x]
            if len(toUse) == 4 and sum(toUse) == target:
                return True
            if len(toUse2) == 4 and sum(toUse2) == target:
                return True
    return False

print(quadruplet(input, 9))
print(quadruplet(input2, 0))
print(quadruplet(input, 10))
"""
False
True
True
"""
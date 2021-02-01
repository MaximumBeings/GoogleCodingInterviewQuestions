"""
Contract:
Given an array nums of n integers where n > 1 return an array output such
that output[i] is equal to the product of all the lements of nums except nums[i]

input = [1,2,3,4]
output = [24,12,8,6]
"""
input = [1,2,3,4]
input2 = [2,3,4,5]
input3 = [10,11,12,13]

def multiply(input, k):
    input = input.copy()
    input.remove(k)
    product = 1
    for x in input:
        product = product * x
    res = [product]
    temp = []
    res = res + temp
    length = len(input)
    while length > 0:
        temp = [ input[0] * x for x in input if x != input[0]]
        res = res + temp
        input.remove(input[0])
        length = len(input)

    return res

print(multiply(input, 1))
print(multiply(input2, 2))
print(multiply(input3, 10))

"""
[24, 6, 8, 12]
[60, 12, 15, 20]
[1716, 132, 143, 156]
"""
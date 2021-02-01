"""
Given an array containing n distinct numbers taken from
0,1,2 ..... n, find the one that is missing from the
array

input = [3,0,1]
output = 2

input = [9,6,4,2,3,5,7,0,1]
output = 8
"""
input = [3,0,1]
input2 = [9,6,4,2,3,5,7,0,1]

def miSSing(input):
    for x in range(min(input), max(input), 1):
        try:
            input.index(x)
        except:
            return x

print(miSSing(input))
print(miSSing(input2))

"""
2
8
"""
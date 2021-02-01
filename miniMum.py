"""
Suppose an array sorted in ascending order is rotated at some pivot
unknown to you before hand i.e. [0,1,2,4,5,6,7] might become
[4,5,6,7,0,1,2]. Find the minimum element. You may assume no duplicate
exists in the array
"""

input = [3,4,5,1,2]
input2 = [4,5,6,7,0,1,2]

def miniMum(input):
    smallest = float("inf")
    for x in range(len(input)):
        if input[x] < smallest:
            smallest = input[x]

    return smallest

print(miniMum(input))
print(miniMum(input2))

"""
1
0
"""
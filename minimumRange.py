"""
There are N ranges to be divided into two non-empty subsets
such that each range is in exactly one of them and whenever two
ranges share a common point, they are in the same subset. It is
allowed to delete some ranges.  Find the minimum number of ranges
you can delete
"""

A = [1, 2, 3, 4]
B = [4, 5, 6, 7, 8]
input = [A,B]

def minimumRanges(input):
    final = []
    temp = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            for z in range(0,len(input)):
                if input[x][y] not in input[z]:
                    temp.append(input[x][y])
        final.append(temp)
        temp = []
    return final

print(minimumRanges(input))
"""
[[1, 2, 3], [5, 6, 7, 8]]
"""
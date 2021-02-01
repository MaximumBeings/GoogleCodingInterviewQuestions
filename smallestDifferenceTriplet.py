"""
Smallest difference triplet from these arrays.

input : A1 = [5, 2, 8]
        A2 = [10, 7, 12]
        A3 = [9, 14, 6]

output: 7 6 5

Note: Sort MAX-MIN of each array
// 8-2 = 6, 12-7=5, 14-6=7
"""
A1, A2, A3 = [5, 2, 8], [10, 7, 12], [9, 14, 6]
arrays = [A1, A2, A3]

def maxMinSortedArray(arrays):
    final = []
    for x in arrays:
        final.append(max(x) - min(x))
    final.sort(reverse = True)
    return final

print(maxMinSortedArray(arrays))

"""
[8, 6, 5]
"""
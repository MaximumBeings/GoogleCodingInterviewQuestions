"""
Given a non-empty array of numbers,
a0, a1, a2......where 0 <= ai < 2^31. Find
the maximum result of ai XOR aj, where
0 <= i, j < n. Could you do this in O(n) runtime?

input = [3, 10, 5, 25, 2, 8]
output = 28
"""
input = [3, 10, 5, 25, 2, 8]

def maximumXor(input):
    """
    O(n^2)
    """
    maxiMum = float("-inf")
    for x in range(len(input)):
        for y in range(len(input)):
            if input[x] ^ input[y] > maxiMum:
                maxiMum = input[x] ^ input[y]
    return maxiMum

print(maximumXor(input))

"""
28
"""

def maximumXor_2(input):
    """
    O(n)
    """
    maxiMum = float("-inf")
    for x in range(1,len(input)):
        if input[x-1] ^ input[x] > maxiMum:
            maxiMum = input[x-1] ^ input[x]
        elif input[x] ^ input[x-1]  > maxiMum:
            maxiMum = input[x] ^ input[x-1]
    return maxiMum

print(maximumXor_2(input))
"""
28
"""
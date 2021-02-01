"""
Equilibrium index of an array is an index i such that the sum
of elements at indices less than i is equal to the sum of elements
at indices greater than i. Find and return the equilibrium index of an
array. Element at index i is not included in either part. And
return -1 if no equilibrium index is present.

Time: O(n)
Space: O(n)

input = [3,11,15,12,6,13,10]
output = 3
"""

input = [3,11,15,12,6,13,10]


def equilibriumIndex(input):
    try:
        for x in range(1,len(input)):
            if sum(input[0:x])==sum(input[x+1:]):
                return x
    except:
        return -1

print(equilibriumIndex(input))

"""
3
"""
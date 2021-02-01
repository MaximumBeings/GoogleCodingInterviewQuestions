"""
Given a collection of distinct integers return all possible permutations.

input: [1, 2, 3]
output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""
import itertools
print(list(itertools.permutations([1, 2, 3])))
print()


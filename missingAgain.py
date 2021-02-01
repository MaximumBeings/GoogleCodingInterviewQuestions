"""
Given an array of integers where 1 <= a[i] <= n
(n = size of array), some elements appear twice and
others appear once.  Find all the elements of [1,n]
inclusive that do not appear in this array. Could you do
it without extra space and O(n) runtime? You may assume the
returned list does not count as extra space.
"""
input = [4,3,2,7,8,2,3,1]

def missingAgain(input):
    return [x for x in range(1, len(input) + 1) if x not in input]

print(missingAgain(input))
"""
[5, 6]
"""
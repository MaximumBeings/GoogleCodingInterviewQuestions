"""
Given two integers n and k, return all possible
combinations of k numbers out of 1....n.
input : n 4, k = 2
output:
[[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4]]
"""


def combination_k(n,k):
    res = []
    temp = []
    for x in range(1,n+1,k-1):
        for y in range(x,n,1):
         temp.append(x)
         temp.append(y+1)
         res.append(temp)
         temp=[]
    return res

print(combination_k(4,2))
print(combination_k(5,3))
"""
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
"""
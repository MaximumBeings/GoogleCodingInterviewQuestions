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
    input = [x+1 for x in range(n)]
    for x in range(len(input[0:n])):
        xinput = input[x+1:n].copy()
        for y in xinput:
            temp.append(input[x])
            temp.append(y)
            res.append(temp)
            temp=[]
    return res


print(combination_k(4,2))
print(combination_k(5,3))
"""
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
[[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
"""
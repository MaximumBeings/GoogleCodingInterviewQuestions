"""
Given a set of distinct positive integers, find the largest subset such that every pair
(Si,Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.If there are
multiple solutions, return any subset.
input = [1,2,3]  output = [1,2] or [1,3]
input = [1,2,4,8]  output = [1,2,4,8]
"""
import copy
def getPairs(input):
    getPairs, res = [],[]
    for x in range(len(input)):
        for y in range(x,len(input)):
            if input[x] != input[y]:
                if input[y]%input[x] == 0:
                    getPairs.append(input[x])
                    getPairs.append(input[y])
                    res.append(getPairs)
                    getPairs=[]
    return res
def module(input):
    input = copy.deepcopy(input)
    pairs = getPairs(input)
    ans , temp = [], set()
    for x in range(len(pairs)):
        for y in range(x,len(pairs)):
            if pairs[y][0]%pairs[x][0] == 0 and pairs[y][1]%pairs[x][1] == 0 :
                if pairs[x][0] not in temp and pairs[x][1] not in temp \
            and pairs[y][1]%pairs[y][1] == 0:
                    temp.add(pairs[x][0])
                    temp.add(pairs[x][1])
                elif pairs[x][1]%pairs[y][1] ==0:
                    temp.add(pairs[y][0])
                    temp.add(pairs[y][1])
        toUse = list(temp)
        toUse.sort()
        if toUse not in ans:
            ans.append(toUse)
        temp = set()
    return ans
print(module([1,2,4,8,9,10,5,6,700]))
print(module([1,2,4,8]))
print(module([1,2,3]))
"""
[[1, 2], [1, 2, 4], [1, 2, 4, 8], [1, 9], [1, 2, 10], [2, 4], [2, 4, 8], [2, 10], [4, 8]]
[[1, 2], [1, 2, 4], [1, 2, 4, 8], [2, 4], [2, 4, 8], [4, 8]]
[[1, 2], [1, 3]]
"""




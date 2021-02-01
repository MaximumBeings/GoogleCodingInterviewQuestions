"""
Contract:
Given a non-empty array of integers return the k most frequent elements
input = [1,1,1,2,2,3], k=2
output = [1,2]
input = [1], k =1
output = [1]
Note: You may assume k is always valid, 1 <= k <= mumber of unique elements.
Your algorithm's time comnplexity  must be better than 0(n log n) where n is
the array's size.
"""
input = [1,1,1,2,2,3]
k = 2
input2 = [1]
k = 1
input3 = [1,1,5,5,6,7,7,7,7,7,7,7,7,7]
k = 4

def nonEmptyArray(input,k):
    soln = {}
    res = []
    for x in input:
        try:
            soln[x] = soln[x] + 1
        except:
            soln[x] = 1
        if soln[x] >= k and x not in res:
            res.append(x)
    return res

print(nonEmptyArray(input,2))
print(nonEmptyArray(input2,1))
print(nonEmptyArray(input3,2))

"""
[1, 2]
[1]
[1, 5, 7]
"""
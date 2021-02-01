"""
Given a sorted array, two integers k and x,
find the k closest elements to x in the array.
The result should also be sorted in ascending order.
If there is a tie, the smaller elements are always
preferred.

input = [1,2,3,4,5], k=4, x=3
output = [1,2,3,4]

input = [1,2,3,4,5], k=4, x=-1
output = [1,2,3,4]
"""
input = [1,2,3,4,5]


k=4
x=-1

def kthSmallest(input,k,x):
    res = []
    final = []
    for y in input:
        res.append(y-x)
    for g in range(k):
        index = res.index(min(res[g:k]))
        final.append(input[index])
    return final

print(kthSmallest(input,4,3))
print(kthSmallest(input,4,-1))
print(kthSmallest(input,3,-2))

"""
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3]
"""
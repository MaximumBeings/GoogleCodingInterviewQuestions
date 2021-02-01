"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in
the sorted order not the kth distinct element.

input: [3,2,1,5,6,4] and k= 2
output: 5

input: [3,2,3,1,2,4,5,5,6] and k=4
output: 4

Note:  You may assume k is always valid 1 <= k <= array's length
"""

def kthLargest(input,k):
    input = input.copy()
    for x in range(k,0,-1):
        ans = max(input)
        input.remove(ans)
    return ans


#Sample Call
print( kthLargest([3,2,1,5,6,4],2))
print()
print( kthLargest( [3,2,3,1,2,4,5,5,6],4))

"""
5

4
"""


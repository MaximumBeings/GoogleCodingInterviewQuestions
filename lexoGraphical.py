"""
Given an array of integers return all
numbers from 1 to n in lexicographical order.

input n = 13
output = [1,10,11,12,13,2,3,4,5,6,7,8,9]
"""

def lexoGraphical(n):
    final = [0]*n
    rank = 0
    count = int(n%10)+2
    for x in range(0,n+1):
        if x == 0:
            final[x] = x+1
        elif x >=10:
            rank=x%10+1
            final[rank] = x
        elif x < 10 and x > 1:
            final[count] = x
            count = count + 1
    return final

print(lexoGraphical(13))
print(lexoGraphical(19))

"""
[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 5, 6, 7, 8, 9]
"""
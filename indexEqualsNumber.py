"""
Given an aray of n distinct integers sorted in ascending order.
Write a function that returns a Fixed Point in the array. Fixed Point in
an array is an index i such that arr[i] is equal to i. If there is no
fixed point return -1.

Time: O(logN)
Space: O(1)

input = [-10,-5,0,3,7]    output = 3
input = [0,2,5,8,17]       output = 0
input = [-10,-5,3,4,7,9]  output= -1 #No Fixed Point
"""
input, input2, input3 = [-10,-5,0,3,7], [0,2,5,8,17], [-10,-5,3,4,7,9]

def indexEqualsNumber(input):
    ans = [x for x in range(len(input)) if input[x]==x]
    if len(ans)==0:
        return -1
    return ans[0]

print(indexEqualsNumber(input))
print(indexEqualsNumber(input2))
print(indexEqualsNumber(input3))

def indexEqualsNumber_2(input):
    for x in range(len(input)):
        if x == input[x]:
            return x
    return -1

print(indexEqualsNumber_2(input))
print(indexEqualsNumber_2(input2))
print(indexEqualsNumber_2(input3))

def indexEqualsNumber_3(input):
    for x in range(len(input)):
        try:
            if x == input.index(x):
                return x
        except:
            pass
    return -1

print(indexEqualsNumber_3(input))
print(indexEqualsNumber_3(input2))
print(indexEqualsNumber_3(input3))
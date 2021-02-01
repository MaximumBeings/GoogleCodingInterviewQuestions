
"""
Contract:
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters
1 or 0
"""
a = "11"
b = "1"
c = "1010"
d = "11"
e = "100101"
f = "10101"
g = "1010"
h = "1011"

def biNary(a,b):
    if len(a) > len(b):
        length = len(a)
    else:
        length = len(b)
    lst = [a,b]
    lst = ['0' * (length - len(i)) + i for i in lst]
    a = lst[0]
    b = lst[1]
    res = ""
    carry = 0
    for x in range(length-1,-1,-1):
        temp = int(a[x]) + int(b[x]) + carry
        if temp == 0  or temp == 1:
            carry = 0
            res = res + str(temp)
        elif temp > 1:
            carry = 1
            temp = 0
            res = res + str(temp)
    if carry == 0:
        pass
    else:
        res = res + str(1)
    return res[::-1]
print(biNary(a,b))
print(biNary(c,d))
print(biNary(e,f))
print(biNary(g,h))
"""
100
1101
111010
10101
"""




"""
For a given Number N find if is colorful. A number is called
colorfulif the product of every digit of a contiguous subsequence is
different.

For Example:

N = 234
2 -> 2
3 -> 3
4 -> 4
23 -> 6
34 -> 12
234 -> 24
output = True

input: N = 11
output = False
"""

def colorful(input):
    input = str(input)
    temp, final = [], [],
    for x in range(len(input)):
        factor = int(input[x])
        if int(input[x]) in temp:
            return False
        temp.append(int(input[x]))
        for y in range(x+1,len(input)):
            factor = factor * int(input[y])
            if factor in temp:
                return False
            temp.append(factor)
    return True
print(colorful(2345))
print(colorful(11))
"""
True
False
"""
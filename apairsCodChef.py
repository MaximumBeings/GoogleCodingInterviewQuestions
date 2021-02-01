"""
Given two numbers, arrange the digits of the second number in such a way
that the sum of the absolute differences of their corresponding digits is minimum
possible for this pair

3178    03178   03178
10920   10920   01029

|0-0| + |3-1| + |1-0| + |7-2| + |8-9| =  9
"""
import random

a = "3178"
b = "10920"

def aiPairs(a,b):
    if len(a) > len(b):
        length = len(a)
    else:
        length = len(b)
    lst = [a,b]
    lst = ['0' * (length - len(i)) + i for i in lst]
    a = lst[0]
    b = lst[1]
    a = [a for a in a]
    b = [b for b in b]

    counter = 0
    sum=0
    biggestSum = float("inf")
    soln=[]
    while counter < 200:
        L = random.sample(b,len(b))
        for x in range(len(L)):
            sum = sum + abs(int(a[x])-int(L[x]))
        if sum < biggestSum:
            soln = L
            biggestSum = sum
        sum = 0
        counter = counter + 1
    final = {}
    final[biggestSum] = soln
    return final

print(aiPairs(a,b))
"""
{9: ['0', '2', '1', '0', '9']}
"""
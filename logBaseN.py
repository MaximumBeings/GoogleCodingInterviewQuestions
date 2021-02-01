"""
Given two values of x and n returns Log of X to the base N.

input: x=8,n=2

output = 3

input: x = 1000000000000
n = 12
"""
import copy
import random

def proDuct(input):
    if len(input) == 0:
        return 0
    ans = 1
    for x in input:
        ans = ans * x
    return ans

def logBaseN(x,n):
    divisor = n
    tracker = x
    count = 0
    checker = 200
    answer = []
    while checker > 0:
        answer.append(divisor)
        tracker = tracker - (tracker/divisor)
        count = count + 1
        if proDuct(answer)==x:
            return count
        checker = checker - 1

print(logBaseN(8,2))
print(logBaseN(1000000000000,10))

"""
3
12
"""

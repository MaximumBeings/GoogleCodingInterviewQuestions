import copy
import random

def proDuct(input):
    if len(input) == 0:
        return 0
    ans = 1
    for x in input:
        ans = ans * x
    return ans

def pRime(n):
    soln = [2]
    for x in range(2,n):
        if x%2 != 0:
            soln.append(x)
    temp = copy.deepcopy(soln)
    res = []
    for x in range(len(soln)):
        if n%soln[x] == 0:
            res.append(soln[x])
            try:
                for y in soln:
                    if soln[x]%y == 0 and soln[x] != y:
                        res.remove(soln[x])
            except:
                pass
    checker = 200
    answer = []
    divisor = 0
    tracker = n
    while checker > 0:
        divisor = random.sample(res,1)[0]
        if tracker%divisor == 0:
            answer.append(divisor)
            tracker = tracker - (tracker/divisor)
            if proDuct(answer)==n:
                return answer
        elif tracker%divisor != 0:
            tracker = n
            answer=[]
        checker = checker - 1
    return answer

print(pRime(54))
print(pRime(120))
print(pRime(2560))
"""
[2, 3, 3, 3]
[2, 2, 2, 5, 3]
[5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 5, 2]
"""
"""
Count the number of prime numbers in n
"""

def pRime(n):
    soln = [2]
    for x in range(2,n):
        if x%2 != 0:
            soln.append(x)
    toRemove = []
    for x in range(len(soln)):
        for y in range(x+1, len(soln)):
            if soln[y]%soln[x]==0:
                toRemove.append((soln[y]))
    soln = [x for x in soln if x not in toRemove]
    return soln


print(pRime(10))
print(pRime(20))
print(pRime(30))
print(pRime(40))
print(pRime(50))
print(pRime(60))
print(pRime(70))
print(pRime(80))
print(pRime(90))
print(pRime(100))

"""
[2, 3, 5, 7, 11, 13, 17, 19]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
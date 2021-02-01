"""
Print a matrix in a spiral form.
input = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]

output = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
"""
input = [[1,  2,  3,  4, 5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

final = []

def printRight(holdconstant,toPrint):
    for x in range(holdconstant, toPrint):
        if input[holdconstant][x] not in final:
            final.append(input[holdconstant][x])
    return x

def printDown(holdconstant,toPrint):
    for x in range(toPrint):
        if input[x][holdconstant] not in final:
            final.append(input[x][holdconstant])
    return x

def printLeft(holdconstant,toPrint):
    for x in range(toPrint,-1,-1):
        if input[holdconstant][x] not in final:
            final.append(input[holdconstant][x])
    return x

def printUp(holdconstant,toPrint):
    for x in range(toPrint-1,0,-1):
        if input[x][holdconstant] not in final:
            final.append(input[x][holdconstant])
    return x

def mainFunction(input):
    toPrint = len(input[0])-1
    try:
        for x in range(toPrint):
            holdconstant = x
            holdconstant=  printRight(holdconstant,toPrint)+1
            holdconstant = printDown(holdconstant,toPrint) +1
            holdconstant = printLeft(holdconstant,toPrint)
            if x+1==toPrint:
                holdconstant = holdconstant + 1
            holdconstant = printUp(holdconstant,toPrint)
    except:
        pass
    return final
print(mainFunction(input))

"""
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
"""











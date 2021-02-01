"""
Find number of pairs (x,y) in an array such that
x^y > y^x
"""
inputX = [2, 1, 6]
inputY = [1,5]
def getPairs(input):
    getPairs, res = [],[]
    for x in range(len(inputX)):
        for y in range(len(inputY)):
            if inputX[x]**inputY[y] > inputY[y]**inputX[x]:
                getPairs.append(inputX[x])
                getPairs.append(inputY[y])
                res.append(getPairs)
                getPairs=[]
    return res


print(getPairs(input))
"""
[[2, 1], [2, 5], [6, 1]]
"""




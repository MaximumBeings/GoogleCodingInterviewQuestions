"""
Given a 2D binary matrix filled with 0's and 1's find the largest square
containing only 1's and return its area.
"""
        # 0 1 2 3 4
input = [[1,0,1,0,0], #0
         [1,0,1,1,1], #1
         [0,1,1,1,1], #2
         [1,0,0,1,0]] #3

def sQuare(input):
    res = []
    for x in range(0,len(input)-1):
        for y in range(0,len(input)-1):
            if input[x][y] == 1 and input[x][y+1]==1 and \
            input[x+1][y]==1 and input[x+1][y+1]==1:
                temp = []
                res.append([x,y])
                res.append([x,y+1])
                res.append([x+1,y])
                res.append([x+1,y+1])
    return res

ans = sQuare(input)

def printIndices(ans):
    print()
    print("The indices of cells with contiguous values of 1 are:")
    print()
    dim = 2
    for x in range(0,len(ans),2):
        print(ans[x:dim])
        dim = dim + 2
        print()

printIndices(ans)

def getIndexValues(ans):
    print("The values at the indices are:")
    print()
    res = []
    temp = []
    counter = 1
    for x in range(0,len(ans),1):
        temp.append(input[ans[x][0]][ans[x][1]])
    dim = 2
    for x in range(0,len(ans),2):
        res.append(temp[x:dim])
        dim = dim + 2
    return res

print(getIndexValues(ans))








"""
Find if there is a rectangle in binary matrix with corners as 1

input = [[1,0,0,1,0],
         [0,0,1,0,1],
         [0,0,0,1,0],
         [1,0,1,0,1]]
output = "Yes"
Note: [[1,0,1],
       [0,1,0],
       [1,0,1]]
Exists
"""
input = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
import random
def binaryMatrix(input):
    final = []
    counter = 0
    indicesX = [x for x in range(len(input))]
    indicesY = [y for y in range(len(input))]
    while counter < 20000:
        x1 = random.sample(indicesX,1)[0]
        x2 = random.sample(indicesX,1)[0]
        y1 = random.sample(indicesY,1)[0]
        y2 = random.sample(indicesY,1)[0]
        if input[x1][y1] == 1 and input[x1][y2]==1 and \
           input[x2][y1] == 1 and input[x2][y2]==1 and \
           x1 != y2 and x1 != y1 and x2 > x1 :
               final.append(input[x1][y1:])
               final.append(input[x2-x1][y1:])
               final.append(input[x2][y2:])
               if final[0][0] == 1 and final[0][-1] == 1 and \
               final[len(final)-1][0] == 1 and final[len(final)-1][-1] == 1\
               and len(final[0]) == len(final[-1]):
                   print(input[x1][y1:])
                   print(input[x2-x1][y1:])
                   print(input[x2][y2:])
                   print()
                   return "Yes"
        counter = counter + 1
    return "No"

def tester():
    for x in range(100):
     ans = binaryMatrix(input)
     if ans == "Yes":
         return "Yes"
    return "No"
print(tester())

"""
[1, 0, 1]
[0, 1, 0]
[1, 0, 1]

Yes
"""
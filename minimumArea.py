"""
Given a set of points in the xy-plane, determine the
minimum area of a rectangle formed from these points,
with sides parallel to the x and y axes.  If there isn't any rectangle , return 0

input: [[1,1], [1,3], [3,1], [3,3],[2,2]]   |||| output: 4

[[1,1]    [1,3]]
[[3,1]]   [3,3]]   ##[2,2] is not useful as a rectangle must be a straightline vertically and
horizontally

input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]   |||| output: 2
[[1,1]    [1,3]]     or   [[1,1], [1,3]]
[[3,1]]   [3,3]]           [4,1], [4,3]]

"""
import copy
def minimumAreaRectangle(input, minOrMax):
    input = copy.deepcopy(input)
    horizontalIndices = []
    verticalIndices = []
    minimumWidth = [x[0] for x in input]
    minimumWidth = min(minimumWidth)
    width = [x for x in input if x[0] == minimumWidth]
    firstWidth = width[1][1] - width[0][1]
    for x in width:
        input.remove(x)
    temp = []
    ans = []
    for x in range(len(input)-1):
        if input[x][0] == input[x+1][0]:
            temp.append(input[x])
            temp.append(input[x+1])
            ans.append(temp)
            temp=[]
    ans = copy.deepcopy(ans[0:])
    height = []
    for x in range(len(ans)):
        height.append(ans[x][0][0] - width[0][1])
    if minOrMax == "min":
        return (firstWidth * min(height))
    elif minOrMax == "max":
        return firstWidth * max(height)

input = [[1,1], [1,3], [3,1], [3,3],[2,2]]
print("Minimum Possible Area of the Rectangle  : " + str(minimumAreaRectangle(input, "min")))
print("Maxiumum Possible Area of the Rectangle : " + str(minimumAreaRectangle(input, "max")))
print()
input = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
print("Minimum Possible Area of the Rectangle  : " + str(minimumAreaRectangle(input, "min")))
print("Maxiumum Possible Area of the Rectangle : " + str(minimumAreaRectangle(input, "max")))
"""
Minimum Possible Area of the Rectangle  : 4
Maxiumum Possible Area of the Rectangle : 4

Minimum Possible Area of the Rectangle  : 4
Maxiumum Possible Area of the Rectangle : 6
"""
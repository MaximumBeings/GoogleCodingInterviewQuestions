"""
Given a matrix where every cell has some number of coins.
Count the number of ways to reach bottom right from top
left with exactly k coins.
input : k = 12
mat = [[1,2,3],
         [4,6,5],
         [3,2,1]]
output: 2
Explanation: 1 -> 2 -> 6 -> 2 -> 1
             1 -> 2 -> 3 -> 5 -> 1
Note: We can move to (i+1, j) and (i, j+1) from a cell (i,j)
"""
input = [[1,2,3],[4,6,5],[3,2,1]]
import random
def randomShortestPath(input, target):
    final, count = [],0
    while count < 200:
        xLoc, yLoc, reward = 0,0, []
        reward.append(input[xLoc][yLoc])
        locationTrajectory = []
        locationTrajectory.append([xLoc,yLoc])
        while len(locationTrajectory) > 0:
            direction = random.sample(['R','D'],1)[0]
            if direction == 'R':
                try:
                    reward.append(input[xLoc][yLoc+1])
                    xLoc = xLoc
                    yLoc = yLoc + 1
                    locationTrajectory.append([xLoc,yLoc])
                except:
                    pass
            if direction == 'D':
                try:
                    reward.append(input[xLoc+1][yLoc])
                    xLoc = xLoc+1
                    yLoc = yLoc
                    locationTrajectory.append([xLoc,yLoc])
                except:
                    pass
            if locationTrajectory[-1] == [2,2]:
                break
        count = count + 1
        if sum(reward) == target:
            if reward not in final:
                final.append(reward)
    return final
print(randomShortestPath(input,12))
"""
[[1, 2, 3, 5, 1], [1, 2, 6, 2, 1]]
"""


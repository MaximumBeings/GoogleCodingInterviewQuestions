"""
Given a m X n grid filled with non-negative numbers, find a path
from left to bottom right which minimizes the sum of all numbers
along its path. Note: You can only move either down or right at any
point in time.
        # 0 1 2
input = [[1,3,1],0
         [1,5,1],1
         [4,2,1]]2
output = 7
"""
input = [[1,3,1],
         [1,5,1],
         [4,2,1]]
import random
def randomShortestPath(input):
    count = 0
    ans={}
    biggestCost = float("inf")
    while count < 20:
        xLoc = 0
        yLoc = 0
        reward = []
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
        if sum(reward) < biggestCost:
            ans={}
            ans[sum(reward)]=locationTrajectory
            biggestCost = sum(reward)
    return ans
print(randomShortestPath(input))
"""
{7: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]}
"""


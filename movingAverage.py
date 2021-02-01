"""
Given a stream of integers - calculate the moving average given k
"""

input = [1,2,3,4,5,6,7,8,9,10]

def movingAverage(input,k):
    res = []
    counter = k
    for x in range(k,len(input)):
        res.append(sum(input[0:x])/counter)
        counter=counter+1
    return res


print(movingAverage(input,1))
print(movingAverage(input,2))
print(movingAverage(input,3))
print(movingAverage(input,4))
print(movingAverage(input,5))

"""
[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
[1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
[2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
[2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
[3.0, 3.5, 4.0, 4.5, 5.0]
"""
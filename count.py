"""
input : [1,2,3,1,1]
output: 1

contract: return n if count(n)/len(input) > 1/3
          otherwise return -1
"""
input = [1,2,3,1,1]
testInput = [4,3,5,7,7,12,13,12,4,4,12,12,12,12,4,4,4]
testInput2 = [4,3,5,7]
testInput3 = [4,4,4,4,3,3,2,2,2]


def counter(input):
    inputSet = list(set(input))
    outPut = []
    for x in inputSet:
        if input.count(x)/len(input) > 1.0/3.0:
            outPut.append(x)
    if len(outPut) > 0:
        return outPut
    return -1

print(counter(input))
print(counter(testInput))
print(counter(testInput2))
print(counter(testInput3))
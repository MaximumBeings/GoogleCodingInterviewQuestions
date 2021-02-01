"""
Contract:
Given an unsorted array of integers, find the length of the
longest increasing subsequence
input = [10,9,2,5,5,3,7,101,18]
"""
input = [10,9,2,5,5,3,7,101,18]
input2 = [2,5,5,3,7,101,18]
input3 = [[8,-3,6,3,-1,4,0,3]]

def swap(x,y):
    res = []
    temp = y
    y = x
    x = temp
    return [x,y]

def increasingSubSequence(input):
    res = []
    soln = [input[0]]
    for x in range(1,len(input)-1,1):
        if input[x]<input[x-1]:
            soln=[]
        if input[x]>input[x-1] or input[x+1]>input[x]:
            soln.append(input[x])
            try:
                if soln[-2] > soln[-1] and input[x]:
                    test = swap(soln[-2],soln[-1])
                    soln[-2] = test[0]
                    soln[-1] = test[1]
            except:
                pass
        if soln not in res:
            res.append(soln)
        longest = max([len(x) for x in res])
        toReturn = [x for x in res if len(x) == longest]
    return toReturn
print(increasingSubSequence(input))
print(increasingSubSequence(input2))
print(increasingSubSequence(input3))
"""
[3, 7, 101]
[3, 7, 101]
[0, 2, 3, 4, 5]
"""






"""
Given a value n print the following pattern till n rows
1
1 1
2 1
1 2 1 1
1 1 1 2 2 1
3 1 2 2 1 1
"""

def stringBreaker(input):
    toUse = str(input)
    final = []
    runningString = ""
    finalString=""
    count = 0
    runningString = runningString + str(toUse[0])
    count = count + 1

    for string in range(1,len(toUse)):
        if toUse[string] == runningString:
            runningString = runningString + toUse[string]
            count = count + 1
        elif toUse[string] != runningString :
            finalString = finalString + str(count)
            finalString = finalString +  runningString
            count = 1
        runningString = ""
        runningString = runningString + toUse[string]

    finalString = finalString + str(count)
    finalString = finalString +  runningString
    return finalString

def conWaySequence(n):
    final = [1]
    for x in range(1, n):
        toAppend = stringBreaker(final[x-1])
        final.append(toAppend)
    return final

#print(conWaySequence(6))
xyz = conWaySequence(16)

for x in xyz:
    print(x)

"""
[1, '11', '21', '1211', '111221', '312211']
[1, '11', '21', '1211', '111221', '312211', '13112221', '1113213211', '31131211131221', '13211311123113112211']
"""
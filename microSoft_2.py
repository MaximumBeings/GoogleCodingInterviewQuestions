input , input5 = [51, 71, 17, 42], [5,9,6,8]
input2, input3 = [42, 33, 60], [51, 32, 43]
input4, input6 = [598888888,688888888,5988888881111,6888888881111], [59,68]

def stringAdder(digit):
    digit = str(digit)
    temp = 0
    res = [temp + int(x) for x in digit]
    return sum(res)

def stringChecker(input):
    res = [stringAdder(str(input[0]))]
    for x in range(1,len(input)):
       t =  stringAdder(str(input[x]))
       if t not in res:
           pass
       elif t in res:
           res.append(t)
    if len(res) == 1:
        return False
    else:
        return True

def microSoftInteger(input):
    max_ = 0
    temp = []
    if stringChecker(input) != False:
        for x in range(0, len(input),1):
            toUse = stringAdder(str(input[x]))
            for y in range(1,len(input),1):
                toUse2 = stringAdder(input[y])
            if toUse == toUse2 :
                temp.append(input[x] + input[y])
                break
    if len(temp) != 0:
        return max(temp)
    return -1
#Sample Calls
print(microSoftInteger(input))
print(microSoftInteger(input2))
print(microSoftInteger(input3))
print(microSoftInteger(input4))
print(microSoftInteger(input5))
print(microSoftInteger(input6))
"""
93, 102, -1, 12877777762222, -1,127
"""
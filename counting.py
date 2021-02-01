"""
Contract:
Given a non-empty array of integers, every element
appears three times except for one which appears exactly
once. Find that single one
"""

input = [2,2,2,3]
input2 = [0,1,0,1,0,1,99]


def counTer(input):
    return [x for x in input if input.count(x) == 1][0]

print(counTer(input))
print(counTer(input2))
print("")

"""
3
99
"""

"""
Contract:
Given a non-empty array of integers, every element
appears three times except for one which appears exactly
once. Find that single one
"""

input = [2,2,3]
input2 = [0,1,0,1,0,1,99]

def counTer2(input):
    res = dict.fromkeys(input, 0)
    for x in input:
        if x in res:
            res[x] = res[x] + 1
        try:
            if res[x] > 1:
                res.pop(x)
        except:
            pass
    return list(res.keys())[0]

print()
print(counTer2(input))
print(counTer2(input2))

"""
3
99
"""
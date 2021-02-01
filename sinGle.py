"""
Given a non-empty array of integers, every element appears twice except
for one. Find that single one.
"""
input = [2,2,1]
input2  = [4,1,2,1,2]

def sinGle(input):
    res = {}
    for x in range(len(input)):
        try:
            res[input[x]] = res[input[x]] + 1
            if res[input[x]] > 1:
                del res[input[x]]
        except:
            res[input[x]] = 1

    return res

print(sinGle(input))
print(sinGle(input2))

"""
{1: 1}
{4: 1}
"""
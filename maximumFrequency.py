"""
Sum of all maximum frequency elements in a Matrix

input =[[1,1,1],
        [2,3,3],
        [4,5,3]]

output = 12
"""
input =[[1,1,1],
        [2,3,3],
        [4,5,3]]

def maximumFrequency(input):
    count = dict()
    sum = 0
    for x in input:
        for y in x:
            try:
                count[y] = count[y] + 1
            except:
                count[y] = 1

    maximum = max(count.values())
    for item in count:
        if count[item] == maximum:
            sum = sum + (item * count[item])
    return sum

print(maximumFrequency(input))
"""
12
"""


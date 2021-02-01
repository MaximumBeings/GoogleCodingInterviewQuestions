"""
Given that an input consists of n numbers.
Check whether those n numbers form an arithmetic
progression or not. Print true or false.

Time = O(n)
Space = O(1)

input = [2,6,10,15,19,23]
output = False
"""

input = [2,6,10,15,19,23]
input_1 = [2,6,10,14,18,22]

def arithmeticProgression(input):
    final = set()
    for x in range(1, len(input)):
        final.add(input[x] - input[x-1])
    if len(final) != 1:
        return False
    else:
        return True

print(arithmeticProgression(input))
print(arithmeticProgression(input_1))

"""
False
True
"""
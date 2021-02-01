"""
input = "code"
output = False

input = "aab"
output = True

input = "carerac"
output = True
"""

def duplicate(input):
    for x in input:
        if input.count(x) > 1:
            return True
    return False

print(duplicate("code"))
print(duplicate("aab"))
print(duplicate("carerac"))

"""
False
True
True
"""
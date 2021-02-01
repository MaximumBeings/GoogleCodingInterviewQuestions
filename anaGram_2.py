"""
Contract:
Given an array of strings, group anagrams together

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
out:
[["ate","eat","tea"], ["nat","tan"],["bat"]]

Definition:
A word, phrase, or sentence formed from another by rearranging its letters:
“Angel” is an anagram of “glean.
"""

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

def helperFunction(first, second):
    res = True
    for x in first:
        if x not in second:
            return False
    return res

def anaGram(input):
    res = []
    temp = []
    for x in range(len(input)):
        temp.append(input[x])
        for y in range(0,len(input)):
            if helperFunction(input[x], input[y]) == True:
                temp.append(input[y])
                temp = list(set(temp))
                temp = sorted(temp)
        if temp not in res:
            res.append(temp)
        temp = []
    return res

print(anaGram(input))

"""
[['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
"""
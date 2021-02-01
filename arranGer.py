"""
Given a string S, check if the letters can be rearranged so that
two characters that are adjacent to each other are not the same.
If possible, output any possible result. If not return the empty
string.

input = "aab"
output = "aba"
input2 = "aaab"
output = ""
"""
import random
input = "aab"
input2 = "aaab"

def arranGer(input):
    counter = 0
    while counter < 100:
        inputList = [x for x in input]
        checker = True
        while checker:
            temp=[]
            toUse = random.sample(inputList,1)[0]
            temp.append(toUse)
            inputList.remove(toUse)
            count = 1
            while len(inputList) > 0:
                toUse = random.sample(inputList,1)[0]
                temp.append(toUse)
                inputList.remove(toUse)
                if temp[count] == temp[count-1]:
                    checker = False
                    break
                count = count + 1
            if checker:
                return ''.join(temp)
        counter = counter + 1
    return " "
print(arranGer(input))
print(arranGer(input2))
"""
aba

"""




"""
Given a positive integer N. Count all possible distinct binary strings
of length N such that there are no consecutive 1s.
"""
import random
def consecutiveOnes(n):
    res = set()
    counter = 0
    checker = False
    tox = 0
    while counter < 300:
        toUse=""
        for c in range(n):
            toUse = toUse + str(random.sample([0,1],1)[0])
        if n == 2:
            if int(toUse[1]) ==1 and int(toUse[0]) == 1:
                checker == False
            else:
                checker = True
        elif n > 2:
            tox = 0
            for x in range(1,len(toUse)):
                if  (int(toUse[x-1]) == 1) and (int(toUse[x]) == 1):
                    if (int(toUse[x-1]) == int(toUse[x])  ):
                        checker = False
                        tox = tox + 1
                elif int(toUse[x-1]) != 1 and  int(toUse[x] != 1):
                    checker = True

        if checker == True and tox==0:
            res.add(toUse)
        checker = False
        counter += 1
    return res

print(consecutiveOnes(2))
print(consecutiveOnes(3))
print(consecutiveOnes(4))
print(consecutiveOnes(5))

"""
{'10', '00', '01'}
{'000', '010', '101', '001', '100'}
{'0001', '0101', '1001', '0010', '1010', '1000', '0100', '0000'}
{'01010', '00001', '10001', '01001', '00101', '00100', '10101', '10100', '10000', '00000', '01000', '10010', '00010'}
"""
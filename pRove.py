"""
Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive), prove that one duplicate number must exist.
Assume that there is only one duplicate number. Find duplicate one.

"""
n = 4

length = n + 1

import random

def eachSet(n):
    sub =  [x+1 for x in range(n)]
    potentialPopulation = [random.choice(sub)  for x in range(length)]
    return potentialPopulation

def checkerFunc(sampledPopulation):
    temp = []
    for x in sampledPopulation:
        temp.append(sampledPopulation.count(x))
    for x in temp:
        if x > 1:
            return True
    return False

def looPer(n):
    counter = 0
    checker = True
    while checker:
        sampledPopulation =  eachSet(n)
        checker = checkerFunc(sampledPopulation)
        counter= counter + 1
        if checker != True:
            return "Not True"
        elif counter == 1000000:
            return "Counted "+ str(counter) + " Times - There is always a Duplicate => Proved"

print(looPer(n))


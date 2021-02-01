"""
Contract:
    You have 100 doors in a row that are all initially closed. You made
    100 passes by the doors starting with the first door every time. The
    first time through you visit every door and toggle the door (if the is closed,
    you open it, if its open you close it). The second time you ony visit every second
    door  (#2, #4, #6), the third time every 3rd door (#3, #6, #9) etc until you only
    visit the 100th floor

    What states are the doors in after the last pass?
    Which are opened and which are closed?
"""


# Recall indexing starts at 0 in Python, C++, Java etc
#So 0-99 = 1-100

doors = [1] * 100  #Close all 100 doors to initialize
skip = 1
for y in range(0,len(doors)):
    #print()
    #print("This is the y " + str(y))
    for x in range(y,len(doors),skip):
        idx = x
        if idx>len(doors):
            idx = idx%len(doors)
        #print("This is the x " + str(idx))
        if doors[idx] == 1:
            doors[idx] = 0
        elif doors[idx] == 0:
            doors[idx] = 1
    skip = skip + 1

res=[]
for x in range(len(doors)):
    if doors[x] == 0:
        res.append(x+1)
print()
print(res)
print()
#print(doors)

"""
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
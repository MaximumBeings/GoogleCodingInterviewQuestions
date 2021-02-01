res = []

def state(loc):
    for x in range(2):
        for y in range(2):
            res.append((x,y))

    res

print(state((2,2)))
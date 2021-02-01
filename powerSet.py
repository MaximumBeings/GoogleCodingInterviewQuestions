def powerSetNaive(array):
    """
    Input = [1,2,3]
    Output = [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
    """

    res = [[d] for d in array]
    res.append([])
    array_ = []
    skip = 1
    while skip <=len(array)-1:

        for x in range(0,len(array),skip):
            array_.append(array[x])
        for y in range(len(array_[0:x+skip+1])):
            toAppend = array_[y:x+1]
            if toAppend not in res:
                res.append(toAppend)
            toAppend = array_[0:x]
            if toAppend not in res:
                res.append(toAppend)
        array_=[]
        skip = skip + 1

    return res

solved = powerSetNaive([1,2,3])
print(solved)

"""
MITx via Edx
Data Science and Computational Thinking
John Guttag
"""
def powerSet(elts):
    if len(elts) == 0:
        return [[]]
    else:
        smaller = powerSet(elts[1:])
        elt = [elts[0]]
        withElt = []
        for s in smaller:
            withElt.append(s + elt)
        allofthem = smaller + withElt
        return allofthem

print(powerSet([2,3,4]))
"""
[[1], [2], [3], [], [1, 2, 3], [1, 2], [2, 3], [1, 3]]
[[], [3], [2], [3, 2], [1], [3, 1], [2, 1], [3, 2, 1]]
"""
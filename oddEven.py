"""
Given an array A of non-negative integers, half of the
integers in A are odd and half of the integers are even. Sort
the array so that whenever A[i] is odd, i is odd; and whenever
A[i] is even , i is even.

You may return any answer array that satisfies this condition.

Time: O(n)
Space: O(1)

input = [4, 2, 5, 7] ; output = [4, 5, 2, 7]
Explanation: [4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5] would also have been
accepted.
"""
input = [4,2,5,7,9,8,6,1,14,12,101,100,11,13]


def oddEven(input):
    for x in range(0,len(input)):
        try:
            if input[x]%2 == 0 and x%2==0:
               pass
            try:
                if input[x]%2 == 0 and x%2!=0:
                    if input[x-1]%2==0:
                        pass
                    elif input[x-1]%2!=0:
                        temp = input[x-1]
                        input[x-1] = input[x]
                        input[x] = temp
            except:
                pass
            try:
                if input[x+1]%2!=0 and x%2 != 0:
                    temp = input[x+1]
                    input[x+1] = input[x]
                    input[x] = temp
                elif input[x+1]%2!=0 and x%2 != 0:
                    pass
            except:
                pass
        except:
            pass
    return input

print(oddEven(input))
"""
[4, 5, 2, 9, 8, 7, 6, 1, 14, 101, 12, 11, 100, 13]
"""
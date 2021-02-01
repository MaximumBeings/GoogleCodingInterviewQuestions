"""
Find the maximum absoute difference of value and
index sums (return max value of f(i,j) wwhere f(i,j) =
|A[i] - A[j] |+|i-j|) in O(n) time.

input=[1,3,-1]

output = 5
"""
input = [1, 3, -1]


def absoluteMaxDiff(input):
    maximum = float("-inf")
    for x in range(1, len(input)):
        test = abs(input[x - 1] - input[x]) + abs((x - 1) - x)
        if test > maximum:
            maximum = test
    return maximum


print(absoluteMaxDiff(input))
"""
5
"""

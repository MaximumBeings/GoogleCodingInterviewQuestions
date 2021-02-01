"""
Contract:
Return the square root of a number as an integer
"""
def intSquareRoot(x):
    return int(x ** (1/2))

#print(intSquareRoot(8))
#print(intSquareRoot(4))
#print(intSquareRoot(30))

"""
2
2
5
"""

"""
Using Bisection Method to Find
Square Root or root of any
polynomial just change the equation in the
helper function
"""
def bisectionSearch(sQuare):
    def helper(x,sQuare):
        return x * x - sQuare
    n = 0
    a = 1
    b = sQuare + a
    while n < 10000:
        c = (a+b)/2.0
        if helper(c,sQuare) == 0 or (b - a) < 0.000000000000001:
            return c
        if helper(c, sQuare) < 0 and helper(a, sQuare) < 0:
            a = c
        else:
            b = c
        n = n + 1

print(bisectionSearch(8))
print(bisectionSearch(200000000))
print(bisectionSearch(4))
print(bisectionSearch(49))
"""
2.8284271247461903
141.4213562373095
2.0
7.0
"""
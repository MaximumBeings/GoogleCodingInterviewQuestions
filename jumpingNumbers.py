"""
Print all jumping numbers smaller tan or equal to x

input x = 105

output = 0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101
"""

def checker(number):
    test = str(number)
    for x in range(1, len(test)):
        if abs(int(test[x]) - int(test[x-1])) != 1:
            return False
    return True

def main(input):
    final = []
    for x in range(input):
        if x < 10:
            final.append(x)
        else:
            ans = checker(x)
            if ans == True:
                final.append(x)
    return final

print(main(105))

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23,
32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89,
98, 101]
"""
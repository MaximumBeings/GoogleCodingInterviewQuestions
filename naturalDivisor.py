"""
Given a natural number n, print all distinct divisors
of it efficiently

Time = O(sqrt(n))
Space = O(1)
input = 10
output = [1,2,5,10]
"""

answer = []

for x in range(10):
    if 10%(x+1) == 0:
        answer.append(x+1)
print(answer)

"""
[1, 2, 5, 10]
"""
"""
Function add(A,B):
    while B greater than 0:
        U = A XOR B
        A = U
        B = V * 2
    return A
"""

def interesting(A,B):
    counter = 0
    while B > 0:
        U = (A and not B) or (not A and B)  #XOR
        #U = bool(A) ^ bool(B) ##Alternative way of expressing XOR
        V = A and B
        A = U
        B = V * 2
        counter = counter + 1
    return counter

print(interesting(350,90000))

"""
2
"""
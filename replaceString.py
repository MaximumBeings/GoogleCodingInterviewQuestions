"""
Given a valid (IPv4) IP address, return a defanged version of that
IP addess - A defanged IP address replaces every period ".' with
"[.]"
input  = "1.1.1.1"
output = "1[.]1[.]1[.]1"
"""
input  = "1.1.1.1"
input2 = "255.100.50.0"

print(input.replace('.', '[.]'))
print(input2.replace('.', '[.]'))

"""
1[.]1[.]1[.]1
255[.]100[.]50[.]0
"""
#https://devsenv.com/example/-2759-beecrowd-online-judge-solution-2759-input-and-output-character-solution-in-c,-c++,-java,-js-and-python
"""
#This code is wrong
A = input()
B = input()
C = input()

A_ = ord(A)
B_ = ord(B)
C_ = ord(C)

print(f"A = {chr(A_)}, B = {chr(A_ + 1)}, B = {chr(A_ + 1)}")
print(f"A = {chr(B_)}, B = {chr(B_ + 1)}, B = {chr(B_ + 1)}")
print(f"A = {chr(C_)}, B = {chr(C_ + 1)}, B = {chr(C_ + 1)}")
"""

a = str(input())
b = str(input())
c = str(input())
print('A = {}, B = {}, C = {}'.format(a, b, c))
print('A = {}, B = {}, C = {}'.format(b, c, a))
print('A = {}, B = {}, C = {}'.format(c, a, b))

#https://github.com/brenonf/URI-python-3/blob/master/1929.py
sticks = list(map(int, input().split()))

sticks.sort()

A = sticks[0]
B = sticks[1]
C = sticks[2]
D = sticks[3]

def tri_cond(X,Y,Z):

    if X+Y>Z and X+Z>Y and Z+Y>X:
        ans = True
    else:
        ans = False

    return ans

if tri_cond(A,B,C) or tri_cond(A,B,D) or tri_cond(A,C,D) or tri_cond(B,C,D):
    print("S")
else:
    print("N")

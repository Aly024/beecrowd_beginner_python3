N = int(input())

for i in range(N):

    T = int(input())

    diff = 2015 - T

    if diff<1:
        print(f"{1-diff} A.C.")
    else:
        print(f"{diff} D.C.")
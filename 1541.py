while True:

    x = input().split(" ")

    if "0" in x:
        break

    A,B,C = map(int,x)

    #House area = Y% of Land Area
    #Land Area = House Area / Y%
    H_A = A*B
    Y = C/100
    L_A = H_A / Y 
    l = int(L_A**0.5)

    print(l)
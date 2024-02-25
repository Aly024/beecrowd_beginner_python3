r = int(input())
c = int(input())

#even - even = white 1
if ( (r%2 == 0) and (c%2 == 0) ):
    print(1)
#odd - odd = white 1
elif ( (r%2 != 0) and (c%2 != 0) ):
    print(1)
else:
    print(0)

while True:

    try: 

        Xf, Yf, Xi, Yi, Vi, R1, R2 = map( int, input().split() )

        dist = ( ((Xi - Xf)**2) + ((Yi - Yf)**2) )**0.5

        dist += Vi*1.50

        #print(dist)

        if dist > R1+R2:
            print("N")

        else:
            print("Y")

    except EOFError:
        break
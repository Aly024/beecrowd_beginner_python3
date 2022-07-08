X, Y = map(float, input().split(" "))

if X == 0 and Y == 0:
    print('Origem')

elif X == 0 or Y == 0:
    if X == 0:
        print('Eixo Y')
    else:
        print('Eixo X')

else:
    if X >= 0 and Y >= 0:
        print('Q1')

    elif X <= 0 and Y >= 0:
        print('Q2')

    elif X <= 0 and Y <= 0:
        print('Q3')

    elif X >= 0 and Y <= 0:
        print('Q4')


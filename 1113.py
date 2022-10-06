while True:

    X, Y = map(int, input().split())

    if X == Y:
        break

    elif X > Y:
        print('Decrescente')

    else: 
        print('Crescente')
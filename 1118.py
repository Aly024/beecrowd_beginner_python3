while True:

    valid = []

    while len(valid) < 2:

        X = float(input())

        if (0<= X <= 10):
            valid.append(X)
        
        else:
            print("nota invalida")

    media = sum(valid) / len(valid)
    print(f"media = {media:.2f}")

    check = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        check = int(input())
        if (check == 1 or check == 2):
            break

    if (check == 2):
        break
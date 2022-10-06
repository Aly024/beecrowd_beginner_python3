valid = []

while True:

    for i in range(1):

        X = float(input())

        if ( 0<= X <= 10):
            valid.append(X)

        else:
            print(f"nota invalida")

    if len(valid) == 2:
        media = sum(valid) / len(valid)
        print(f"media = {media:.2f}")
        break
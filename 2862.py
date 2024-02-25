N = int(input())

for i in range(N):

    power = int(input())

    if power <= 8000:
        print("Inseto!")

    elif power > 8000:
        print("Mais de 8000!")
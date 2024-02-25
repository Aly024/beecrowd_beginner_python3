while True:
    try:
        N = int(input())

        if 0 <= N < 90 or N == 360:
            print("Bom Dia!!")

        elif 90 <= N < 180:
            print("Boa Tarde!!")

        elif 180 <= N < 270:
            print("Boa Noite!!")

        elif 270 <= N < 360:
            print("De Madrugada!!")
    
    except EOFError:
        break

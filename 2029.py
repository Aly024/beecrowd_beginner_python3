pi = 3.14
while True:

    try:
        Volume = float(input())
        Dia = float(input())
        r = Dia/2

        Area = 3.14*r*r
        Height = Volume / Area

        print(f"ALTURA = {Height:.2f}")
        print(f"AREA = {Area:.2f}")

    except EOFError:
        break
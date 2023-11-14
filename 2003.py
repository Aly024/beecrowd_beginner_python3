while True:
    try:

        hr,min = map(int,input().split(":"))

        if hr < 7:
            print(f"Atraso maximo: 0")
        else:
            f_hr = hr-7
            f_min = (f_hr*60) + min
            print(f"Atraso maximo: {f_min}")

    except EOFError:
        break
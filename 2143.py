while True:

    t_c = int(input())

    if t_c == 0:
        break

    for i in range(t_c):

        people = int(input())

        if people%2 == 0:
            result = 2*people - 2

        if people%2 != 0:
            result = 2*people - 1

        print(result)
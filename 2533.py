while True:
    try:

        M = int(input())

        N_list =[]
        C_list = []

        for i in range(M):
            N, C = map(int,input().split())
            N_list.append(N)
            C_list.append(C)

        numeritor = 0
        demomeritor = sum(C_list)

        for i in range(M):
            numeritor += ((N_list[i]) * (C_list[i]))


        numeritor_avg = numeritor/M
        demomeritor_avg = demomeritor/M

        result = numeritor_avg / (demomeritor_avg*100)
        print(f"{result:.4f}")

    except EOFError:
        break
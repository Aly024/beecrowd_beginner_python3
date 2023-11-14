while True:
    try:
                
        N = int(input())

        M, L = map(int, input().split())

        M_list = []
        L_list = []

        for i in range(M):
            m = list(map(int, input().split()))
            M_list.append(m)

        for i in range(L):
            l = list(map(int, input().split()))
            L_list.append(l)

        C_M, C_L = map(int, input().split())

        A = int(input())

        card_M = M_list[C_M-1]
        card_L = L_list[C_L-1]

        #print(card_M)
        #print(card_L)

        attrib_M = card_M[A-1]
        attrib_L = card_L[A-1]

        if attrib_M > attrib_L:
            print("Marcos")
        elif attrib_M < attrib_L:
            print("Leonardo")
        elif attrib_M == attrib_L:
            print("Empate")

    except EOFError:
        break
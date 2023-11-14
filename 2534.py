#https://github.com/mcavalca/uri-python/blob/master/2534.py
while True:
    try:
        N, Q = map(int, input().split())

        N_list=[]
        Q_list=[]

        for i in range(N):
            n = int(input())
            N_list.append(n)

        N_list.sort(reverse=True)

        for i in range(Q):
            p = int(input())
            Q_list.append(p)

        #print(Q_list)

        for i in Q_list:
            print(N_list[i-1])

    except EOFError:
        break

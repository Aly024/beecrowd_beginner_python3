while (True):

    N = int(input())

    if N == -1:
        break

    elif N==0:
        print(0)

    elif 0<N<=10000000000000000000:
        print(N-1)
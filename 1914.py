t_c = int(input())

for i in range(t_c):

    k1, v1, k2, v2 = input().split()
    n1, n2 = map(int,input().split())

    player1 = {k1:v1}
    player2 = {k2,v2}

    N = n1+n2

    if N%2 == 0:
        winner = "PAR"
    else:
        winner = "IMPAR"

    if v1 == winner:
        print(k1)
    else:
        print(k2)
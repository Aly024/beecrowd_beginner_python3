p, j1, j2, r, a = map(int,input().split())

result = j1+j2

#Player 2 guessing
if r == 1 and a == 1:
    #print("player 2 wins")
    print("Jogador 2 ganha!")

elif r == 1 and a == 0:
    #print("player 1 wins")
    print("Jogador 1 ganha!")

elif r == 0 and a == 1:
    #print("player 1 wins")
    print("Jogador 1 ganha!")

elif r == 0 and a == 0:

    if p == 1 and result%2 == 0:
        #print("Player 1 wins")
        print("Jogador 1 ganha!")

    elif p == 0 and result%2 == 1:
        #print("Player 1 wins")
        print("Jogador 1 ganha!")

    else:
        #print("Player 2 wins")
        print("Jogador 2 ganha!")

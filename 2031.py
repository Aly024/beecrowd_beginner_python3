N = int(input())

for i in range(N):
    signs = {"ataque":2,
            "pedra":1,
            "papel":0
            }

    player_1 = input()
    player_2 = input()

    if player_1 == player_2 == "ataque":
        #print("Mutual Annihilation")
        print("Aniquilacao mutua")

    elif player_1 == player_2 == "papel":
        #print("both win")
        print("Ambos venceram")

    elif player_1 == player_2 == "pedra":
        #print("both lose")
        print("Sem ganhador")

    else:
        p1_score = signs[player_1]
        p2_score = signs[player_2]

        if p1_score>p2_score:
            #print("player 1 winner")
            print("Jogador 1 venceu")

        else:
            #print("player 2 winner")
            print("Jogador 2 venceu")




while True:
    try:

        #list
        output = ["Os atributos dos monstros vao ser inteligencia, sabedoria...",
                "Iron Maiden's gonna get you, no matter how far!",
                "Urano perdeu algo muito precioso..."]
        answer = []
        #var = ["rock", "paper", "scissors"]
        var = ["pedra", "papel", "tesoura"]

        #dictionary
        powers = {"papel": "pedra",
                "pedra": "tesoura",
                "tesoura": "papel",
                }

        #functions
        def tie(a,b,c):
            if a==b==c:
                return True
            if a in var and b in var and c in var and a!=b and b!=c and a!=c:
                return True

        count = 0
        def compare(a,b):
            global count
            A = answer[a]
            B = answer[b]
            if A==B:
                count += 1
                return a
            else:
                for key, val in powers.items():
                    if A==key and B==val:
                        #print(f"{key} {val}")
                        return a
                    if B==key and A==val:
                        #print(f"{key} {val}")
                        return b


        #main program
        answer = input().split()
        #First checking if tie
        if tie(answer[0], answer[1], answer[2]):
            #print("tie")
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        else:
            if answer[0] == answer[1]:
                x = 2
                y = 1
                z = 0
            else:
                x = 0
                y = 1
                z = 2
            round_1 = compare(x,y)
            #print(round_1)
            round_2 = compare(round_1,z)
            #print(round_2)
            #print(f"count: {count}")

            if count == 0:
                print(output[round_2])
            elif count > 0:
                #print("tie")
                print("Putz vei, o Leo ta demorando muito pra jogar...")

    except EOFError:
        break
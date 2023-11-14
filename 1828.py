T_C = int(input())

for i in range(T_C):

    j = i+1
    sheldon, raj = input().split()

    '''
    { Rock : [ Lizard, Scissors ]
    Paper : [ Rock, Spock ]
    Scissors : [ Paper, Lizard ]
    Lizard : [ Spock, Rock ]
    Spock : [ Scissors, Rock ] }
    '''


    outcome = {"pedra": ["lagarto","tesoura"],
            "papel": ["pedra", "Spock"],
            "tesoura": ["papel", "lagarto"],
            "Spock": ["tesoura", "pedra"],
            "lagarto": ["Spock", "papel"]}

    if sheldon == raj:
        print(f"Caso #{j}: De novo!")

    else: 
        for key, value in outcome.items():
            if (sheldon == key) and (raj in value):
                print(f"Caso #{j}: Bazinga!")

            else:
                if (raj == key) and (sheldon in value):
                    print(f"Caso #{j}: Raj trapaceou!")

            
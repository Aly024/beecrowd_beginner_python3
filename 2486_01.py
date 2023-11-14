food_list = {"suco de laranja": 120,
             "morango fresco" : 85,
             "mamao" : 85,
             "goiaba vermelha" : 70,
             "manga" : 56,
             "laranja" : 50,
             "brocolis" : 34}

while(True):

    T = int(input())

    if T == 0:
        break

    min = 110
    max = 130
    Z = 0

    for i in range(T):

        input_str = input()
        split_input = input_str.split()

        if len(split_input) >= 2:
            X = int(split_input[0])
            Y = " ".join(split_input[1:])

        for key, value in food_list.items():
            if key == Y:
                Z += X*value

    if Z < min:
        print(f"Mais {min-Z} mg")

    elif Z > max:
        print(f"Menos {Z-max} mg")

    else:
        print(f"{Z} mg")
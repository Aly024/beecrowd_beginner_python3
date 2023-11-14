t = 0
while (True):

    try:
        t += 1
        x = input()
        z = input()

        len_x = len(x)
        #print(len_x)

        subsequence = 0
        pos = 0

        for i in range(len(z)):

            pos += 1

            if x[0] == z[i]:

                match = z[i:i+len_x]
                #print(match)

                if x == match:
                    subsequence += 1
                    last_pos = pos

        if subsequence > 0:
            print(f"Caso #{t}:")
            print(f"Qtd.Subsequencias: {subsequence}")
            print(f"Pos: {last_pos}")
        else:
            print(f"Caso #{t}:")
            print("Nao existe subsequencia")

        print()
        
    except EOFError:
        break
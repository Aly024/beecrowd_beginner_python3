#https://github.com/gustavonikov/URI_problems/blob/main/URI%202724%20-%20Help%20Patatatitu.py

N = int(input())

for cases in range(N):
    dangerousCompounds = []
    juvenalCompounds = []

    T = int(input())

    for dangerousCompound in range(T):
        dangerousCompounds.append(input())
    
    U = int(input())

    for juvenalCompound in range(U):
        juvenalCompounds.append(input())

    for juvenalCompound in juvenalCompounds:
        count = 0

        for dangerousCompound in dangerousCompounds:
            word = ''

            for index, letter in enumerate(juvenalCompound):
                word += letter

                diff = len(word) - len(dangerousCompound)

                if len(word) >= len(dangerousCompound):
                    if dangerousCompound in word:
                        if index == len(juvenalCompound) - 1 and (juvenalCompound[diff:] == dangerousCompound):
                            count += 1
                            break
                        elif index != len(juvenalCompound) - 1 and juvenalCompound[index + 1].isnumeric():
                            break
                        elif index != len(juvenalCompound) - 1 and juvenalCompound[index + 1].isalpha() and juvenalCompound[index + 1].isupper():
                            count += 1
                            break
                
        if count > 0:
            print('Abortar')
        else:
            print('Prossiga')
    
    if cases != (N - 1):
        print()
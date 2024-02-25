#not accepted
#https://github.com/gustavonikov/URI_problems/blob/main/URI%202724%20-%20Help%20Patatatitu.py

N = int(input())

for i in range(N):

    num_chem = int(input())
    name_chem_list = [input() for num in range(num_chem)]

    num_exp = int(input())
    exp_list = [input() for num in range(num_exp)]

    ############
    for j in exp_list:
        count = 0

        for i in name_chem_list:
            word = ''

            for index,letter in enumerate(j):
                word+=letter

                diff = len(word) - len(j)

                if len(word) >= len(j):

                    if index == len(j) - 1 and (j[diff:] == j):
                        count += 1
                        break

                    elif index != len(j) - 1 and j[index + 1].isnumeric():
                        break

                    elif index != len(j) - 1 and j[index + 1].isalpha() and j[index+1].isupper():
                        count += 1
                        break

            if count > 0:
                print("Abortar")
            else:
                print("Prossiga")

        if i != (N-1):
            print()
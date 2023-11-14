while True:
    try:

        #N = no. of game || I = ID
        N, I = map(int,input().split())

        # cannot use dictionaries because of duplicates
        list_uni_id = []
        #1 means LOL || 0 means CS
        list_game_name = []

        for num in range(N):
            i , j = map(int, input().split())
            list_uni_id.append(i)
            list_game_name.append(j)

        result = 0

        for item in range(N):
            if list_uni_id[item-1] == I and list_game_name[item-1] == 0:
                result += 1

        print(result)

    except EOFError:
        break
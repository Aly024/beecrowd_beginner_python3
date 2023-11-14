while True:
    try:

        N = int(input())

        poll = list(map(int, input().split()))
        t_vote = sum(poll)

        yes = (2/3)*N
        #print(yes)

        if t_vote >= yes:
            print('impeachment')
        else:
            print("acusacao arquivada")

    except EOFError:
        break
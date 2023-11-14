    t_c = int(input())

    for i in range(t_c):

        name = input()
        difficulty = float(input())
        score = list(map(float, input().split()))
        score.sort()
        score = score[1:-1]
        score_f = difficulty*(sum(score))
        print(f"{name} {score_f:.2f}")
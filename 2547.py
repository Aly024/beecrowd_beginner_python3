while True:
    try:
        N, A_min, A_max = map(int, input().split())

        result = 0

        for i in range(N):
            height = int(input())

            if A_min <= height <= A_max:
                result += 1

        print(result)

    except EOFError:
        break
while True:

    try:

        L = int(input())
        v = list(map(int,input().split()))
        v.sort()

        ans = 0
        for item in v:
            if item < 10:
                ans = 1
            elif 10<=item<20:
                ans = 2
            elif 20 <= item:
                ans = 3

        print(ans)

    except EOFError:
        break


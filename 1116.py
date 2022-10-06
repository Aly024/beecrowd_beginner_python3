N = int(input())

for i in range(N):

    X, Y = map(int, input().split())

    if Y == 0:
        print("divisao impossivel")

    else:
        ans = X / Y
        print(f"{ans:.1f}")
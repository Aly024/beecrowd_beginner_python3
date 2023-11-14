N,M = map(int, input().split())

for i in range(M):

    action = input()

    if action == "fechou":
        N += 1

    if action == "clicou":
        N -= 1

print(N)
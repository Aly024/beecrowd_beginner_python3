N = int(input())

for i in range(N):
    x, y = map(int, input().split() )
    total = []
    X = min(x,y)
    Y = max(x,y)

    for j in range(X+1,Y):

       if (j % 2) != 0:
            total.append(j)

    #print(total)
    total = sum(total)
    print(total)
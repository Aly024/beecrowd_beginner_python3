x = int(input())
y = int(input())

X = min(x,y)
Y = max(x,y)

for i in range(X+1,Y):

    if (i % 5 == 2) or (i % 5 == 3):
        print(i)
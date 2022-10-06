result = []

x = int(input())
y = int(input())

X = min(x,y)
Y = max(x,y)

for i in range(X,Y+1):

    if i % 13 != 0:
        result.append(i)

output = sum(result)
print(output)
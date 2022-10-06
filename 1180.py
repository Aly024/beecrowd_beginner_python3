N = int(input())

X = []

list_X = list(map(int, input().split()))

for i in range(N):

    item_x = list_X[i]
    X.append(item_x)

#print(X)

min_val = min(X)
print(f"Menor valor: {min_val}")
index_min_val = X.index(min_val)
print(f"Posicao: {index_min_val}")

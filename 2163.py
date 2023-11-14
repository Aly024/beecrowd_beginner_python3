N, M = map(int, input().split())

array = []

for i in range(N):
    row = list(map(int, input().split()))
    array.append(row)

cndtn = 0
n = 0
m = 0

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if array[i][j] == 42:
            if (
                array[i - 1][j - 1] == 7
                and array[i - 1][j] == 7
                and array[i - 1][j + 1] == 7
                and array[i][j - 1] == 7
                and array[i][j + 1] == 7
                and array[i + 1][j - 1] == 7
                and array[i + 1][j] == 7
                and array[i + 1][j + 1] == 7
            ):
                cndtn = 1
                n = i + 1
                m = j + 1

print(n, m)
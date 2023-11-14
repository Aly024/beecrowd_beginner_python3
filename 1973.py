#https://github.com/mcavalca/uri-python/blob/master/1973.py
n = int(input())
x = list(map(int, input().split()))
total = sum(x)
atacadas = [0] * n
i = 0

while i >= 0 and i < n:
    lado = x[i] % 2
    if x[i] > 0:
        x[i] -= 1
        atacadas[i] = 1
        total -= 1
    if lado:
        i += 1
    else:
        i -= 1

atacadas = atacadas.count(1)
print(atacadas, total)
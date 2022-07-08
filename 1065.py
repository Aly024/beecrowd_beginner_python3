count = 0

for i in range(5):
    z = float(input())
    if z % 2 == 0:
        count += 1

print(f'{count} valores pares')
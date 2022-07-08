N = int(input())
IN = 0
OUT = 0

for i in range(N):

    X = int(input())

    if 10 <= X <= 20:
        IN += 1
    else:
        OUT += 1

print(f'{IN} in')
print(f'{OUT} out')

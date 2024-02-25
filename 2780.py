dist = int(input())
point = 0
if dist <= 800:
    point += 1

elif (800 < dist <= 1400):
    point += 2

elif (1400 < dist <= 2000):
    point += 3

print(point)
num = []
portion = [300, 1500, 600, 1000, 150]
for i in range(5): 
    x = int(input())
    num.append(x)

total = 225
for i in range(5):
    total += num[i]*portion[i]

print(total)


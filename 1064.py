count = 0
pos_num = []

for i in range(6):
    z = float(input())
    if z > 0:
        pos_num.append(z)
        count += 1

print(f'{count} valores positivos')

if count == 0:
    avg = '-nan'
else:
    avg = float( sum(pos_num) / len(pos_num) )

print(f'{avg:0.1f}')

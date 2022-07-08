count = 0
even = 0
odd = 0
pos = 0
neg = 0
for i in range(5):
    z = int(input())


    if z > 0:
        pos += 1  
    if z < 0:
        neg += 1
    if z % 2 == 0:
        even += 1
    if z % 2 != 0:
        odd += 1

print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')

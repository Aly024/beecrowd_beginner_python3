#https://github.com/Lucas-FLima/Python-Uri-Judge3/blob/main/1021.py

val = float(input())
notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')

for n in notes:
    quotient = int((val / n))
    print(f'{quotient} nota(s) de R$ {n:.2f}')
    remainder = val % n
    val = remainder
print('MOEDAS:')
for m in coins:
    quotient = int(round(val,2) / m)
    print(f'{quotient} moeda(s) de R$ {m:.2f}')
    remainder = round(val,2) % m
    val = remainder
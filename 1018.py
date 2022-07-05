val = int(input())
print(val)
notes = [100, 50, 20, 10, 5, 2, 1]

for n in notes:
    quotient = int((val / n))
    print(f'{quotient} nota(s) de R$ {n},00')
    remainder = val % n
    val = remainder
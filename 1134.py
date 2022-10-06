Alcohol = 0
Gasoline = 0
Diesel = 0

while True:

    n = int(input())

    if n == 1:
        Alcohol += 1

    if n == 2:
        Gasoline += 1

    if n == 3:
        Diesel += 1

    if n == 4:
        break

print("MUITO OBRIGADO")
print(f"Alcool: {Alcohol}")
print(f"Gasolina: {Gasoline}")
print(f"Diesel: {Diesel}")
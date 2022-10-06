Matches = 0
Inter = 0
Gremio = 0
Draw = 0

while True:

    I, G = map(int, input().split())

    if I > G:
        Inter += 1

    elif I < G:
        Gremio += 1

    elif I == G:
        Draw += 1

    Matches += 1

    print("Novo grenal (1-sim 2-nao)")
    check = int(input())
    if check == 2:
        break

print(f"{Matches} grenais")
print(f"Inter:{Inter}")
print(f"Gremio:{Gremio}")
print(f"Empates:{Draw}")

if Inter == Gremio:
    print("Nao houve vencedor")

else:
    if Inter > Gremio:
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")


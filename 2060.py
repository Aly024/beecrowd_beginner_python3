two, three, four, five = 0, 0, 0, 0

N = int(input())

u_i_list = list(map(int, input().split()))

for item in u_i_list:
    
    if item%2 == 0:
        two += 1

    if item%3 == 0:
        three += 1

    if item%4 == 0:
        four += 1

    if item%5 == 0:
        five += 1

print(f"{two} Multiplo(s) de 2")
print(f"{three} Multiplo(s) de 3")
print(f"{four} Multiplo(s) de 4")
print(f"{five} Multiplo(s) de 5")

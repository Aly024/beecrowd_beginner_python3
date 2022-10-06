N = int(input())

for i in range(N):

    tc = int(input())

    divisor = []

    for j in range(1,tc):

        if tc % j == 0:
            divisor.append(j)

    if sum(divisor) == tc:
        print(f"{tc} eh perfeito")
    
    else:
        print(f"{tc} nao eh perfeito")
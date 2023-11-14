F_h, N_P =  map(int,input().split())

P_h = list(map(int,input().split()))
output = 0

for i in range(len(P_h)-1):

    if abs(P_h[i]-P_h[i+1]) > F_h:
        output = 1
        break
    else:
        output = 0

if output == 1:
    print("GAME OVER")
else:
    print("YOU WIN")

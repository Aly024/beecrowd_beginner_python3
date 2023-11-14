t_c = int(input())

for i in range(t_c):

    H, M, S = input().split()

    if len(H) == 1:
        H = "0"+H
    
    if len(M) == 1:
        M = "0"+M

    if S == "0": 
        print(f'{H}:{M} - A porta fechou!')

    else: 
        print(f'{H}:{M} - A porta abriu!')

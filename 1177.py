T = int(input())
j = 0

for i in range(1000):

    if j < T:
        print(f"N[{i}] = {j}")
        j += 1
    
    else:
        j = 0
        print(f"N[{i}] = {j}")
        j += 1
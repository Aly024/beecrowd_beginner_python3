N = int(input())

for i in range(N):

    x,y = map(int, input().split())

    odd_num = []
    count = 0

    while (count < y):

        z = x
        if z % 2 != 0:
            odd_num.append(z)
            count += 1
            #print(f"count = {count}")

        x += 1
    
    print(sum(odd_num))


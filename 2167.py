N = int(input())

rpm = list(map(int, input().split()))
ans = 0
for i in range(1,len(rpm)):

    if rpm[i-1] > rpm[i]:
        ans = i+1
        print(ans)
        break

if ans == 0:
    print(ans)



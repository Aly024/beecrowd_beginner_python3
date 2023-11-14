N = int(input())
T = list(map(int,input().split()))

ans = T.index(min(T))
ans += 1
print(ans)
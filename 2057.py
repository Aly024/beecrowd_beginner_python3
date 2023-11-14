S,T,F = map(int,input().split())

result = (S+T+F)

if result>24:
    result = result-24
elif result<0:
    result = 24 + result

print(result)
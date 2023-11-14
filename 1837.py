a,b = map(int, input().split())

q = int(a/b)

r = a - (b*q)

while r<0:
    if a<0 and b<0:
        q+=1
        r = a - (b*q)

    else:
        q-=1
        r = a - (b*q)

print(f"{q} {r}")
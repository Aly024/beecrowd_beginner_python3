#https://github.com/joy1954islam/uri-problem-solution-in-python/blob/master/problem%201145%20%20Logical%20Sequence%202.py

n1,n2 = list(map(int,input().split()))
cont = 1
end = (int((n2/n1))+1)
for i in range(1,end):
    r = ""
    for y in range(n1):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])
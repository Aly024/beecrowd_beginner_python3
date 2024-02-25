#https://github.com/mcavalca/uri-python/blob/master/2896.py 
T_C = int(input())

for i in range(T_C):
    b, d = map(int, input().split())

    
    remaining = int(b%d)+int(b/d)
    print(remaining)
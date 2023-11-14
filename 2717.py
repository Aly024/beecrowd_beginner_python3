N = int(input())

A,B = map(int, input().split())

if A+B <= N:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")
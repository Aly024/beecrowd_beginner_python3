N = int(input())

for i in range(N):
    A, B, C = map(float, input().split())
    result = ( (A*2) + (B*3) + (C*5) )/ 10
    print(f'{result:.1f}')
    #print('%.1f' %result)
m, n = map(int, input().split())

while True:

    if (m <= 0) or ( n<= 0):
        break

    else:

        result = []

        M = min(m,n)
        N = max(m,n)

        for i in range(M,N+1):
            result.append(i)

        output = ' '.join(map(str,result))
        print(f'{output} Sum={sum(result)}')
    
    m, n = map(int, input().split())
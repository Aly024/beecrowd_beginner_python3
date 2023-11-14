#https://github.com/brenonf/URI-python-3/blob/master/1557.py

while True:
    N = int(input())

    if N == 0:
        break

    matrix = []

    for r in range(N):
        row = []
        for c in range(N):
            row.append(0)
        matrix.append(row)

    for r in range(N):
        for c in range(N):
            matrix[r][c]=2**(r+c)

    T = len(str(matrix[N-1][N-1]))
    
    for i in range(N):
        for j in range(N):
            matrix[i][j] = str(matrix[i][j])
            while len(matrix[i][j]) < T:
                matrix[i][j] = ' ' + matrix[i][j]
        M = ' '.join(matrix[i])

        print(M)   

    print()
          
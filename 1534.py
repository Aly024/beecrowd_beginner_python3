#https://github.com/brenonf/URI-python-3/blob/master/1534.py
#https://www.youtube.com/watch?v=6SPDvPK38tw&t=4s&ab_channel=Telusko

while True:
    try:

        N = int(input())

        if 3<=N<=70:

            matrix= []

            for r in range(N):
                row = []
                for c in range(N):
                    row.append(3)
                matrix.append(row)

            #print(matrix)

            for r in range(N):
                matrix[r][r]=1
                matrix[r][N-r-1]=2

            for r in range(N):
                for c in range(N):
                    print(matrix[r][c],end="")
                print()
    
    except EOFError:
        break
while True:
    try:
        N, M = map(int, input().split())

        matrix = []

        for i in range(N):
            row_list = []
            row = input()
            for item in row:
                row_list.append(int(item))
            matrix.append(row_list)

        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 1:
                    matrix[r][c] = 9

        #print(matrix)

        #calculating adjacent

        for r in range(N):
            for c in range(M):
                if (r!=0 and c!=0 and r!=N-1 and c!=M-1):
                    if matrix[r][c] == 0:
                        sum = 0
                        if matrix[r-1][c] == 9:
                            sum = sum + 1
                        if matrix[r][c+1] == 9:
                            sum = sum + 1
                        if matrix[r+1][c] == 9:
                            sum = sum + 1
                        if matrix[r][c-1] == 9:
                            sum = sum + 1
                        matrix[r][c] = sum
                else:
                    if matrix[r][c] == 0 and r==0 and c==0:
                        sum = 0
                        if matrix[r][c+1] == 9:
                            sum = sum + 1
                        if matrix[r+1][c] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum
                    if matrix[r][c] == 0 and r==0 and c==M-1:
                        sum = 0
                        if matrix[r][c-1] == 9:
                            sum = sum + 1
                        if matrix[r+1][c] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum
                    if matrix[r][c] == 0 and r==N-1 and c==0:
                        sum = 0
                        if matrix[r-1][c] == 9:
                            sum = sum + 1
                        if matrix[r][c+1] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum
                    if matrix[r][c] == 0 and r==N-1 and c==M-1:
                        sum = 0
                        if matrix[r][c-1] == 9:
                            sum = sum + 1
                        if matrix[r-1][c] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum
                    if matrix[r][c] == 0 and r>0 and c==0:
                        sum = 0
                        if matrix[r-1][c] == 9:
                            sum = sum + 1
                        if matrix[r][c+1] == 9:
                            sum = sum + 1
                        if matrix[r+1][c] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum
                    if matrix[r][c] == 0 and r==0 and c>0:
                        sum = 0
                        if matrix[r][c+1] == 9:
                            sum = sum + 1
                        if matrix[r+1][c] == 9:
                            sum = sum + 1
                        if matrix[r][c-1] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum
                    if matrix[r][c] == 0 and r>0 and c==M-1:
                        sum = 0
                        if matrix[r-1][c] == 9:
                            sum = sum + 1
                        if matrix[r+1][c] == 9:
                            sum = sum + 1
                        if matrix[r][c-1] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum
                    if matrix[r][c] == 0 and r==N-1 and c>0:
                        sum = 0
                        if matrix[r-1][c] == 9:
                            sum = sum + 1
                        if matrix[r][c+1] == 9:
                            sum = sum + 1
                        if matrix[r][c-1] == 9:
                            sum = sum + 1   
                        matrix[r][c] = sum

        for r in range(N):

            result = "".join(map(str,matrix[r]))
            print(result)

    except EOFError:
        break
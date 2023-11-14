while True:
    try:
        M, N = map(int, input().split())

        matrix = []

        for i in range(M):
            row = []
            row = input().split()
            row = [int(char) for char in row]
            matrix.append(row)

        #print(matrix)
        pos_1 = []
        pos_2 = []

        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 1:
                    pos_1.append(r)
                    pos_1.append(c)
                if matrix[r][c] == 2:
                    pos_2.append(r)
                    pos_2.append(c)

        #print(pos_1)
        #print(pos_2)

        #calculating difference
        x_dist = abs(pos_1[0] - pos_2[0])
        y_dist = abs(pos_1[1] - pos_2[1])

        #print(x_dist)
        #print(y_dist)

        time = x_dist + y_dist
        print(time)
    
    except EOFError:
        break
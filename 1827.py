while True:
    try:

        N = int(input())

        if 5<=N<=101 and N%2!=0:

            matrix = []

            for r in range(N):
                row = []
                for c in range(N):
                    row.append("0")
                matrix.append(row)

            pad = int(N/3)

            for r in range(N):
                for c in range(N):

                    if r==c:
                        matrix[r][c]="2"
                    
                    if r==N-c-1:
                        matrix[r][c]="3"

                    if r>pad-1 and r<N-pad and c>pad-1 and c<N-pad:
                        matrix[r][c]="1"

                    if r==int(N/2) and c==int(N/2):
                        matrix[r][c] ="4"

            for r in range(N):
                M = ''.join(matrix[r])
                print(M)
            print()

    except EOFError:
        break


#Has errors
#https://github.com/brenonf/URI-python-3/blob/master/1435.py

while True:

    N = int(input())

    if N == 0:
        break

    #creating the matrix with zeros
    matrix = []
    for r in range(N):
        row = []
        for c in range(N):
            row.append(0)
        matrix.append(row)

    #calculating how many layers needed
    if N%2==0:
        layer = int(N/2)
    else:
        layer = 1+int(N/2)

    #print(f"layer = {layer}")

    #Changin values accordingly
    min = 0
    max = N
    count = 0
    for l in range(layer):
        count+=1
        for r in range(min,max):
            for c in range(min,max):
                matrix[r][c]=count
        min+=1
        max-=1

    print(matrix)
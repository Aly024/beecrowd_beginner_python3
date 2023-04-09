mode = input()
n = 12
matrix = []

for r in range(n):

    row = []

    for items in range(n):

        item = float(input())

        row.append(item)

    matrix.append(row)
    
#print(matrix)
output = 0
length = 0

if mode == "S":

    for i in range(n):

        init_output = matrix[i][i+1:]
        output += sum(init_output)
    
    print(f"{output:.1f}")

if mode == "M":

    for i in range(n):

        init_output = matrix[i][i+1:]
        length += len(init_output)
        output += sum(init_output)
    
    output = output/length
    print(f"{output:.1f}")
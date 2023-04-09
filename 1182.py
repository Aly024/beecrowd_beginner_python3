C = int(input())
mode = input()

matrix = []

for r in range(12):

    row = []

    for item in range(12):

        item_row = float(input())
        row.append(item_row)

    matrix.append(row)

#print(matrix)
output = 0

if mode == "S":

    for i in range(12):

        out_init = matrix[i][C]
        #out_final = out_init[C]
        output += out_init
    
    print(f"{output:.1f}")

if mode == "M": 

    for i in range(12):

        out_init = matrix[i]
        out_final = out_init[C]
        output += out_final
    
    output = output/12

    print(f"{output:.1f}")
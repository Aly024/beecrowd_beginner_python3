O = input()
matrix = []

for r in range(12):

    row = []

    for item in range(12):

        item_row = float(input())
        row.append(item_row)

    matrix.append(row)

#print(matrix)

output = 0

if O == "S":

    result_final = 0

    for i in range(12):

        init_row = matrix[i]
        output = init_row[i+1:]
        result = sum(output)
        result_final += result

    print(f"{result_final:.1f}")

if O == "M":

    result_final = 0
    count = 12
    for_avg = 0

    for i in range(12):

        init_row = matrix[i]
        output = init_row[i+1:]
        result = sum(output)
        result_final += result
        count -= 1
        for_avg += count

    result_final = result_final / for_avg    

    print(f"{result_final:.1f}")




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
no_items = 0
mid = int(n/2)
for i in range(mid,n):

    #print(f"i= {i}")
    item_select = matrix[i][n-i:i]
    #print(item_select)
    no_items += len(item_select)
    output += sum(item_select)

if mode == "S":

    print(f"{output:.1f}")

if mode == "M":

    output = output / no_items
    print(f"{output:.1f}")
